import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/fruitbasket', methods=['POST'])
def evaluateFruit():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    appleAmount = data.get("maApple")
    watermelonAmount = data.get("maWatermelon")


    result = inputValue * inputValue
    logging.info("My result :{}".format(result))
    return json.dumps(result);
