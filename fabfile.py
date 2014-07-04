# root/fabfile.py

from fabric.api import local

# prepare for deployment

def test():
    local("python test_tasks.py -v && python test_users.py -v")


def commit():
    message = raw_input("Enter a git commit message: ")
    local("git add -A && git commit -m '{}'".format(message))

def push():
    local("git push origin master")

def prepare():
    test()
    commit()
    push()
    
