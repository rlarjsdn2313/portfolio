# import Flask class for app
from flask import Flask
# import CORS for front and back
from flask_cors import CORS
# import data info class
from lib.DataInfo import DataInfo
# import history model
from lib.History import History
# for change dict to json
import json


# create Flask class
app = Flask(__name__)
# for Korean encoding
app.config['JSON_AS_ASCII'] = False
CORS(app)

Info = DataInfo('data')


@app.route('/history', methods=['GET'])
def history():
      datas = []
      # read file
      for num in range(Info.howmany):
            datas.append(
                  History(num, Info.data_path).to_dict()
            )

      return json.dumps({
            'history': datas
      }, ensure_ascii=False)


# start app
if __name__ == '__main__':
      app.run()
