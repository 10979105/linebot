from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import(MessageEvent,TextMessage,TextSendMessage)

app = Flask(__name__)
# Channel Access Token
line_bot_api = LineBotApi('s5YBNSSGg3DnkfM6Vtl+wBCrFOqMEHIK+hfDpyuFcmVxsDnc/1J0r0IS+PkFsGAqInOXfanhP15huw4ILSofFSZZSEsKZFSlTQngNsbkVH41F6dbf0qK8nzlDPucrT4NOeu7zFuLgN3MES1EYqFMlAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('ce1688bf709d921435209419534a18e7')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    #app.logger.info("Request body: " + body)
    print("request: " +body, "signature :" +signature)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'




import os
if __name__ == "__main__":
    app.run