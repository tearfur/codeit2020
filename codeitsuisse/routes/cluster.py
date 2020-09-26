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

    M = len(data[0])
    N = len(data)

    ans = 0
    if 3 <= M <= 1000 and 3 <= N <= 1000:
        read = [[False for j in range(M)] for i in range(N)]


        def search(i, j):
            q = Queue()
            q.put([i, j])
            read[i][j] = True
            while not q.empty():
                y, x = q.get()
                if y > 0:
                    if x > 0 and data[y - 1][x - 1].isnumeric() and not read[y - 1][x - 1]:
                        q.put([y - 1, x - 1])
                        read[y - 1][x - 1] = True
                    if data[y - 1][x].isnumeric() and not read[y - 1][x]:
                        q.put([y - 1, x])
                        read[y - 1][x] = True
                    if x < M - 1 and data[y - 1][x + 1].isnumeric() and not read[y - 1][x + 1]:
                        q.put([y - 1, x + 1])
                        read[y - 1][x + 1] = True
                if y < N - 1:
                    if x > 0 and data[y + 1][x - 1].isnumeric() and not read[y + 1][x - 1]:
                        q.put([y + 1, x - 1])
                        read[y + 1][x - 1] = True
                    if data[y + 1][x].isnumeric() and not read[y + 1][x]:
                        q.put([y + 1, x])
                        read[y + 1][x] = True
                    if x < M - 1 and data[y + 1][x + 1].isnumeric() and not read[y + 1][x + 1]:
                        q.put([y + 1, x + 1])
                        read[y + 1][x + 1] = True
                if x > 0 and data[y][x - 1].isnumeric() and not read[y][x - 1]:
                    q.put([y, x - 1])
                    read[y][x - 1] = True
                if x < M - 1 and data[y][x + 1].isnumeric() and not read[y][x + 1]:
                    q.put([y, x + 1])
                    read[y][x + 1] = True


        for i, row in enumerate(data):
            for j, unit in enumerate(row):
                if unit == "1" and not read[i][j]:
                    search(i, j)
                    ans += 1

    logging.info("My result :{}".format(ans))
    return json.dumps({"answer": ans});



