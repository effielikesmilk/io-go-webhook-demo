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


@app.route('/webhook', methods=['POST'])
def triggerevent():
    req = request.get_json(silent=True, force=True)
    action = req.get("result").get("action")
    if action == "needaparkinglot":
        time.sleep(20)
        event_name = "eating-event"
        res = {
            "followupEvent": {
                "name": event_name,
                "data": {

                }
            }
        }
        res = json.dumps(res, indent=4)
        r = make_response(res)
        r.headers['Content-Type'] = 'application/json'
    else:
        r = "fail"
    return r


def processRequest(req):
    my_action = req.get("result").get("action")

    result = req.get("result")

    parameters = result.get("parameters")

    if my_action == "noRecomPlace":
        my_action = my_previous_action
        res = "铜锣湾怎么样？"
    elif my_action == "noPlanedPlace":
        res = "那去尖沙咀呗！"
    elif my_action == "chooseacar":
    	res = "你可以选择xxx路线，离它较近的停车场是xxx，价格为xxx，你需要预约停车位么？"
    elif my_action == "changeparkinglot":
    	res = "那你觉得xxx停车场怎么样？它的价格是xxx，暂有xxx个空闲停车位，需要预约么？"
    elif my_action == "needaparkinglot":
    	res = "好的，前往xxx停车场xxx号停车位，到达后开始计费"
    	# event_name = "eating-event";
    	# event_para_time = "14:00";
    	# event_para_place = "麦当劳";
    else:
    	return {}
    return {
        "speech": res,
        "displayText": res,
        "source": "io-go-webhook-demo"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print ("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
