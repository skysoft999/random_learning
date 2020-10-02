from pymongo import MongoClient

client = MongoClient("localhost", 27017)

# client = MongoClient("localhost", 27017)

db = client.pymongo_test

# db = client["pymongo_test"]

posts = db.posts

post_1 = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
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


# post_data = posts.insert_one(post_data)


new_data = posts.insert_many([post_1, post_2, post_3])

print("Multiple Posts: {0}".format(new_data.inserted_ids))