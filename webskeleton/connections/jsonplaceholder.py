import requests
from webskeleton.connections.serializers import echo_serializer as serializer
import concurrent.futures


class JsonPlaceHolder(object):

    def __init__(self, config):
        self.session = requests.Session()
        # TODO add headers and authentication to self.session, as required by the service you're connecting to.
        self.get_posts_url = 'https://jsonplaceholder.typicode.com/posts'
        self.get_todos_url = 'https://jsonplaceholder.typicode.com/todos'
        self.get_users_url = 'https://jsonplaceholder.typicode.com/users'
        self.results = dict()
        self.config = config

    def get_posts(self):
        response = self.session.get(self.get_posts_url)
        self.results['posts'] = serializer(response)
        return True

    def get_todos(self):
        response = self.session.get(self.get_todos_url)
        self.results['todos'] = serializer(response)
        return True

    def get_users(self):
        response = self.session.get(self.get_users_url)
        self.results['users'] = serializer(response)
        return True

    def run(self):
        futures = list()
        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as e:
            futures.append(e.submit(self.get_posts))
            futures.append(e.submit(self.get_todos))
            futures.append(e.submit(self.get_users))
            for future in concurrent.futures.as_completed(futures, timeout=10):
                self.config.logger.info('finished a future')
        return self.results

    def run_linear(self):
        self.get_posts()
        self.get_todos()
        self.get_users()
        return self.results
