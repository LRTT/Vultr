import requests
import json
import time

BUILD = json.load(open("vultr.build.info.json", "r"))

class VultrError(RuntimeError):
    """ Vultr Exception """

class Base(object):
    # Ref https://raw.githubusercontent.com/spry-group/python-vultr/32b5d19b1b45db9ef96f0ddf4439df7a0acbd652/vultr/utils.py

    BASE_HOST = "https://api.vultr.com"
    REQ_PER_SECOND = 1

    def __init__(self, session):
        self.__session = session
        # set the request/second at run-time
        self.req_duration = 1 / self.REQ_PER_SECOND

    def request(self, method, path, data):
        """ API request / call method """
        _start = time.time()
        
        if not path.startswith("/"): path = "/" + path
        
        resp = getattr(self.__session, method)(self.BASE_HOST + path, data=data)
        
        if resp.status_code != 200:
            if resp.status_code == 400:
                raise VultrError('Invalid API location. Check the URL that you are using')
            elif resp.status_code == 403:
                raise VultrError('Invalid or missing API key. Check that your API key is present and matches your assigned key')
            elif resp.status_code == 405:
                raise VultrError('Invalid HTTP method. Check that the method (POST|GET) matches what the documentation indicates')
            elif resp.status_code == 412:
                raise VultrError('Request failed. Check the response body for a more detailed description. Body: \n' + resp.text)
            elif resp.status_code == 500:
                raise VultrError('Internal server error. Try again at a later time')
            elif resp.status_code == 503:
                raise VultrError('Rate limit hit. API requests are limited to an average of 1/s. Try your request again later.')
            else:
                raise VultrError(resp.text)

        _elapsed = time.time() - _start
        if _elapsed < self.req_duration:
            time.sleep(self.req_duration - _elapsed)

        return resp.json() if resp.text else {}

    def create_sub_class(self, class_name):
        if not hasattr(self, class_name):
            sub_class_base = Base(self.__session)
            sub_class_base.__name__ = class_name
            setattr(self, class_name, sub_class_base)
        return getattr(self, class_name)

    def create_or_get_sub_class(self, class_name):
        return getattr(self, class_name, self.create_sub_class(class_name))

    def type_to_python(self, type_string):
        if type_string == "integer": return int
        if type_string == "string": return str
        if type_string == "boolean": return bool
        if type_string == "list": return list

    def create_method(self, method_info):
        def method_wrapper(*args, **kwargs):
            data = {}
            for index, value in enumerate(args):
                try:
                    data[method_info['params'][index]['name']] = value
                except IndexError:
                    raise Exception('%s is invaild args' % (value))
            for key, value in kwargs.items():
                param_info = ([param for param in method_info['params'] if key == param['name']]+[None])[0]
                if param_info:
                    assert isinstance(value, self.type_to_python(param_info['type'])), '%s must be %s, not %s' % (param_info['name'], param_info['type'], type(value).__name__)
                    data[param_info['name']] = value
            for param in method_info['params']:
                if param['required'] and param['name'] not in data:
                    raise Exception('%s is required' % (param['name']))
            return self.request(method_info['method'], method_info['path'], data)
        return method_wrapper

class Vultr(Base):
    __name__ = 'Vultr'
    
    def __init__(self, API_KEY):
        self.__session = requests.session()
        self.__session.headers = {
            "API-Key": API_KEY,
        }
        super().__init__(self.__session)

        for method in BUILD:
            full_method_name = method
            subclass_n_method_loc = method.split('.')
            s_ = method.split('.')
            on_sub_class = self
            while len(subclass_n_method_loc) != 1:
                name = subclass_n_method_loc.pop(0)
                on_sub_class = on_sub_class.create_or_get_sub_class(name)
            name = subclass_n_method_loc.pop(0)
            setattr(on_sub_class, name, on_sub_class.create_method(BUILD[full_method_name]))
