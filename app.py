from flask import Flask
from pymongo import MongoClient

'''
    This will be a test project using Flask, MongoDB, and maybe an maps and email api
    the goal of this app is to learn how to make a flask web and learn how to connect it to a database,
    then be able to deploy the web along with the database.
    
    As I said, the web will be really simple, it will do the next: 
    [X] It will only connect to a database
    [X] Do simple request to the database
    [X] Help me understand how flask work with mongo
    [X] Learn to use the maps and email correctly
    [X] Learn how to deploy the web and the database
'''
app = Flask(__name__)


# Configure mongo's connection
client = MongoClient('mongodb://localhost:27017')

# Select database
db = client.users

# Insert document to users
collection = db.users

# The structure of the data we'll be saving from the user
document = {
    'user': {
        "email": "Carlos@gmail.com",
        "name": "Carlitos"
    }
}
insert_document = collection.insert_one(document)
print(f'ID from the inserted document: {insert_document.inserted_id}')

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
