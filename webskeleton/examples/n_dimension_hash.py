from datetime import timedelta, datetime
from hashlib import sha256
from collections import Counter

now = datetime.now()

data = [
    dict(time=now - timedelta(seconds=12), location=4, username='abc'),
    dict(time=now - timedelta(seconds=847), location=4, username='abc'),
    dict(time=now - timedelta(seconds=3000), location=4, username='abcfdfsdfdsfs'),
    dict(time=now - timedelta(seconds=10000), location=4, username='abcdfsd'),
    dict(time=now - timedelta(seconds=0), location=1, username='abc'),
    dict(time=now - timedelta(seconds=3000), location=2, username='abc'),
    dict(time=now - timedelta(seconds=4), location=2)
]


def key_maker(dt, location, user):
    dt = dt.replace(microsecond=0, second=0, minute=0)
    time_location_user = dt.isoformat() + str(location) + str(user)
    print(dt, location, time_location_user)
    return sha256(time_location_user.encode()).hexdigest()


keys = []
for datum in data:
    key = key_maker(datum['time'], datum['location'], datum.get('username', ''))
    print(key)
    keys.append(key)

print('------------------------------')

c = Counter()
c.update(keys)
d = dict(c)
print(d)
