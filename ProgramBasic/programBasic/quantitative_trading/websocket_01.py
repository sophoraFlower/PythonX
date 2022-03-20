import ssl
import websocket

# 全局计数器
count = 5


def on_message(ws_, message):
    global count
    print(message)
    count -= 1
    # 接收了5次消息之后关闭websocket连接
    if count == 0:
        ws_.close()


if __name__ == "__main__":
    ws = websocket.WebSocketApp(
        "wss://api.gemini.com/v1/marketdata/btcusd?top_of_book=true&offers=true",
        on_message=on_message)
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
