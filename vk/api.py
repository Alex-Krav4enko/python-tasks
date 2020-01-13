from urllib.parse import urlencode
import requests


class User:
    VK_URL = 'https://vk.com/id'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']

    def __repr__(self):
        return self.VK_URL + str(self.id)


class VK:
    OAUTH_URL = 'https://oauth.vk.com/authorize'
    OAUTH_PARAMS = {
        'client_id': 7280871,
        'display': 'page',
        'response_type': 'token',
        'scope': 'friends'
    }
    ACCESS_TOKEN = '123'
    VERSION = 5.103
    API_URL = 'https://api.vk.com/method/'
    API = {
        'get_user': API_URL + 'users.get',
        'common_friends': API_URL + 'friends.getMutual'
    }
    PARAMS = {
        'access_token': ACCESS_TOKEN,
        'v': VERSION
    }

    def get_oauth_request(self):
        return '?'.join((self.OAUTH_URL, urlencode(self.OAUTH_PARAMS)))

    def get_user(self, user_id):
        params = self.PARAMS.copy()
        params['user_ids'] = user_id
        user = requests.get(self.API['get_user'], params)
        return User(user.json()['response'][0])

    def get_common_friends(self, source_uid, target_uid):
        friends = []
        params = self.PARAMS.copy()
        params['source_uid'] = source_uid
        params['target_uid'] = target_uid
        res = requests.get(self.API['common_friends'], params)
        for _id in res.json()['response']:
            friends.append(self.get_user(_id))
        return friends


vk = VK()
common_friends = vk.get_common_friends(123, 123)
print(common_friends)
