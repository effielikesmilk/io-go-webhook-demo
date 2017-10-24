# -*- coding:utf8 -*-
from __future__ import print_function   # 禁用print，只能用print()
from future.standard_library import install_aliases
install_aliases()

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
    
    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res) # make_response()的参数必须是字符串
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    my_action = req.get("result").get("action")

    result = req.get("result")

    parameters = result.get("parameters")

    my_previous_action = parameters.get("my-action")

    if my_action == "noRecomPlace":
        my_action = my_previous_action
        res = "铜锣湾怎么样？"
    else:
        res = "那去尖沙咀呗"
    return {
        "speech": res,
        "displayText": res,
        "source": "io-go-webhook-demo"
    }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print ("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
