import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/bucket-fill', methods=['POST'])
def evaluateBucket():
    data = request.get_data();
    logging.info("data sent for evaluation {}".format(data))

    print(data)
    return json.dumps(0);



