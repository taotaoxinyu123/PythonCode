import console_websocket
import _thread
import time

def on_message(ws, message):
    print("recv message:")
    print(message)

def on_error(ws, error):
    print("### error ###")
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("### open ###")
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    _thread.start_new_thread(run, ())

if __name__ == "__main__":
    console_websocket.enableTrace(True)
    ws = console_websocket.WebSocketApp("ws://echo.console_websocket.org/",
                                        on_open=on_open,
                                        on_message=on_message,
                                        on_error=on_error,
                                        on_close=on_close)
    ws.send("hhhh")
    ws.run_forever()