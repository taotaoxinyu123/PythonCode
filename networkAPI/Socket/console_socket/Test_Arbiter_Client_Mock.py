from socket import *
from threading import Thread
import json
import time
# 一直发送心跳
def send_tick_tok(tcp_socket):
    while True:
        tick_tok_dict:dict = {
            "type": "/tick_tock",
            "id": "1",
            "time": "2021-11-01 07:00:00",
            "ip": "192.168.0.120",
            "data": "tick"
        }
        tick_tok_json:json = json.dumps(tick_tok_dict)
        print("send:" + str(tick_tok_json))
        tcp_socket.send(tick_tok_json.encode("gbk"))
        time.sleep(1)

# 发送具体内容--eg:提升主机
def send_specify_content(tcp_socket, content_dict:dict):
    # content_dict:dict = {
    #     "type": "/primary_up/1",
    #     "id": "1",
    #     "time": "2021-11-01 07:00:00",
    #     "ip": "192.168.0.120",
    #     "data": "tick"
    # }
    content_json:json = json.dumps(content_dict)
    print("send:" + str(content_json))
    tcp_socket.send(content_json.encode("gbk"))

# 服务端接受数据
def recv_data_from_server(tcp_socket):
    # 从服务器接收数据
    while True:
        # 注意这个1024byte，大小根据需求自己设置
        from_server_msg = tcp_socket.recv(1024)
        # 加上.decode("gbk")可以解决乱码
        print(from_server_msg.decode("gbk"))

if __name__ == '__main__':
    # 1.创建套接字
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    # 2.准备连接服务器，建立连接
    serve_ip = "192.168.0.120"
    serve_port = 9002  # 端口，比如8000
    tcp_socket.connect((serve_ip, serve_port))  # 连接服务器，建立连接,参数是元组形式
    # 多线程 : 线程1:发送心跳  线程2:发送其他内容
    t1 = Thread(target=send_tick_tok, args=(tcp_socket,))
    # 提示主机
    content_dict:dict = {
        "type": "/primary_up/1",
        "id": "1",
        "time": "2021-11-01 07:00:00",
        "ip": "192.168.0.120",
        "data": "tick"
    }
    t2 = Thread(target=send_specify_content, args=(tcp_socket,content_dict,))
    t3 = Thread(target=recv_data_from_server, args=(tcp_socket,))
    t1.start()
    time.sleep(3)
    t2.start()
    t3.start()
    # 发送心跳数据
    # send_data = "今天是2021年08月29日，辰哥给服务器端发送数据了"
    # tcp_socket.send(send_data.encode("gbk"))
    # send_tick_tok(tcp_socket)
    # recv_data_from_server(tcp_socket)
    tcp_socket.close()