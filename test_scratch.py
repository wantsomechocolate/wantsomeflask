#root/test_scratch.py

import test_users

import os, unittest
from app import app, db
from app.models import User, FTasks
from config import basedir
from datetime import datetime, date

TEST_DB = 'test.db'



app.config['TESTING'] = True
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir, TEST_DB)
app = app.test_client()
db.create_all()
#new_user = User('James','wantsomechocolate@gmail.com','asdfasdf')
#db.session.add(new_user)
#db.session.commit()

def login(username, password):
    return app.post('users/', data=dict(
            name=username,
            password=password
            ), follow_redirects=True)

def create_user():
    new_user = User('James','wantsomechocolate@gmail.com',
                    'asdfasdf')
    db.session.add(new_user)
    db.session.commit()

create_user()

#response=login('James','asdfasdf')
login('James','asdfasdf')

#response = app.get('tasks/tasks/', follow_redirects=True)

response_tasks=app.get('tasks//tasks/', follow_redirects=True)
response_tasks_text=response_tasks.get_data(as_text=True)
if response_tasks_text.find('Add a new task')!=-1:
    print ('success')

#response_text=response.get_data(as_text=True)

#response_text.find('Welcome')

db.drop_all()
