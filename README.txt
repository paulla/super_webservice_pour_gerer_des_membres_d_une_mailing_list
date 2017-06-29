super-webservice-pour-gerer-des-membres-d-une-mailing-list
==========================================================

Getting Started
---------------

- Change directory into your newly created project.

    cd super_webservice_pour_gerer_des_membres_d_une_mailing_list

- Create a Python virtual environment.

    python3 -m venv env

- Upgrade packaging tools.

    env/bin/pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    env/bin/pip install -e ".[testing]"

- Run your project's tests.

    env/bin/pytest

- Run your project.

    env/bin/pserve development.ini
