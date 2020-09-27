import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/supermarket', methods=['POST'])
def walk(x):
    for i in range(len(sol)):
        for j in range(len(sol[i])):
            if sol[i][j] == x:
                if sol[i-1][j] != 0 and sol[i][j-1] != 0 and sol[i+1][j] != 0 and sol[i][j+1] != 0:
                    x = -1
                    return(x)
                if i>0 and sol[i-1][j] == 0 and maze[i-1][j] == 0:
                    sol[i-1][j] = x+1
                if j>0 and sol[i][j-1] == 0 and maze[i][j-1] == 0:
                    sol[i][j-1] == x+1
                if i<len(sol)-1 and sol[i+1][j] == 0 and maze[i+1][j] == 0:
                    sol[i+1][j] == x+1
                if j<len(sol[i])-1 and sol[i][j+1] == 0 and maze[i][j+1] == 0:
                    sol[i][j+1] == x+1

def evaluateMaze():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))

    answer = {}
    tests = data.get("test")

    for x in tests:
        start = tests.get("start")
        end = tests.get("end")
        maze = tests.get("maze")

        sol = []
        for i in range(len(maze)):
            sol.append([])
            for j in range(len(maze[i])):
                sol[j].append(0)
        sol[start[0]][start[1]] = 1

        k=0
        while sol[end[0]][end[1]] == 0 and k >= 0:
            k+=1
            walk(k)

        if sol[end[0]][end[1]] != 0:
            answer[x] = sol[end[0]][end[1]]
        else:
            answer[x] = -1

    logging.info("My result :{}".format(answer))
    return json.dumps(answer);
