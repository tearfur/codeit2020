import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/contact_trace', methods=['POST'])
def evaluateContactTrace():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
