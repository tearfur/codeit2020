import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/cluster', methods=['POST'])
def evaluateCluster():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))

    M = len(data[0])
    N = len(data)

    ans = 0
    if 3 <= M <= 1000 and 3 <= N <= 1000:
        read = [[False] * M] * N


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


        for i, row in enumerate(data):
            for j, unit in enumerate(row):
                if unit == "1" and not read[i][j]:
                    search(i, j)
                    ans += 1

logging.info("My result :{}".format(ans))
return json.dumps({"answer": ans});



