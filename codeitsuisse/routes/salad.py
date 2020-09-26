import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/salad-spree', methods=['POST'])
def evaluateSalad():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))

    n = data.get("number_of_salads");
    prices = data.get("salad_prices_street_map")
    ans = 0
    
    for i in prices:
        count = 0
        tmpSum = 0
        for j in i:
            if count >= n:
                ans = tmpSum if ans == 0 else min(ans, tmpSum)
                tmpSum = 0
                count = 0
            elif j != "X":
                tmpSum += int(j)
                count += 1
            else:
                tmpSum = 0
                count = 0

    logging.info("My result :{}".format(ans))
    return json.dumps(ans);



