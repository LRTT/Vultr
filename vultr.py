import requests
import json

build = json.load(open("vultr.build.info.json", "r"))

class Base:
    BASE_HOST = "https://api.vultr.com"
    
    def __init__(self, session):
        self.__session = session

    def request(self, method, path, data):
        response = getattr(self.__session, method)(self.BASE_HOST + path, data=data)
        if response.status_code != 200:
            raise Exception(response.text)
        return response.json()

    def create_sub_class(self, class_name):
        setattr(self, class_name, Base(self.__session))
        return getattr(self, class_name)

    def type_to_python(type_string):
        if type_string == "integer": return int
        if type_string == "string": return str
        if type_string == "boolean": return bool
        if type_string == "list": return list

    def create_method(self, method_name, method_info):
        def method_wrapper(*args, **kwargs):
            data = {}
            for index, value in enumerate(args):
                try:
                    data[method_info['params'][index]['name']] = value
                except IndexError:
                    raise Exception('%s is invaild args' % (value))
            for key, value in kwargs.items():
                param_info = ([param for param in params if key == param['name']]+[None])[0]
                if param_info:
                    assert isinstance(self.type_to_python(param_info['type'])), '%s must be %s, not' % (param_info['name'], param_info['type'], type(value).__name__)
                    data[param_info['name']] = value
            for param in method_info['params']:
                if param['required'] and param['name'] not in data:
                    raise Exception('%s is required' % (param['name']))
            return self.request(method_info['method'], method_info['path'], data)
        return method_wrapper

class Vultr(Base):
    
    def __init__(self, API_KEY):
        self.__session = requests.session()
        self.__session.headers = {
            "API-Key": API_KEY,
        }
        super().__init__(self.__session)

        for method in build:
            full_name = method
            method_n_sub_class = method.split('.')
            on_sub_class = self
            while len(method_n_sub_class) != 1:
                sub_class_name = method_n_sub_class.pop(0)
                if not hasattr(on_sub_class, sub_class_name):
                    on_sub_class = on_sub_class.create_sub_class(sub_class_name)
            name = method_n_sub_class.pop(0)
            setattr(on_sub_class, name, on_sub_class.create_method(name, build[full_name]))
