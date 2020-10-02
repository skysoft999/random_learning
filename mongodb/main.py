from pymongo import MongoClient
from mongoengine import *
import datetime


client = connect('mongoengine_test', host='localhost', port=27017)

# client = MongoClient("localhost", 27017)

# client = MongoClient("localhost", 27017)

# db = client.pymongo_test

# db = client["pymongo_test"]

# posts = db.posts

# post_1 = {
#     'title': 'Python and MongoDB',
#     'content': 'PyMongo is fun, you guys',
#     'author': 'Scott'
# }
# post_2 = {
#     'title': 'Virtual Environments',
#     'content': 'Use virtual environments, you guys',
#     'author': 'Scott'
# }
# post_3 = {
#     'title': 'Learning Python',
#     'content': 'Learn Python, it is easy',
#     'author': 'Bill'
# }




# new_data = posts.insert_many([post_1, post_2, post_3])

# print("Multiple Posts: {0}".format(new_data.inserted_ids))

# bills_post = posts.find_one({'author': 'Bill'})



class Author(Document):
    name = StringField()


class Post(Document):
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)
    # author = StringField(required=True, max_length=50)
    author = ReferenceField(Author)
    published = DateTimeField(default=datetime.datetime.now)

    @queryset_manager
    def live_posts(clazz, queryset):
        return queryset.filter(published=True)



import pdb;pdb.set_trace()

Auth = Author(name="Sanu ky")


Auth.save()

post_1 = Post(
    title='Sample Post',
    content='Some engaging content',
    author=Auth
)

# Post.objects.first().author.name

post_1.save()       # This will perform an insert
print(post_1.title)
post_1.title = 'A Better Post Title'
post_1.save()       # This will perform an atomic edit on "title"
print(post_1.title)



