import requests
from datetime import datetime

startup = datetime.utcnow()
print('App startup: {}. Date: {}. Time: {}. ISO Format: {}. Epoch: {}'.format(
    str(startup),
    str(startup.date()),
    str(startup.time()),
    startup.isoformat(),
    str(startup.timestamp())
))

# Get your zoo from an API
certfile = '/path/to/my/cert/file.pem' # You PKI certificate signed by a CA
keyfile = '/path/to/my/key/file.pem' # Your PKI private key
zoo_api = requests.Session() # Sessions are ways to persist settings, like your certs
zoo_api.cert = (certfile, keyfile) # This will add your already defined client certs to the Session
zoo_api.verify = '/path/to/trust/store.pem' # Your truststore (which remote hosts do you trust?)

zoo = zoo_api.get('https://zoo-server.com/my-zoo?q=category:mammal')
print('Zoo api status code: ', zoo.status_code)
# Do any quality checks needed on your zoo
# Perhaps make a "verify_zoo()" function
zoo = zoo.json()

# Supply your own zoo
zoo = {
    'blake:dog:': {'name': 'blake', 'species': '8472'},
    'amelia:cat:': {'name': 'amelia', 'species': 'borg'}
}

# Filter your zoo
good_animals = ['dog', 'cat']
good_zoo = [v['name'] for k, v in zoo.items() if k.split(':')[1][:-1] in good_animals]
