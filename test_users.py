# root/test_users.py

import os, unittest
from app import app, db
from app.models import User, FTasks
from config import basedir
from datetime import datetime, date

TEST_DB = 'test.db'

class UserTests(unittest.TestCase):

    # this is a special method that is executed prior to each test

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+\
                os.path.join(basedir, TEST_DB)

        self.app = app.test_client()
        db.create_all()

    # this is a special method that is executed after each test

    def tearDown(self):
        db.drop_all()



    # helper methods
    def login(self, username, password):
        return self.app.post('users/', data=dict(
            name=username,
            password=password
            ), follow_redirects=True)

    def logout(self):
        return self.app.get('users/logout', follow_redirects=True)

    def register(self):
        return self.app.post('users/register/', data=dict(
            name= 'James',
            email = 'wantsomechocolate@gmail.com',
            password = 'asdfasdf',
            confirm = 'asdfasdf'
            ), follow_redirects=True)

    def create_user(self):
        new_user = User('James','wantsomechocolate@gmail.com',
                        'asdfasdf')
        db.session.add(new_user)
        db.session.commit()

    # testing the views

    def test_users_can_login(self):
        self.create_user()
        response=self.login('James', 'asdfasdf')
        response_text=response.get_data(as_text=True)
        assert response_text.find('Welcome')!=-1

    def test_users_cannot_login_unless_registered(self):
        response = self.login('James', 'asdfasdf')
        response_text=response.get_data(as_text=True)
        assert response_text.find('Invalid username or password')!=-1

    def test_users_can_logout(self):
        self.create_user()
        self.login('James','asdfasdf')
        response = self.logout()
        response_text=response.get_data(as_text=True)
        assert response_text.find('You are logged out')!=-1

    def test_logged_in_users_can_access_tasks(self):
        self.create_user()
        self.login('James','asdfasdf')
        response = self.app.get('/tasks/tasks', follow_redirects=True)
        response_text = response.get_data(as_text=True)
        assert response_text.find('Add a new task')!=-1

    def test_not_logged_in_users_cannot_access_tasks(self):
        response=self.app.post('/tasks/tasks', follow_redirects=True)
        response_text=response.get_data(as_text=True)
        assert response_text.find('You need to login first')

    def test_user_registration(self):
        self.app.get('users/register/',follow_redirects=True)
        response=self.register()
        response_text=response.get_data(as_text=True)
        assert response_text.find('Thanks for registering')



    # testing the models

    def test_new_user_can_register_model(self):
        self.create_user()
        test = db.session.query(User).all()
        for t in test:
            #t.name
            assert t.name == 'James'


if __name__== "__main__":
    unittest.main()
