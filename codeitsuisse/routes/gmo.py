import logging
import json
from math import ceil

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/intelligent-farming', methods=['POST'])
def evaluateGMO():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))

    seqs = data["list"]


    def fillA(str_l, rem, n):
        for num in range(min(rem, n)):
            str_l.append("A")
            rem -= 1
        return rem


    for seq in seqs:
        a = seq["geneSequence"].count("A")
        c = seq["geneSequence"].count("C")
        g = seq["geneSequence"].count("G")
        t = seq["geneSequence"].count("T")

        cc_count = c // 2
        acgt_count = min(a, c % 2, g, t)
        a_rem = a - acgt_count
        c_rem = c - cc_count * 2 - acgt_count
        g_rem = g - acgt_count
        t_rem = t - acgt_count
        sep_count = c_rem + g_rem + t_rem

        if sep_count < ceil(a_rem / 2) - 2 and acgt_count > 0:
            acgt_count -= 1
            a_rem += 1
            c_rem += 1
            g_rem += 1
            t_rem += 1

        str_list = []

        for i in range(acgt_count):
            a_rem = fillA(str_list, a_rem, 1)
            str_list.append("ACGT")

        for i in range(cc_count):
            a_rem = fillA(str_list, a_rem, 2)
            str_list.append("CC")

        for i in range(c_rem):
            a_rem = fillA(str_list, a_rem, 2)
            str_list.append("C")

        for i in range(g_rem):
            a_rem = fillA(str_list, a_rem, 2)
            str_list.append("G")

        for i in range(t_rem):
            a_rem = fillA(str_list, a_rem, 2)
            str_list.append("T")

        for i in range(a_rem):
            str_list.append("A")

        seq["geneSequence"] = ''.join(str_list)

    logging.info("My result :{}".format(data))
    return jsonify(data);



