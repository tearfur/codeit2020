import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/inventory-management', methods=['POST'])
def evaluateInventory():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))

    def get_pre_result(d, i, j, search_in, item_in):
        if i == 0:
            ret = ""
            for k in range(j):
                ret += "-" + item_in[k]
            return ret
        elif j == 0:
            ret = ""
            for k in range(i):
                ret += "-" + search_in[k]
            return ret
        if d[i][j] == "ul":
            return get_pre_result(d, i - 1, j - 1, search_in, item_in) + search_in[i - 1]
        elif d[i][j] == "u":
            return get_pre_result(d, i - 1, j, search_in, item_in) + "-" + search_in[i - 1]
        else:
            return get_pre_result(d, i, j - 1, search_in, item_in) + "+" + item_in[j - 1]


    def get_result(res):
        temp = []
        for i, result in enumerate(res):
            temp.append(0)
            temp_str = result
            for j, char in enumerate(result):
                if char == "+" or char == "-":
                    try:
                        if char == "+" and result[j - 2] == "-":
                            temp_str = temp_str.replace(result[j - 2: j + 1], '')
                        elif char == "-" and result[j - 2] == "+":
                            temp_str = temp_str.replace(result[j - 2: j + 2], result[j - 1])
                        else:
                            temp[-1] += 1
                    except IndexError:
                        temp[-1] += 1
            res[i] = temp_str

        return [x for _, x in sorted(zip(temp, res))]


    ans = []
    for search in data:
        pre_results = []
        for item in search["items"]:
            item_lower = item.lower()
            searchIn = search["searchItemName"].lower()
            n = len(searchIn) + 1
            m = len(item_lower) + 1
            l = [[0 for j in range(m)] for i in range(2)]
            d = [["" for j in range(m)] for i in range(n)]

            for i in range(1, n):
                i1 = i % 2
                for j in range(1, m):
                    im = (i - 1) % 2
                    jm = j - 1
                    if searchIn[i - 1] == item_lower[j - 1]:
                        l[i1][j] = l[im][jm] + 1
                        d[i][j] = "ul"
                    elif l[im][j] >= l[i1][jm]:
                        l[i1][j] = l[im][j]
                        d[i][j] = "u"
                    else:
                        l[i1][j] = l[i1][jm]
                        d[i][j] = "l"

            pre_results.append(get_pre_result(d, n - 1, m - 1, search["searchItemName"], item))

        ans.append({"searchItemName": search["searchItemName"], "searchResult": get_result(pre_results)[:10]})

    return json.dumps(ans);



