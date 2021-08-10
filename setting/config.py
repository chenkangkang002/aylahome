import os

BASE_PATH = os.path.realpath(os.path.dirname(os.path.dirname(__file__)))
UI_PATH = os.path.join(BASE_PATH, 'lib/ui')
API_PATH = os.path.join(BASE_PATH, 'lib/api')
REPORT_PATH = os.path.join(BASE_PATH, 'report')
SETTING = os.path.join(BASE_PATH, 'setting')
TEST_CASES_PATH = os.path.join(BASE_PATH, 'test_cases')
