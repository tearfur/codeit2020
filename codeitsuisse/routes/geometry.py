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

        inter = {"x": ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denom,
                "y": ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denom}

        if min(x1, x2) <= inter["x"] <= max(x1, x2) and min(y1, y2) <= inter["y"] <= max(y1, y2):
            return inter


    ans = []
    for i, pt in enumerate(shape):
        nextIndex = (i + 1) % len(shape)
        ret = findIntersection(pt["x"], pt["y"], shape[nextIndex]["x"], shape[nextIndex]["y"], line[0]["x"], line[0]["y"], line[1]["x"], line[1]["y"])
        if ret is not None:
            ans.append(ret)
        else:
            continue

    logging.info("My result :{}".format(ans))
    return json.dumps(ans);



