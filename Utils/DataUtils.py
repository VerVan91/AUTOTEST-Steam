import json


class DataUtils:
    DATA_FILE = '../TestData/test_data.json'
    CONFIG_FILE = '../Config/config_data.json'

    @staticmethod
    def data_json(url):
        with open(url) as f:
            content = f.read()
            content_dict = json.loads(content)
        return content_dict

    @classmethod
    def test_data_json(cls):
        return cls.data_json(cls.DATA_FILE)

    @classmethod
    def config_data_json(cls):
        return cls.data_json(cls.CONFIG_FILE)
