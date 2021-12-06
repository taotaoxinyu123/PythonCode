import websocket
from threading import Thread
import time
import json


def on_message(ws, message):
    if message.find("tock") > -1:
        # print("recv message:" + message)
        pass
    else:
        print("recv message:" + message)

def on_error(ws, error):
    print("### error ###")
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("### open ###")
    thread_tik_tok = Thread(target=send_tik_tok, args=(ws,))
    thread_tik_tok.start()
    time.sleep(3)
    # 查询主机
    print("### 查询主机 ###")
    thread_select_1 = Thread(target=send_special_msg, args=(ws, select_type("QueryPrimary", "10.10.10.239"),))
    thread_select_2 = Thread(target=send_special_msg, args=(ws, select_type("QueryPrimary", "10.10.10.232"),))
    thread_select_1.start()
    thread_select_2.start()
    time.sleep(3)
    # 提升主机
    print("### 提升主机 ###")
    thread_primary_up = Thread(target=send_special_msg, args=(ws, select_type("PrimaryUp", "10.10.10.239"),))
    thread_primary_up.start()
    thread_select_3 = Thread(target=send_special_msg, args=(ws, select_type("QueryPrimary", "10.10.10.239"),))
    thread_select_4 = Thread(target=send_special_msg, args=(ws, select_type("QueryPrimary", "10.10.10.232"),))
    thread_select_3.start()
    thread_select_4.start()
    time.sleep(3)
    # 主机倒机
    print("### 主机倒机 ###")
    thread_primary_down = Thread(target=send_special_msg, args=(ws, select_type("PrimaryDown", "10.10.10.239"),))
    thread_primary_down.start()
    thread_select_1 = Thread(target=send_special_msg, args=(ws, select_type("QueryPrimary", "10.10.10.239"),))
    thread_select_2 = Thread(target=send_special_msg, args=(ws, select_type("QueryPrimary", "10.10.10.232"),))
    thread_select_1.start()
    thread_select_2.start()
    time.sleep(3)
# 发送心跳信息
def send_tik_tok(websocket_):
    while True:
        tick_tok_dict:dict = {
            "type": "/tick_tock",
            "id": "1",
            "time": "2021-11-01 07:00:00",
            "ip": "10.10.10.239",
            "data": "tick"
        }
        tick_tok_json:json = json.dumps(tick_tok_dict)
        print("send:" + str(tick_tok_json))
        websocket_.send(tick_tok_json.encode("gbk"))
        time.sleep(4)

# 提升主机
def select_type(type:str, ip:str):
    while True:
        if type == "PrimaryUp":
            PrimaryUp: dict = {
                "type": "/primary_up/1",
                "id": "2",
                "time": "2021-11-01 07:00:00",
                "ip": ip
            }
            return PrimaryUp
        elif type == "PrimaryDown":
            PrimaryDown: dict = {
                "type": "/primary_down/1",
                "id": "3",
                "time": "2021-11-01 07:00:00",
                "ip": ip
            }
            return PrimaryDown
        elif type == "ManualDown":
            ManualDown: dict = {
                "type": "/manual_down/1",
                "id": "4",
                "time": "2021-11-01 07:00:00",
                "ip": ip
            }
            return ManualDown
        elif type == "QueryPrimary":
            QueryPrimary: dict = {
                "type": "/query_primary/1",
                "id": "5",
                "time": "2021-11-01 07:00:00",
                "ip": ip
            }
            return QueryPrimary
        else:
            print("not find")

# 发送其他信息
def send_special_msg(websocket_, content_dict:dict):
    content_json:json = json.dumps(content_dict)
    websocket_.send(content_json.encode("gbk"))
    print("send:" + str(content_json))

if __name__ == "__main__":
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp("ws://172.16.1.55:9002/",
                                        on_open=on_open,
                                        on_message=on_message,
                                        on_error=on_error,
                                        on_close=on_close)
    ws.run_forever()