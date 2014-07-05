##config.py

CSRF_ENABLED = True
SECRET_KEY = "^oW'saZW4*N:SO0_xq.W6,4272h=fq"

### Comment out if not using sqlite3
import os
### name of database file
DATABASE = 'flasktaskr.db'
###grabs the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))
###defines the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)
### the database uri
##SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH

SQLALCHEMY_DATABASE_URI = """postgres://gavdvwwkwqmjwv:GB890krqxqA_zOfWuQLe8EBRvL@ec2-54-225-101-60.compute-1.amazonaws.com:5432/dd5mao2molcn4s"""
