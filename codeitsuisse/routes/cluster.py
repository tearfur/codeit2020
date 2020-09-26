import logging
import json
from queue import Queue

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/cluster', methods=['POST'])
def evaluateCluster():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))

    ans = 0
    if 3 <= M <= 1000 and 3 <= N <= 1000:
        read = [[False] * M] * N


        def search(i, j):
            q = Queue()
            q.put([i, j])
            while not q.empty():
                x, y = q.get()
                read[x][y] = True
                if x > 0:
                    if y > 0 and data[x - 1][y - 1].isnumeric() and not read[x - 1][y - 1]:
                        q.put([x - 1, y - 1])
                    if data[x - 1][y].isnumeric() and not read[x - 1][y]:
                        q.put([x - 1, y])
                    if y < M - 1 and data[x - 1][y + 1].isnumeric() and not read[x - 1][y + 1]:
                        q.put([x - 1, y + 1])
                if x < N - 1:
                    if y > 0 and data[x + 1][y - 1].isnumeric() and not read[x + 1][y - 1]:
                        q.put([x + 1, y - 1])
                    if data[x + 1][y].isnumeric() and not read[x + 1][y]:
                        q.put([x + 1, y])
                    if y < M - 1 and data[x + 1][y + 1].isnumeric() and not read[x + 1][y + 1]:
                        q.put([x + 1, y + 1])


        for i, row in enumerate(data):
            for j, unit in enumerate(row):
                if unit == "1" and not read[i][j]:
                    search(i, j)
                    ans += 1

    logging.info("My result :{}".format(ans))
    return json.dumps({"answer": ans});



