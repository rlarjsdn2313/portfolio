# import Flask class for app
from flask import Flask

# create Flask class
app = Flask(__name__)


@app.route('/')
def hello_world():
      return 'Hello, World!'


# start app
if __name__ == '__main__':
      app.run()
