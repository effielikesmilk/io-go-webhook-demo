# -*- coding:utf8 -*-
from __future__ import print_function   # 禁用print，只能用print()

import os
import json

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)
    # print(res)
    r = make_response(res) # make_response()的参数必须是字符串
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    my_action = req.get("result").get("action")

    result = req.get("result")

    parameters = result.get("parameters")

    my_previous_action = parameters.get("my-action")

    if my_action == "goSomewhere.no-recom-place":
        my_action = my_previous_action
        res = "那去铜锣湾你觉得ok吗？"
    else:
        res = "那你想去尖沙咀么？"
    return res

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(prot=port)
