from flask import Flask,request,Response
import logging
import json
import requests

rasa_server = "rasa"
database = "database-service"

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route("/chat-rasa",methods=["POST"])
def conversation():
    if request.method == "POST":
        logging.info(".....Starting Conversation.....")
        user_message = request.get_json()
        logging.info("%s",user_message["message"])  # This message is from FRONTEND

        user  = user_message["sender"]
        message = user_message["message"]

        #****************Sending to RASA ***************************
        res = requests.post("http://{}:5005/webhooks/rest/webhook".format(rasa_server),
                        data = json.dumps(user_message))
        messageChatbot = json.loads(res.text)

        tracker = requests.get("http://{}:5005/conversations/{}/tracker".format(rasa_server, user))
        emo = json.loads(tracker.text)["slots"]["emotion"]

        logging.info(messageChatbot) # This message is from RASA
        mess = []
        for msg in messageChatbot:
            logging.info(msg["text"])
            mess.append(msg["text"])

        logging.info(".....Sending to Database chatbot message.....")

        req_mongo = sending_data(
            user,
            message,
            mess,
            emo
        )

        if req_mongo.status_code < 300:
            logging.info("adding correctly in mongo")
        else:
            logging.info("There's was a problem with database")

        return json.dumps({
            "messages": mess,
            "emotion": emo
        })

    else:
        logging.info("There was an error with method POST")
        return Response(status=500)

def sending_data(user,message,chatbot,emo):

    conversation_message = {
        "user": user,
        "message": message,
        "chatbot": chatbot,
        "emotion": emo
    }

    headers = {"Content-type": "application/json", "Accept": "text/plain"}
    res_db = requests.post("http://{}:5004/prueba".format(database),
                        data = json.dumps(conversation_message), headers=headers)
    if res_db.status_code < 300:
        logging.info("...The message is saved...")
        return Response(status=200)
    else:
        logging.info("...There was a error with database...")
        return Response(status=400)
