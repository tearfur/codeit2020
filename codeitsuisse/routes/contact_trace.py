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
    count1 = (1 for inf,clu in zip(infectedGenome,clusterGenome) if inf != clu)
    count2 = (1 for inf,ori in zip(infectedGenome,clusterGenome) if inf != ori)

    if count1 <= 2 && count2 <= 2:
        if count1 == 0 && count2 == 0:
            result.append(infected.get("name")+" -> "+cluster.get("name"))
            result.append(infected.get("name")+" -> "+origin.get("name"))
        else if count1 != 0 && count2 == 0:
            result.append(infected.get("name")+"* -> "+cluster.get("name")+" -> "+origin.get("name"))
        else:
            result.append(infected.get("name")+"* -> "+cluster.get("name")+"* -> "+origin.get("name"))

    logging.info("My result :{}".format(result))
    return json.dumps(result);
