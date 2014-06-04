from flask.ext.script import Manager

from g4g import app

manager = Manager(app)

if __name__ == "__main__":
    manager.run()

