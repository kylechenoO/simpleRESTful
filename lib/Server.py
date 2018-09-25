from flask import Flask
import flask_restful as restful
from lib.simpleRESTful import simpleRESTful

## a class to start service
class Server(object):
    def __init__(self, server, port, apiName, key, sec):
        self.server = server
        self.port = port
        self.apiName = apiName
        self.key = key
        self.sec = sec
        self.start(self.server, self.port, self.apiName, self.key, self.sec)

    def start(self, server, port, apiName, key, sec):
        app = Flask(__name__)
        api = restful.Api(app)

        ## api.add_resource(simpleRESTful, '/<string:sn>')
        api.add_resource(simpleRESTful, '/{}'.format(apiName))
        app.run(host = server,  port = port, debug = True)
