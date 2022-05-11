from flask import Flask, request, render_template
import time
import json

app = Flask(__name__)

DB_FILE = "data/db.json"

def load_messages():
    json_file = open(DB_FILE, "r")
    data = json.load(json_file)  
    return data["messages"]

all_messages = load_messages()


def save_messages():
    data = {
        "messages": all_messages
    }
    json_file = open(DB_FILE, "w")
    json.dump(data, json_file)
    return

def print_message(msg):
    print(f"[{msg['sender']}]: {msg['text']} / {msg['time']}")

def add_message(sender, text):
    new_message = {
        "sender": sender,
        "text": text,
        "time": time.strftime("%H:%M:%S"),
    }
    all_messages.append(new_message)
    save_messages()

@app.route("/get_messages")
def get_messages():
    return {"messages": all_messages}


@app.route("/")
def main_page():
    return "Hello, this is Skill Chat v0.1"

@app.route("/send_message")
def send_message():
    sender = request.args["name"]
    text = request.args["text"]
    add_message(sender, text)
    return "OK"


@app.route("/chat")
def display_chat():
    return render_template("index.html")


app.run()
