import os
from configparser import ConfigParser

# Config Class
class Config(object):

    # initial func
    def __init__(self, BASE_PATH):
        # initial global val
        self.BASE_PATH = BASE_PATH
        self.GLOBAL_FILENAME = 'global.conf'
        self.CONF_PATH = '{}/etc'.format(self.BASE_PATH)
        self.CONF_FILE = '{}/{}'.format(self.CONF_PATH, self.GLOBAL_FILENAME)

        # initial configObj
        configParserObj = ConfigParser()
        configParserObj.read(self.CONF_FILE)

        # initial config val
        self.SERVER_HOST = configParserObj.get('SERVER', 'HOST')
        self.SERVER_PORT = configParserObj.get('SERVER', 'PORT')
        self.SERVER_API = configParserObj.get('SERVER', 'API')
        self.SERVER_KEY = configParserObj.get('SERVER', 'API_KEY')
        self.SERVER_SEC = configParserObj.get('SERVER', 'API_SEC')

    # directory initial function
    def dir_init(self, dir):
        if not os.path.exists(dir):
            try:
                os.mkdir(dir)

            except Except as e:
                sys.stderr.write('[Error][%s]' % (e))
                sys.stderr.flush()

        return(True)
