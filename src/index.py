from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

import os

line_bot_api = LineBotApi(os.getenv("UfEEE43XoRD3XKiS6VJI3Q6yVhgDJRu/81avn5xo1dBlXB2RDxjKOXbkY1C3hbVnsricFOc7FLPwBaD5RvWSxoOnnsJYrgvIs1VP8UF4QciAhUM/QBDf+Zh+Ag78DL6yXKQK9/3iI08yPaCaOCDJmQdB04t89/1O/w1cDnyilFU="))
line_handler = WebhookHandler(os.getenv("aa34b86c7e7617a5174c754c5ce55aca"))
working_status = os.getenv("DEFALUT_TALKING", default = "true").lower() == "true"

app = Flask(__name__)

# domain root
@app.route('/')
def home():
    return 'Hello, World!'

@app.route("/webhook", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        line_handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@line_handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global working_status
    
    if event.message.type != "text":
        return
    
    else :
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text))
        return

if __name__ == "__main__":
    app.run()
