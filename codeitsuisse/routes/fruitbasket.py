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

    pineappleAmount = data.get("maPineapple")
    appleAmount = data.get("maApple")
    watermelonAmount = data.get("maWatermelon")

    pineappleWeight = 30
    appleWeight = 10
    watermelonWeight = 20


    result = appleAmount*appleWeight + watermelonAmount*watermelonWeight + pineappleAmount*pineappleWeight

    logging.info("My result :{}".format(result))
    return json.dumps(result);
