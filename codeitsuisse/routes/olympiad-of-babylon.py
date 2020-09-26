import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/olympiad-of-babylon', methods=['POST'])
def evaluatePortfolio():
    dataByteString = request.get_data()
    dataString = dataByteString.decode('utf-8')
    data = json.loads(dataString)
    logging.info("data sent for evaluation {}".format(data))

    daysAvailable = data.get(days)
    booksAvailable = data.get(books)
    print(daysAvailable)
    print(booksAvailable)

    c = 0

    inputValue = data[0].get("n");
    result = inputValue * inputValue

    logging.info("My result :{}".format(result))
    return json.dumps(result);
