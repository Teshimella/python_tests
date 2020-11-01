from requests import Session, exceptions
import sys


class Connector:

    def __init__(self, base_url, token):
        self.session = Session()
        self.base_url = base_url
        self.current_url = base_url
        self.headers: dict = {'Content-Type': 'application/json',
                              'Authorization': f'Basic {token}'
                              }

    def delete_headers(self, headers: dict):
        self.headers.pop(headers)

    def __send_query(self, method: str, path: str = None, body: dict = None, *args, **kwargs):
        try:
            url = f'{self.base_url}{path}'
            if path is None:
                url = self.current_url
            response = self.session.request(method, url=url, json=body, headers=self.headers)

            if not response.ok:
                print(f'response error: {response.text}')
            self.current_url = url
            return response
        except exceptions.ConnectionError as e:
            print(e, file=sys.stderr)
        except exceptions.Timeout as e:
            print(e, file=sys.stderr)
        except Exception as e:
            print(e, file=sys.stderr)


    def post(self, *args, **kwargs):
        respone = self.__send_query('POST', *args, **kwargs)
        return respone

    def put(self, *args, **kwargs):
        respone = self.__send_query('PUT', *args, **kwargs)
        return respone

    def get(self, *args, **kwargs):
        respone = self.__send_query('GET', *args, **kwargs)
        return respone

    def delete(self, *args, **kwargs):
        respone = self.__send_query('DELETE', *args, **kwargs)
        return respone

