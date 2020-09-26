import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/olympiad-of-babylon', methods=['POST'])
def evaluateOlympiad():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))

    daysAvailable = data.get("days")
    booksAvailable = data.get("books")
    print(daysAvailable)
    print(booksAvailable)

    count = 0

    for x in daysAvailable:
        eff = 0
        target = x
        bye = []
        for i in booksAvailable:
            print("Loop i = "+str(i))
            if target == i:
                print("target = i blyat")
                count += 1
                booksAvailable.remove(i)
            elif i < target :
                temp = []
                targetClone = target
                targetClone -= i
                print("tarclone = "+tarClone)
                temp.append(i)
                for j in booksAvailable:
                    if j != i:
                        print("Loop j = "+str(j))
                        if (target - j) >= 0:
                            targetClone -= j
                            print("tarclone = "+ tarClone)
                            temp.append(j)
                            if targetClone < eff or eff == 0:
                                eff = targetClone
                                bye = temp
                temp.clear()
                for x in bye:
                    count += 1
                    booksAvailable.remove(x)

    result = {"optimalNumberOfBooks":count}

    logging.info("My result :{}".format(result))
    return json.dumps(result);
