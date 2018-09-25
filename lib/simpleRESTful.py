import os
import json
from flask import request
import flask_restful as restful
from lib.Config import Config

class simpleRESTful(restful.Resource):
    '''
        simpleRESTful is a simple RESTful interface
    '''

    def put(self):
        '''
            put action
        '''

        ## get data
        data_raw = request.form['data']

        ## trans data_raw to json
        data_json = json.loads(data_raw)

        ## preCheck key and sec
        result = data_json
        if not self.preAuth(data_json['key'], data_json['sec']):
            result = None

        ## return
        return(result)

    def post(self):
        '''
            post action
        '''

        ## get data
        data_raw = request.form['data']

        ## trans data_raw to json
        data_json = json.loads(data_raw)

        ## preCheck key and sec
        result = data_json
        if not self.preAuth(data_json['key'], data_json['sec']):
            result = None

        ## return
        return(result)

    def get(self):
        '''
            get action
        '''

        ## get data
        data_raw = request.form['data']

        ## trans data_raw to json
        data_json = json.loads(data_raw)

        ## preCheck key and sec
        result = data_json
        if not self.preAuth(data_json['key'], data_json['sec']):
            result = None

        ## return
        return(result)

    def preAuth(self, key, sec):
        '''
            preAuth is a function to check the key and sec
        '''

        # initial val
        BASE_PATH = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

        ## load config file
        configObj = Config(BASE_PATH)

        if (key == configObj.SERVER_KEY) and (sec == configObj.SERVER_SEC):
            return(True)

        else:
            return(False)
