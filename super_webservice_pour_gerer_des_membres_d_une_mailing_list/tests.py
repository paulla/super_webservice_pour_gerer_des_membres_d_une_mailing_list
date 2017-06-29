import unittest

from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_create_member(self):
        from .views import create_email
        request = testing.DummyRequest()
        info = my_view(request)
        self.assertEqual(info['project'], 'super-webservice-pour-gerer-des-membres-d-une-mailing-list')


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from super_webservice_pour_gerer_des_membres_d_une_mailing_list import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_root(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue(b'Pyramid' in res.body)


if __name__ == '__main__':
    unittest.main()

