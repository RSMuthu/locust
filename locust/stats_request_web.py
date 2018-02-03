import json
import os
from gevent import wsgi
from flask import Flask, make_response, request, render_template

app = Flask(__name__)
app.debug = True
app.root_path = os.path.dirname(os.path.abspath(__file__))

def start(options):
    wsgi.WSGIServer((options.web_host, options.port), app, log=None).serve_forever()

@app.route('/stats/requests')
def stats_request():
    from .web import request_stats
    return request_stats()
