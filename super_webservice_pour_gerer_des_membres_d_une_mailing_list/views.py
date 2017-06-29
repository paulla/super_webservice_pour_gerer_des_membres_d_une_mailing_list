from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPBadRequest, HTTPNotFound, HTTPForbidden, HTTPAccepted, HTTPCreated
from Mailman.MailList import MailList
from Mailman import Errors

def valid_request(func):
    def wrapper(context, request):
        params = {}
        try:
            body = request.json_body
        except:
            raise HTTPBadRequest('Not JSON', body_template='${detail}')
        params['mail'] = body.get('mail')
        # TODO: check if mail is a valid mail
        if params['mail'] is None:
            raise HTTPBadRequest('Missing e-mail', body_template='${detail}')
        try:
            params['liste'] = MailList(request.matchdict.get('liste'), lock=1)
        except Errors.MMUnknownListError:
            raise HTTPNotFound('Unknown list')
        
        return func(request, params)

    return wrapper



@view_config(route_name='membres_liste', request_method="POST", decorator=valid_request)
def create_member(request, params):

    class Membre():
        def __init__(self, mail):
            self.address = mail
    try:
        params['liste'].AddMember(Membre(params['mail']))
        params['liste'].save()
    except Errors.MMAlreadyAMember:
        raise HTTPForbidden('Already a member')
    except Errors.MMBadEmailError:
        raise HTTPBadRequest('Bad email')
    except Errors.MembershipIsBanned:
        raise HTTPForbidden('Membership is banned')
    except Errors.MMSubsribeNeedsConfirmation, Errors.MMNeedApproval:
        raise HTTPAccepted
    else:
        return HTTPCreated

@view_config(route_name='membres_liste', request_method="DELETE")
def delete_member(request):
    return Response('')

# vim:set et sts=4 ts=4 tw=80:
