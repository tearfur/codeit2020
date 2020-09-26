import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/social_distancing', methods=['POST'])
def evaluateSocialDist():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))

    read = [[False] * len(data[0])] * len(data)


    def search(i, j):
        try:
            if data[i][j].isnumeric() and not read[i][j]:
                read[i][j] = True
                search(i - 1, j - 1)
                search(i - 1, j)
                search(i - 1, j + 1)
                search(i, j - 1)
                search(i, j + 1)
                search(i + 1, j - 1)
                search(i + 1, j)
                search(i + 1, j + 1)
        except IndexError:
            pass


    ans = 0
    for i, row in enumerate(data):
        for j, unit in enumerate(row):
            if unit == "1" and not read[i][j]:
                search(i, j)
                ans += 1

    logging.info("My result :{}".format(ans))
    return json.dumps({"answer": ans});



