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
    
    if 1 <= n <= len(prices[0]) <= 100:
        for i in prices:
            count = 0
            tmpSum = 0
            for j, val in enumerate(i):
                if val != "X":
                    count += 1
                    tmpSum += int(val)
                    if count >= n:
                        if count > n:
                            tmpSum -= int(i[j - 10])
                        ans = tmpSum if ans == 0 else min(ans, tmpSum)
                else:
                    count = 0
                    tmpSum = 0

    logging.info("My result :{}".format(ans))
    return json.dumps({'result': ans});



