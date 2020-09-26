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
    sum = 0
    for j in i:
        if count >= n:
            ans = sum if ans == 0 else min(ans, sum)
            sum = 0
            count = 0
        elif j != "X":
            sum += int(j)
            count += 1
        else:
            sum = 0
            count = 0

    logging.info("My result :{}".format(ans))
    return json.dumps(ans);



