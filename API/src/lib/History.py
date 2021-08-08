# join path
from os import path
# read json file
import json


class History:
      def __init__(self, num: int, data_path: str) -> None:
            # data path
            self.data_path = data_path
            # data number
            self.num = num

            # file path
            self.file_path = path.join(
                  self.data_path, f'{self.num}.json'
            )

            self.title = ''
            self.description = ''
            # [year, month, day, 'SUN...']
            self.date = []
            self.id = 0

            # update model
            self.update()
      
      # update data
      def update(self) -> None:
            # read file
            with open(self.file_path, 'r', encoding='utf-8') as f:
                  json_data = json.load(f)

            # save query
            self.title = json_data['title']
            self.description = json_data['description']
            self.date = json_data['date']
            self.id = json_data['id']

      def to_dict(self) -> dict:
            return {
                  'id': self.id,
                  'title': self.title,
                  'description': self.description,
                  'date': self.date
            }
