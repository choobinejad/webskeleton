import requests
from webskeleton.connections.serializers import echo_serializer as serializer


class JsonPlaceHolder(object):

    def __init__(self):
        self.session = requests.Session()
        # TODO add headers and authentication to self.session, as required by the service you're connecting to.
        self.get_posts_url = 'https://jsonplaceholder.typicode.com/posts'
        self.get_todos_url = 'https://jsonplaceholder.typicode.com/todos'
        self.get_users_url = 'https://jsonplaceholder.typicode.com/users'

    def get_posts(self):
        return self.session.get(self.get_posts_url)

    def get_todos(self):
        return self.session.get(self.get_todos_url)

    def get_users(self):
        return self.session.get(self.get_users_url)

    def run(self):
        results = dict()
        results['posts'] = self.get_posts()
        results['todos'] = self.get_todos()
        results['users'] = self.get_users()
        return serializer(results)