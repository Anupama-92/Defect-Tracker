import psutil
import pytest

from ._Wrapper.Shared.Util.TestLog import cogtestlog
from ._Wrapper.Shared.Util.logger import COGStaticLogger
from ._Wrapper import helper as delayed_assert


@pytest.mark.tryfirst
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # we only look at actual failing test calls, not setup/teardown
    if (rep.when == "call" or rep.when == "setup") and rep.failed:
        # Log CPU percent at failure
        try:
            cpu_percent = psutil.cpu_percent(interval=.1)
            virtual_mem = psutil.virtual_memory()
            COGStaticLogger.logger_adapter.info("CPU Percent: {}\tVirtual Memory: {}".format(cpu_percent, virtual_mem))
        except Exception:
            pass

        COGStaticLogger.get_screenshot(rep.nodeid[rep.nodeid.rfind("::") + 2:], adtl_filename_text='fail')

    return rep


@pytest.fixture(scope='function', autouse=True)
def set_test_name_within_log_object(request):
    """Fixture function is called with every test to set the test name within the Log() object.
    This allows for the test name to be used in screenshots and other logging items."""
    COGStaticLogger.set_test_name(request.function.__name__)
    cogtestlog().info('Test has started.')


def pytest_report_teststatus(report):
    if report.when == "call" or report.when == "teardown":
        if delayed_assert.any_failures():
            report.outcome = "failed"
            report.longrepr = "{0}\n\n{1}".format(report.longrepr, delayed_assert.get_failure_report())
            delayed_assert.clear_expectations()
    if report.when == "call":
        if report.outcome == 'passed':
            cogtestlog().info('Test passed.')
        else:
            cogtestlog().error('Test failed.')
