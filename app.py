from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import(MessageEvent,TextMessage,TextSendMessage,)

app = Flask(__name__)
# Channel Access Token
line_bot_api = LineBotApi('JnmSUgVjnr6qaksfmnefZAGdACh2AEic36jiP9aVlsZ7eCpvW0VMwHTQnBgS8K/uInOXfanhP15huw4ILSofFSZZSEsKZFSlTQngNsbkVH4vHmUpRMpFxHfLxgABLtWTGFoN7sT2kfxt6uqpt2jEJAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('0c8d8fea192c7149abcd008868a54c3d')

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
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)