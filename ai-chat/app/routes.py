import random
import uuid
from flask import jsonify, render_template, url_for, flash, redirect, request
from app.models import Interactions, db_get_history, set_interaction
from app import app, dt

global chat_instance
userID=100
# Routes
@app.route('/test')
def test():
    return "Hello, Flask!"

@app.route('/')
@app.route('/home')
def home():
    global chat_instance
    chat_instance = str(uuid.uuid4())
    print(chat_instance)

    return render_template('home.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    global chat_instance
    print(chat_instance)
    data = {}
    req = request.get_json()

    if request.method == 'POST':
        data['userID'] = userID
        data['user_prompt'] = req['user_prompt']
        data['chat_instance'] = chat_instance
        try:
            ai_response = random.random()
            # store the request and response in DB
            data['ai_response'] = str(ai_response)
                
        except Exception:
            print("error")
            data['ai_response'] = "Something went wrong"
        finally:
            print(data)
            set_interaction(data)
    
    return jsonify(data), 200


@app.route('/history', methods=['GET'])
def get_history():
    global chat_instance
    print(chat_instance)

    data = {}
    # req = request.get_json()
    status_code = 0
    if request.method == 'GET':
        data = db_get_history()
        if data == False:
            status_code = 404
        else:
            status_code = 200
    return render_template('history.html', data=data, status_code=status_code)