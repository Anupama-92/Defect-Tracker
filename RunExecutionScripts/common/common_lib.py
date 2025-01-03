import os


class CommonPaths(object):
    project_root = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__))))
    log_directory = os.path.join(project_root, 'logs')
    test_logs_directory = os.path.join(log_directory, 'test_logs')
    src_main = os.path.join(project_root, 'CognineAutomationSuite')
    screenshots_directory = os.path.join(log_directory, 'screenshots')
    src_external = os.path.join(src_main, 'external')
    driver_logs = os.path.join(src_external, "DriverLogs")
