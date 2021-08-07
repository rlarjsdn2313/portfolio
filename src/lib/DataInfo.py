# for join a path
from os import path
# for read json file
import json


# save information about data
class DataInfo:
      def __init__(self, data_path) -> None:
            # data info file
            self.info_file_name = 'info.json'
            # data_path
            self.data_path = data_path
            # data info file path
            self.info_file_path = path.join(
                  self.data_path, self.info_file_name
            )

            # ready for file
            self.info_file = {}
            # ready for query
            self.howmany = 0

            self.update_info()

      def update_info(self):
            # read data info file
            with open(self.info_file_path, 'r') as f:
                  json_data = json.load(f)
                  self.info_file = json_data

            # save howmany query
            self.howmany = self.info_file['howmany']
