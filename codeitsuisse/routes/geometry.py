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
    
    logging.info("{}".format(shape))

    logging.info("My result :{}".format(ans))
    return json.dumps({'result': ans});



