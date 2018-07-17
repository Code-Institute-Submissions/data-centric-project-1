import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from mongodb import mongo_uri, mongodb_name

app = Flask(__name__)

app.config["MONGO_URI"] = mongo_uri()
app.config["MONGODB_NAME"] = mongodb_name()

mongo = PyMongo(app)


@app.route("/")
def index():
    
    return "Hello World"
    
def find_all_books():
    
    _books = mongo.db.books.find()
    books = [book for book in _books]
    
    return books
    
def search(search_for):
    
    mongo.db.books.createIndex({ "$**": "text" })
    search_results = mongo.db.books.find({ "$text": { "$search": search_for }})
    
    return search_results

def get_genres():
    
    _genres = mongo.db.books.find({}, { "genre": 1, "_id": 0 })
    genre_list = [genre for genre in _genres]
    
    genres = []
    for genre in genre_list:
        if genre["genre"] not in genres:
            genres.append(genre["genre"])
    
    return genres
    
def get_authors():
    
    _authors = mongo.db.books.find({}, { "author": 1, "_id": 0 })
    author_list = [author for author in _authors]
    
    authors = []
    for author in author_list:
        if author["author"] not in authors:
            authors.append(author["author"])
    
    return authors

    
def insert_book():

    # Insert new book record
    
    mongo.db.books.insert_one({
            "title": "Test Book 2",
            "author": ["Me"],
            "genre": ["Test 1"],
            "blurb": "This is a test book",
            "publisher": ["No one"],
            "cover_image": "None",
            "views": 0,
            "reviews": [],
            "ratings": []
        })

def find_book(book_id):
    
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    
    return book
    
def find_last_inserted():
    
    last_book = mongo.db.books.find_one({ "$query": {}, "$orderby": { "_id" : -1 }}, { "_id": 0})
    
    return last_book
    
def update_book(book_id):
    
    # Update book
    
    mongo.db.books.update(
        {"_id": ObjectId(book_id)},
        { "$set": 
            {
                "title": "Test Book 1",
                "blurb": "This is a test book, updated",
                "cover_image": "None"
            }
        })
    mongo.db.books.update(
        {"_id": ObjectId(book_id)},
        { "$addToSet":
            {
                "genre": "Test",
                "author": "No one",
                "publisher": "Me"
            }
        })
        
def update_reviews(book_id):
    
    # Update reviews and rating
    
    mongo.db.books.update({"_id": ObjectId(book_id)},
    { "$push":
        {
            "reviews": {
                "name": "Me",
                "review": "This is a test"
            },
            "rating": 1
        }
    })
    
def delete_book(book_id):
    
    mongo.db.books.remove({"_id": ObjectId(book_id)})


if __name__ == "__main__":
    app.run(host= os.environ.get("IP"),
    port= int(os.environ.get("PORT")),
    debug= True)