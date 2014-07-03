# root/test_tasks.py

import os
import unittest
from app import app, db
from app.models import User
from app.models import FTasks
from config import basedir
import datetime

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

    # tests

    def test_add_new_task(self):
        new_task = FTasks(
                    'Task Name',
                    datetime.date(2012,6,5),
                    8,
                    datetime.date(2012,6,5),
                    '1',
                    'mherman'
                    )
        db.session.add(new_task)
        db.session.commit()
        

if __name__== "__main__":
    unittest.main()
