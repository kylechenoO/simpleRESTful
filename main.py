import os
from lib.Config import Config
from lib.Server import Server

if __name__ == '__main__':
    # initial val
    BASE_PATH = os.path.abspath(os.path.dirname(__file__))

    ## load config file
    configObj = Config(BASE_PATH)

    ## start service
    print(configObj.SERVER_API)
    serverObj = Server(configObj.SERVER_HOST, configObj.SERVER_PORT, configObj.SERVER_API, configObj.SERVER_KEY, configObj.SERVER_SEC)
    serverObj.start()

