from app import db, dt

class Interactions(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userID = db.Column(db.Integer, nullable=False, unique=True)
    # chat_instance = db.Column(db.String, nullable=False, unique=True)
    # user_prompt = db.Column(db.String(255))
    # ai_response = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, nullable=False, default=dt.datetime.now(dt.timezone.utc))

    def __repr__(self):
        return f"Interactions('{self.id}','{self.chat_instance}','{self.user_prompt}','{self.ai_response}','{self.timestamp}')"

# used to relate each user and several chat instances 
class Mappings(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userID = db.Column(db.Integer, db.ForeignKey('interactions.userID'),  nullable=False)
    chat_instance = db.Column(db.String(500), db.ForeignKey('history.chat_instance'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=dt.datetime.now(dt.timezone.utc))
    
    def __repr__(self):
        return f"Mappings('{self.id}','{self.userID}','{self.chat_instance}','{self.timestamp}')"

# used for storing the chat_instances of users
class History(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # userID = db.Column(db.Integer, nullable=False, unique=True)
    chat_instance = db.Column(db.String(500), unique=True, nullable=False)
    user_prompt = db.Column(db.String(255))
    ai_response = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, nullable=False, default=dt.datetime.now(dt.timezone.utc))

    def __repr__(self):
        return f"History('{self.id}','{self.chat_instance}','{self.user_prompt}','{self.ai_response}','{self.timestamp}')"


def set_interaction(data):
    interactions = Interactions(userID=data['userID'])
    # interaction = Interactions(chat_instance = data['chat_instance'], user_prompt = data['user_prompt'], ai_response = data['ai_response'])
    mappings = Mappings(userID=data['userID'], chat_instance=data['chat_instance'])
    history = History(chat_instance = data['chat_instance'], user_prompt = data['user_prompt'], ai_response = data['ai_response'])

    try:
        db.session.add(interactions)
        db.session.add(mappings)
        db.session.add(history)
        db.session.commit()
        db.session.close()
        print("DB Insert successful : insert Interaction, insert mappings, insert history")
        return 
    except Exception as e:
        print('DB error: ', e)
    return False

def db_get_history():
    try:
        data = Interactions.query.all()
        print("DB Fetch SUccessful: db_get_history()")
        return data

    except Exception as e:
        print('DB fetch error: db_get_history() ', e)
        return False
    
