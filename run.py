import os
import re
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from random import randint


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://admin:r00t_mdbtj@ds039261.mlab.com:39261/project-books-tj"
app.config["MONGODB_NAME"] = "project-books-tj"

mongo = PyMongo(app)


@app.route("/")
def index():
    
    # display homepage and content
    _books = mongo.db.books.find()
    books = [book for book in _books]
    
    # most viewed books to display
    most_viewed_books = mongo.db.books.find(
        { "$query": {},
            "$orderby": { "views" : -1 }}).limit(5)
            
    most_viewed = [book for book in most_viewed_books]
    
    # random featured book
    i = randint(0, (len(books) - 1)) 
    featured_book = books[i]
    featured = {
        "title": featured_book["title"],
        "author": ",".join(featured_book["author"]),
        "blurb": featured_book["blurb"],
        "ISBN": re.sub(r'[^\w.]', '', featured_book["ISBN"]) 
    }
    
    # list of genres to filter by
    _genres = get_genres()
    
    return render_template("index.html",
                            featured=featured,
                            most_viewed=most_viewed,
                            genres=_genres)


@app.route("/add_book")
def add_book():
    
    # go to add book form
    return render_template("add_book.html") 
    
@app.route("/insert_book", methods = ["POST"])
def insert_book():

    # Insert new book record
    
    mongo.db.books.insert_one({
            "title": request.form["title"],
            "author": [request.form["author"]],
            "genre": [request.form["genre"]],
            "blurb": request.form["blurb"],
            "publisher": [request.form["publisher"]],
            "ISBN": request.form["ISBN"],
            "views": 0,
            "reviews": [],
            "ratings": []
        })
    
    return redirect(url_for("add_book"))

    
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
    genre_list = [",".join(genre["genre"]) for genre in _genres]
    
    genres = []
    for genre in genre_list:
        if genre not in genres:
            genres.append(genre)
    
    return genres
    
def get_authors():
    
    _authors = mongo.db.books.find({}, { "author": 1, "_id": 0 })
    author_list = [",".join(author["author"]) for author in _authors]
    
    authors = []
    for author in author_list:
        if author not in authors:
            authors.append(author)
    
    return authors

    
def insert_test_book():

    # Insert test book record
    
    mongo.db.books.insert_one({
            "title": "Test Book 2",
            "author": ["Me"],
            "genre": ["Test 1"],
            "blurb": "This is a test book",
            "publisher": ["No one"],
            "ISBN": "None",
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
                "ISBN": "None"
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