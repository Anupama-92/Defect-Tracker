import logging
import os
import sys

from AutomationSuite._Wrapper.DriverInitialization import DriverInitialization
from AutomationSuite._Wrapper.Shared.Util.DateUtil import get_date_serial
from AutomationSuite.cog_config import COGConfig
from RunExecutionScripts.common.common_lib import CommonPaths


class MyLoggerAdaptor(logging.LoggerAdapter):

    @staticmethod
    def get():
        COGConfig.load_from_file()
        log_folder = COGConfig().logging.get('log_folder', 'None')
        if log_folder == 'None' or log_folder == '':
            log_folder = CommonPaths.test_logs_directory
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

        default_formatter = '%(asctime)s [%(levelname)s] %(name)s %(message)s'
        level = logging.getLevelName(COGConfig().log_level)
        logging.basicConfig(filename=log_folder + "/" + MyLoggerAdaptor._get_log_file(), level=level,
                            format=default_formatter)

        # Use root logger
        logger = logging.getLogger('automation')
        return MyLoggerAdaptor(logger, None)

    @staticmethod
    def _get_log_file():
        return "TestRun{0}.log".format(get_date_serial())


class COGStaticLogger:
    logger_adapter = None
    started = False
    test_name = None
    _browser = None

    def __init__(self):
        if not COGStaticLogger.started:
            COGStaticLogger.start()

    @staticmethod
    def start():
        COGStaticLogger.logger_adapter = MyLoggerAdaptor.get()
        # Add a Stream Handler locally to display the live log info in the console (mainly for running in Pycharm)
        if COGConfig().logging['console']:
            console_format = '[%(levelname)s] %(message)s'
            COGStaticLogger._console_handler = logging.StreamHandler(stream=sys.stdout)
            console_formatter = logging.Formatter(console_format)
            COGStaticLogger._console_handler.setFormatter(console_formatter)
            COGStaticLogger.logger_adapter.logger.addHandler(COGStaticLogger._console_handler)

        COGStaticLogger.logger_adapter.logger.setLevel(logging.getLevelName(COGConfig().logging['log_level']))

        COGStaticLogger.started = True

    @staticmethod
    def set_test_name(test_name):
        COGStaticLogger.test_name = test_name

    @staticmethod
    def get_screenshot(test_name=None, adtl_filename_text=None):
        global local_test_runner
        try:
            cog_config = COGConfig.load_from_file()
            if test_name is None:
                test_name = COGStaticLogger.test_name

            # get the CW config file
            cog_config = COGConfig()
            cog_config_contents = cog_config.get_config()

            screenshots_config = cog_config_contents.get('screenshots', {})

            if screenshots_config.get('override'):
                ss_path = screenshots_config.get('path', CommonPaths.screenshots_directory)
            else:
                ss_path = cog_config.logging.get('screenshot_output_folder', CommonPaths.screenshots_directory)

            if not os.path.exists(ss_path):
                os.makedirs(ss_path)

            screenshot_filename = (f"{test_name}_{'' if adtl_filename_text is None else '_' + adtl_filename_text}"
                                   f"{get_date_serial()}.png")

            screenshot_path = os.path.join(ss_path, screenshot_filename)

            DriverInitialization().browser.get_screenshot_as_file(filename=screenshot_path)
            COGStaticLogger.logger_adapter.info("screenshot logged as: %s" % screenshot_path)

        except Exception as ex:
            COGStaticLogger.logger_adapter.warning("screenshot failed: %s" % ex)
