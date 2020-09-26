import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/fruitbasket', methods=['POST'])
def evaluateFruit():
    data = request.get_data();
    json.loads(data)
    json.dump(data, sort_keys=True, indent=4)
    print(data)
    logging.info("data sent for evaluation {}".format(data))

    appleAmount = data.get("maApple")
    watermelonAmount = data.get("maWatermelon")
    bananaAmount = data.get("maBanana")

    appleWeight = 10
    watermelonWeight = 20
    bananaWeight = 30

    result = appleAmount*appleWeight + watermelonAmount*watermelonWeight + bananaAmount*bananaWeight

    logging.info("My result :{}".format(result))
    return json.dumps(result);
