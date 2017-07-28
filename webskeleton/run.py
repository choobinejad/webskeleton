from webskeleton import GoogleMaps
from webskeleton import JsonPlaceHolder
import logging
from webskeleton import Config


# TODO Perhaps use a scheduler to manage when requests are executed.
# TODO Within each connection, incorporate appropriate means of concurrent execution.
config = Config(app_name='my_app_name', working_directory='')


connections = list()
# connections.append(GoogleMaps('/etc/my_config/google.key'))
connections.append(JsonPlaceHolder())

for cx in connections:
    data = cx.run()
    config.logger.info(data)
    # TODO Write your data to a file, message queue, or database.
