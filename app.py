from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from google.cloud import storage

app = Flask(__name__)


@app.route('/collect')
def collectData():
    url = request.get_json()
    return url["url"]


if __name__ == '__main__':
    app.run()
