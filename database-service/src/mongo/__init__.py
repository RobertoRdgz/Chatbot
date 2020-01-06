from flask import Flask, request, Response
import requests
from pymongo import MongoClient
import logging
import requests
import random
import json

mongo = "db"

myclient = MongoClient("mongodb://{}:27017/".format(mongo))
mydb = myclient["mydatabase"]
conv = mydb["chat"]

# INSERT DUMMY DOC

default_conversation = {
    "user": "Default",
    "password": "password",
    "conversation":[{"message": "Hi, this is a Default message",
                    "chatbot": "Ok, then this is a Default answer"}]
}

chatbot_names = [
    "Charlie",
    "Frankie",
    "Sidney",
    "Denver",
    "Robin",
    "Jael",
    "Perry",
    "Jules",
    "Jackie",
    "Ridley",
    "Timber",
    "Alex",
    "Andy",
    "Ariel",
    "Charlie",
    "Cris",
    "Francis",
    "Jessie",
    "Joss"
]

myquery_2 = { "user": default_conversation["user"]}
mydoc_2 = conv.find(myquery_2)

if len(list(mydoc_2)) > 0:
    pass

else:
    y = conv.insert_one(default_conversation)

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route("/prueba", methods=["POST"])
def sending_message():
    if request.method == "POST":
        conversation_message = request.get_json()
        logging.info(".....Here's the message.....")
        logging.info(conversation_message)

        logging.info("..... Updating conversation .....")
        new_conversation = {"message": conversation_message["message"],
                            "chatbot": conversation_message["chatbot"],
                            "emotion": conversation_message["emotion"]}

        conv.update({"user": conversation_message["user"]},
                    {'$push': {"conversation": new_conversation}})

        logging.info("..... Finishing to update .....")

        return Response(status=200)

    else:
        logging.info("...There was an error with method POST in database...")
        return Response(status=400)

@app.route("/login",methods=["POST"])
def login():
    if request.method == "POST":
        logging.info("..... Getting the conversation .....")
        login_user = request.get_json()

        myquery_login = { "user": login_user["sender"]}
        mydoc_login = conv.find(myquery_login)
        doclist = list(mydoc_login)
        if doclist:
            doc = doclist[0]
            if "conversation" in doc.keys():
                con = doc["conversation"]
                icon_db = doc["icon"]
                chatbot_n = doc["chatbot_name"]
                logging.info("..... Sending the conversation of the user .....")
                return json.dumps({
                    "conversation": con,
                    "icon": icon_db,
                    "chatbot_name": chatbot_n
                })

            else:
                con = []
                icon_db = doc["icon"]
                chatbot_n = doc["chatbot_name"]
                logging.info("..... Sending the conversation of the user .....")
                return json.dumps({
                    "conversation": con,
                    "icon": icon_db,
                    "chatbot_name": chatbot_n
                })

        else:
            data_user = {
                "user": login_user["sender"],
                "password": login_user["password"],
                "icon": login_user["icon"],
                "chatbot_name": random.choice(chatbot_names)
            }
            conv.insert_one(data_user)

            logging.info("..... new user was saved in Mongo .....")
            return Response(status=200)

@app.route("/validate", methods=["POST"])
def validate():
    if request.method == "POST":
        logging.info(".....Looking for User.....")
        validate_user = request.get_json()

        myquery_validate = { "user": validate_user["sender"]}
        mydoc_login = conv.find(myquery_validate)
        doclist_validate = list(mydoc_login)
        if doclist_validate:
            doc = doclist_validate[0]
            pw = doc["password"]

            logging.info("..... Sending the password of the user .....")
            return json.dumps({
                "password": pw
            })

        else:
            logging.info("..... No encontre al usuario .....")
            return Response(status=400)

    else:
        logging.info("..... Trouble with method POST .....")
