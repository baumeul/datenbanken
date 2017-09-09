from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client.fullstack

# Inserting 1 Document

posts = db.posts
post_data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott',
}
result = posts.insert_one(post_data)
print('One post: {0}'.format(result.inserted_id))

# Inserting Documents

post_2 = {
    'title': 'Virtual Environments',
    'content': 'Use virtual environments, you guys',
    'author': 'Scott'
}
post_3 = {
    'title': 'Learning Python',
    'content': 'Learn Python, it is easy',
    'author': 'Bill'
}
new_result = posts.insert_many([post_2, post_3])
print('Multiple posts: {0}'.format(new_result.inserted_ids))

# Retrieving Documents

bills_post = posts.find_one({'author': 'Bill'})
print(bills_post)

scotts_post = posts.find({'author': 'Scott'})
for post in scotts_post:
    print(post)

