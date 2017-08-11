from webskeleton import GoogleMaps
from webskeleton import JsonPlaceHolder
from webskeleton import Config
from datetime import datetime

startup = datetime.now().timestamp()

# TODO Perhaps use a scheduler to manage when requests are executed.
# TODO Within each connection, incorporate appropriate means of concurrent execution.
config = Config(app_name='my_app_name', working_directory='')


connections = list()
# TODO If you want to use the GoogleMaps object, you need to get a Google Maps API key!
# connections.append(GoogleMaps(config, '/etc/my_config/google.key'))
connections.append(JsonPlaceHolder(config))

for cx in connections:
    data = cx.run()
    config.logger.info(data)
    # TODO Write your data to a file, message queue, or database.

config.logger.info('Run duration: {} seconds.'.format(str(datetime.now().timestamp() - startup)))