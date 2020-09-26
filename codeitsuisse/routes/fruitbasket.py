import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/fruitbasket', methods=['POST'])
def evaluateFruit():
    dataByteString = request.get_data()
    dataString = dataByteString.decode('utf-8')
    data = json.loads(dataString)
    logging.info("data sent for evaluation {}".format(data))

    fruits = []
    for x in data.values():
        fruits.append(x)

    weight1 = 10
    weight2 = 20
    weight3 = 30

    result = fruits[0]*weight1 + fruits[1]*weight2 + fruits[2]*weight3

    logging.info("My result :{}".format(result))
    return json.dumps(result);
