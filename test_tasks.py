# root/test_tasks.py

import os, unittest
from app import app, db
from app.models import User, FTasks
from config import basedir
from datetime import datetime, date

TEST_DB = 'test.db'

class Tasks(unittest.TestCase):

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


    def create_task(self):
        return self.app.post('tasks/add/', data=dict(
            name='Task',
            due_date = '06/07/2014',
            priority='1',
            posted_date = '06/07/2014',
            status = '1'
            ), follow_redirects=True)



    # tests

    def test_add_new_task(self):
        self.create_user()
        self.login('James','asdfasdf')
        self.app.get('tasks/tasks', follow_redirects=True)
        response = self.create_task()
        response_text = response.get_data(as_text=True)
        assert response_text.find('New entry was success')!=-1

    def test_users_can_complete_tasks(self):
        self.create_user()
        self.login('James','asdfasdf')
        self.app.get('tasks/tasks',follow_redirects=True)
        self.create_task()
        response=self.app.get("tasks/complete/1/", follow_redirects=True)
        response_text = response.get_data(as_text=True)
        assert response_text.find("The task was marked as complete")!=-1

    def test_users_can_incomplete_tasks(self):
        self.create_user()
        self.login('James','asdfasdf')
        self.app.get('tasks/tasks',follow_redirects=True)
        self.create_task()
        response=self.app.get("tasks/incomplete/1/", follow_redirects=True)
        response_text = response.get_data(as_text=True)
        assert response_text.find("The task was marked as incomplete")!=-1

    def test_users_can_delete_tasks(self):
        self.create_user()
        self.login('James', 'asdfasdf')
        self.app.get('tasks/tasks', follow_redirects=True)
        self.create_task()
        response=self.app.get('tasks/delete/1/', follow_redirects=True)
        response_text=response.get_data(as_text=True)
        assert response_text.find('The task was deleted')!=-1

    def test_users_cannot_add_tasks_when_error(self):
        self.create_user()
        self.login('James', 'asdfasdf')
        self.app.get('tasks/tasks', follow_redirects=True)
        response=self.app.post('tasks/add/',data=dict(
            name='Task',
            duedate = '',
            priority='1',
            posted_date='',
            status='1'
            ), follow_redirects=True)
        response_text=response.get_data(as_text=True)
        assert response_text.find('Error in the Posted Date')!=-1

    # testing the models

    def test_users_can_add_tasks_model(self):
        self.create_user()
        self.login('James', 'asdfasdf')
        self.app.get('tasks/tasks', follow_redirects=True)
        new_task=FTasks('Task',date.today(),'1',date.today(),'1','1')
        db.session.add(new_task)
        db.session.commit()
        test = db.session.query(FTasks).all()
        for t in test:
            assert t.name == 'Task'

if __name__=='__main__':
    unittest.main()
        
        
    
        

if __name__== "__main__":
    unittest.main()
