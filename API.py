# Creating api to get data from the database

# importing Required Libraries

from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
from credentials import DATABASE_USER, DATABASE_PASSWORD
from Database1 import MedisageDB
# There are two end points

app = Flask(__name__)
api = Api(app)


class Events(Resource):

    def get(self):
        data = pd.read_csv('users.csv')  # read local CSV
        data = data.to_dict()  # convert dataframe to dict
        return {'data': data}, 200  # return data and 200 OK
    # Getting the data from the database and returning it to the user using Get method


api.add_resource(Events, '/Events')  # Adding the end point to the api

if __name__ == '__main__':
    app.run()