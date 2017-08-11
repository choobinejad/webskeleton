import requests
from requests.exceptions import ConnectionError

t = requests.Session()
# t.cert = ('/path/to/cert.pem', '/path/to/key.pem')
# t.verify = '/path/to/trust.pem'
#openSSl convert pks12 to pem

get_posts_url = 'https://jsonplaceholder.typicode.com/posts'
bad_posts_url = 'https://jsonfdsfsplaceholder.typicode.com/poshfdjkfndsktsdnjsdn'

try:
    result = t.get(bad_posts_url)
except ConnectionError:
    result = t.get(get_posts_url)

print("Status: {}".format(str(result.status_code)))
print("Data: ", result.json())






posts = result.json()

# Who are the authors of the posts?

# Use list comprehension!
authors = [post['userId'] for post in posts]
print('List comprehension: ', authors)

# alternate list comprehension
authors = []
for post in posts:
    authors.append(post['userId'])

# Result will be the last value of 'userId'
# authors = []
# for post in posts:
#     authors = post['userId']


# Use set comprehension
authors = set(post['userId'] for post in posts)
print('Set comprehension: ', authors)


# Compare our authors to another set of authors
other_authors = {1, 2, 7, 14, 9, 10}
print('Union: ', authors.union(other_authors))
print('Unique authors: ', authors - other_authors)
print('Unique other authors: ', other_authors - authors)
print('Joint authors: ', authors.intersection(other_authors))


# Filter the posts collection using the builtin filter() function
def keyword_title_filter(text):
    if 'ut' in text['title']:
        return True
    return False

# Use filter() as a generator
filtered_posts = []
for post in filter(keyword_title_filter, posts):
    filtered_posts.append(post)
print('Filtered posts: ', filtered_posts)

# User filter() in a list comprehension
filtered_posts = [i for i in filter(keyword_title_filter, posts)]
print('Filtered posts: ', filtered_posts)
