# import Flask class for app
from flask import Flask
# import CORS for front and back
from flask_cors import CORS
# import MySQL for DB
from flask_mysqldb import MySQL
from dotenv import load_dotenv

# create Flask class
app = Flask(__name__)
CORS(app)
mysql = MySQL(app)


@app.route('/')
def hello_world():
      return 'Hello, World!'


# start app
if __name__ == '__main__':
      app.run()
