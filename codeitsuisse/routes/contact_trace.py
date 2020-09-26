import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/contact_trace', methods=['POST'])
def evaluateContactTrace():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    infected = data.get("infected")
    infectedGenome = infected.get("genome")
    origin = data.get("origin")
    originGenome = origin.get("genome")
    cluster = data.get("cluster")
    clusterGenome = cluster.get("genome")
    result = []

    count1 = 0
    silentCheck1 = True
    count2 = 0
    silentCheck2 = True
    i=0
    for a,b in zip(infectedGenome,clusterGenome):
        if a != b:
            count1 += 1
            if (i+1)%3 == 0 :
                silentCheck1 = False
        i += 1
    i=0
    for a,b in zip(clusterGenome,originGenome):
        if a != b:
            count2 += 1
            if (i+1)%3 == 0 :
                silentCheck1 = False
        i += 1

    if count1 == 0 and count2 == 0:
        result.append(infected.get("name") + " -> " + cluster.get("name"))
        result.append(infected.get("name") + " -> " + origin.get("name"))

    if count1 <= 2 and count2 <= 2:
        if silentCheck1 == True and silentCheck2 == True:
            result.append(infected.get("name") + " -> " + cluster.get("name") + " -> " + origin.get("name"))
        elif silentCheck1 == False and silentCheck2 == True:
            result.append(infected.get("name") + "* -> " + cluster.get("name") + " -> " + origin.get("name"))
        elif silentCheck1 == True and silentCheck2 == False:
            result.append(infected.get("name") + " -> " + cluster.get("name") + "* -> " + origin.get("name"))
        else:
            result.append(infected.get("name") + "* -> " + cluster.get("name") + "* -> " + origin.get("name"))
        logging.info("My result :{}".format(result))
        return json.dumps(result);
