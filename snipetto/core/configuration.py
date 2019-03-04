import os

SNIPPETTO_HOST = os.environ.get('SNIPPETTO_HOST', 'https://snippetto.trurl.it')
SNIPPETTO_PATH_CONFIGURATION = '/v1/api/paths/'
HOME_DIR = os.path.expanduser('~')
CONFIG_PATH = '{}/.snippetto'.format(HOME_DIR)
