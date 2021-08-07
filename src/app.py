# import Flask class for app
from flask import Flask
# import CORS for front and back
from flask_cors import CORS
# import data info class
from lib.DataInfo import DataInfo


# create Flask class
app = Flask(__name__)
CORS(app)

Data = DataInfo('data')


@app.route('/history', methods=['GET'])
def history():
      return 'Hello, World!'


# start app
if __name__ == '__main__':
      app.run()
