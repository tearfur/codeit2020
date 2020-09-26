import logging
import json
import math

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/revisitgeometry', methods=['POST'])
def evaluateGeometry():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))

    shape = data.get("shapeCoordinates");
    line = data.get("lineCoordinates")
    
    def findIntersection(x1, y1, x2, y2, x3, y3, x4, y4):
        denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

        if math.isclose(denom, 0):
            return None

        temp1 = x1 * y2 - y1 * x2
        temp2 = x3 * y4 - y3 * x4
        inter = {"x": (temp1 * (x3 - x4) - (x1 - x2) * temp2) / denom,
                "y": (temp1 * (y3 - y4) - (y1 - y2) * temp2) / denom}

        if min(x1, x2) <= inter["x"] <= max(x1, x2) and min(y1, y2) <= inter["y"] <= max(y1, y2):
            return inter


    ans = []
    if 1 <= len(shape) <= 100:
        for i, start in enumerate(shape):
            endIndex = (i + 1) % len(shape)
            ret = findIntersection(start["x"], start["y"], shape[endIndex]["x"], shape[endIndex]["y"],
                                line[0]["x"], line[0]["y"], line[1]["x"], line[1]["y"])
            if ret is not None:
                ans.append(ret)
            else:
                continue

    logging.info("My result :{}".format(ans))
    return json.dumps(ans);



