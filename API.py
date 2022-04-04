# Creating api to get data from the database

# importing Required Libraries

from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

# There are two end points

app = Flask(__name__)
api = Api(app)

