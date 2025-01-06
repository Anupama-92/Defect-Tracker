import pytest

from AutomationSuite._Wrapper.login import Login
from AutomationSuite.cog_config import COGConfig


@pytest.fixture()
def microsoft_login(request):
    """
    logs in with microsoft
    """
    if request.keywords._markers.get('skip_login',
                                     request.node.parent.keywords._markers.get('skip_login', False)):
        # do not login is test has skip_login marker
        return

    login_member = get_login_key(request)
    Login().chorus_login(login_member)


def get_login_key(request):
    useloginkey_marker = request.keywords._markers.get('useloginkey',
                                                       request.node.parent.keywords._markers.get('useloginkey', None))
    markers = request.instance.pytestmark
    if useloginkey_marker is None:
        login_key = COGConfig().portal_login
    else:
        login_key = str(list(filter(lambda py_mark: py_mark.name == 'useloginkey', markers))[0].args[0])
    return login_key


@pytest.fixture(scope="function", autouse=True)
def teardown_steps(request):
    def final():

        try:
            COGConfig().load_from_file()
        except:
            pass

    request.addfinalizer(final)


def pytest_configure(config):
    config.addinivalue_line("markers", "chorus: custom mark for chorus tests")
    config.addinivalue_line("markers", "crm: custom mark for crm tests")
    config.addinivalue_line("markers", "crm_homepage: custom mark for crm homepage tests")
