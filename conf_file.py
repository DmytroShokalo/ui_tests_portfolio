import os

ENV_PARAM = os.environ.get('ENV', 'PROD')

if ENV_PARAM == 'PROD':
    print(ENV_PARAM)
    from configs.prod import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ALLURE_RESULTS_DIR = BASE_DIR + '/allure-results'

# WAIT TIME
WAIT_TIME = {
    'timeWaitSmall': 1,
    'timeWaitSmall2': 2,
    'timeWaitNormal': 3,
    'timeWaitLong': 6,
    'timeWaitEpick': 12
}

