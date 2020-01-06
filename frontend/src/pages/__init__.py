from flask import Flask, request,render_template,url_for,session,redirect, Response
import requests
import random
import logging
import json
from flask_login import current_user, login_user, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash


logging.basicConfig(level=logging.INFO)

back_server = "backend"
db_server = "database-service"

app = Flask(
    __name__,
    template_folder="templates",
    # static_folder="static"
)

chatbot_emotions = {
    "anger": [
        "badword",
        "impressed2"
    ],
    "disgust": [
        "anger"
    ],
    "fear": [
        "impressed1"
    ],
    "guilt": [
        "guilt"
    ],
    "joy": [
        "amazing",
        "funny",
        "inlove",
        "kiss",
        "tongue",
        "wink"
    ],
    "sadness": [
        "sad"
    ],
    "shame": [
        "shame"
    ]
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template(
            "index2.html"
        )
    elif request.method == "POST":

        logging.info("Welcome")
        user_and_pass = request.get_json()
        logging.info(user_and_pass)

        user = user_and_pass["sender"]
        icon = user_and_pass["icon"]
        password_hash = generate_password_hash(user_and_pass["password"])
        logging.info(f"password encrypted {password_hash}")
        logging.info(user)
        headers = {"Content-type": "application/json", "Accept": "text/plain"}
        res = requests.post(
            "http://{}:5004/validate".format(db_server),
            data =  json.dumps({"sender": user}),
            headers=headers
        )
        if res.status_code > 300:
            logging.info(".......... New user ...........  ")
            requests.post("http://{}:5004/login".format(db_server),
                        data =  json.dumps({"sender": user, "password": password_hash,
                         "icon": icon}), headers=headers)
            logging.info("User created")
            return json.dumps({"html": None})

        else:
            password_db = json.loads(res.text)
            logging.info("reading password")
            logging.info(f"password {password_db}")

            if check_password_hash(password_db["password"], user_and_pass["password"]) is True:

                logging.info("password correcct")

                conversation_history = requests.post("http://{}:5004/login".format(db_server),
                        data =  json.dumps(user_and_pass), headers=headers)

                conversation = json.loads(conversation_history.text)
                logging.info(conversation)


                convs = []
                for conv in conversation["conversation"]:
                    emotion = conv["emotion"]
                    if emotion is not None:
                        bot_emotion = random.choice(chatbot_emotions[emotion])
                    else:
                        bot_emotion = "normal"

                    mess = render_template(
                        'message2.html',
                        message=conv["message"],
                        avatar=conversation["icon"]
                    )
                    resp = render_template(
                        'response2.html',
                        messages=conv["chatbot"],
                        bot_emotion=bot_emotion
                    )
                    convs.append(mess)
                    convs.append(resp)

                html = "".join(convs)


                return json.dumps({
                    "html": html,
                    "icon": conversation["icon"],
                    "chatbot_name": conversation["chatbot_name"]
                })
            else:
                logging.info(".....Password incorrect, try again......")

                return Response(status=400)



@app.route("/send", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        message = request.get_json()
        logging.info(message)
        headers = {"Content-type": "application/json", "Accept": "text/plain"}
        logging.info("************Make post to back****************")
        req_front=requests.post("http://{}:5000/chat-rasa".format(back_server),data = json.dumps(message), headers = headers)
        bot_response = json.loads(req_front.text)
        logging.info(bot_response)

        emotion = bot_response["emotion"]
        if emotion is not None:
            bot_emotion = random.choice(chatbot_emotions[emotion])
        else:
            bot_emotion = "normal"


        responses = render_template(
            'response2.html',
            messages = bot_response["messages"],
            bot_emotion = bot_emotion
        )

        return json.dumps({
            "html": responses,
            "emotion": bot_response["emotion"]
        })

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/about')
def about_page():
    return render_template('about.html')
