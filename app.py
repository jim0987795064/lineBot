import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message,send_image_message

load_dotenv()


machine = TocMachine(
        states=["user","menu", "viewshow1","viewshow2","viewshow3","viewshow4","viewshow5","viewshow6","ptt","book"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "viewshow1",
            "conditions": "is_going_to_viewshow1",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "viewshow2",
            "conditions": "is_going_to_viewshow2",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "viewshow3",
            "conditions": "is_going_to_viewshow3",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "viewshow4",
            "conditions": "is_going_to_viewshow4",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "viewshow5",
            "conditions": "is_going_to_viewshow5",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "viewshow6",
            "conditions": "is_going_to_viewshow6",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "ptt",
            "conditions": "is_going_to_ptt",
        },
        {
            "trigger": "advance",
            "source": "viewshow1",
            "dest": "book",
            "conditions": "is_going_to_book",
        },
        {
            "trigger": "advance",
            "source": "viewshow2",
            "dest": "book",
            "conditions": "is_going_to_book",
        },
        {
            "trigger": "advance",
            "source": "viewshow3",
            "dest": "book",
            "conditions": "is_going_to_book",
        },
        {
            "trigger": "advance",
            "source": "viewshow4",
            "dest": "book",
            "conditions": "is_going_to_book",
        },
        {
            "trigger": "advance",
            "source": "viewshow5",
            "dest": "book",
            "conditions": "is_going_to_book",
        },
        {
            "trigger": "advance",
            "source": "viewshow6",
            "dest": "book",
            "conditions": "is_going_to_book",
        },
        {"trigger": "go_back", "source": ["ptt","book"], "dest":"user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")
final_states=["ptt","book"]

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text,str):
            continue
        if event.message.text.lower()=='fsm':
            if machine.state!="user":
                machine.go_back()
            send_image_message(event.reply_token,'https://github.com/jim0987795064/lineBot/blob/main/fsm.png?raw=true')
            continue
        
        response=True
        for state in final_states:
            if machine.state==state:
                response=False
                break
        if response:
            machine.advance(event)
        else:
            machine.go_back()
            machine.advance(event)
    return "OK"




@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
