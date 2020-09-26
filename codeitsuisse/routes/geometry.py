import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/revisitgeometry', methods=['POST'])
def evaluateGeometry():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))

    shape = data.get("shapeCoordinates");
    line = data.get("lineCoordinates")
    
    x3, y3 = line[0]["x"], line[0]["y"]
    x4, y4 = line[1]["x"], line[1]["y"]

    ans = []
    for i, pt1 in enumerate(shape[:-1]):
        for pt2 in shape[i + 1:]:
            x1, y1 = pt1["x"], pt1["y"]
            x2, y2 = pt2["x"], pt2["y"]
            print(x1, y1)
            print(x2, y2)

            denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

            if math.isclose(denom, 0):
                continue

            inter = {"x": ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denom,
                    "y": ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denom}

            inter["x"] = round(inter["x"], 2)
            inter["y"] = round(inter["y"], 2)

            if min(x1, x2) <= inter["x"] <= max(x1, x2) and min(y1, y2) <= inter["y"] <= max(y1, y2):
                ans.append(inter)

    logging.info("My result :{}".format(ans))
    return json.dumps(ans);



