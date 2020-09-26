import logging
import json
import operator as op
from functools import reduce

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/social_distancing', methods=['POST'])
def evaluateSocialDist():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))

    tests = data.get("tests");
    
    def ncr(n, r):
        r = min(r, n-r)
        numer = reduce(op.mul, range(n, n-r, -1), 1)
        denom = reduce(op.mul, range(1, r+1), 1)
        return numer // denom  # or / in Python 2


    ans = {}
    for key in tests:
        case = tests[key]
        fixed = case["people"] + (case["people"] - 1) * case["spaces"]
        free = case["seats"] - fixed

        ans[key] = ncr(case["people"] + 1 + free - 1, free)

    logging.info("My result :{}".format(ans))
    return json.dumps({"answers": ans});



