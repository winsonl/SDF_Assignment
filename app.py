from flask import Flask
from flask_restful import Resource, Api, reqparse
import requests
import json
import pandas as pd
import datetime

app = Flask(__name__)
api = Api(app)

class text(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('name', required = True)
        parser.add_argument('expires_in', required=True)
        parser.add_argument('snippet', required=True)

        args = parser.parse_args()
        timeout_increases = int(args['expires_in'])

        expires_at = datetime.datetime.now() + datetime.timedelta(seconds = int(args['expires_in']))

        url = 'https://example.com/snippets'

        headers = {}

        post_data = {
            "url": url,
            "name": args['name'],
            "expires_at": expires_at,
            "snippet": args['snippet']
        }

        json_data = json.dumps(post_data,sort_keys=True, default=str)
        return json_data

        # res = requests.post(url, data=json_data, headers = headers, timeout=timeout_increases)
        # return res

if __name__ == '__main__':
    api.add_resource(text,"/snippets")
    app.run()