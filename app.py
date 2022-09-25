# from flask import Flask

# app = Flask(__name__)


# @app.route('/')
# def hello():
#     return '<h1>Hello, World!</h1>'

from mongodb import CBR

cbr = CBR('cbr-data')
cbr.print_all_data()
