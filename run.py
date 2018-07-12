import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from mongodb import mongo_uri, mongodb_name

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://admin:r00t-DBTJ@ds039261.mlab.com:39261/project-books-tj"
app.config["MONGODB_NAME"] = "project-books-tj"

mongo = PyMongo(app)


@app.route("/")
def index():
    
    return "Hello World"
    
def insert_book():

    # Insert new book record
    
    mongo.db.books.insert_one({
            "title": "Test Book",
            "author": "No one",
            "genre": "Test",
            "blurb": "This is a test book",
            "publisher": "Me",
            "cover_image": "None",
            "views": 0,
            "reviews": [],
            "ratings": []
        })

def find_book(book_id):
    
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    
    return book
    
def update_book(book_id):
    
    # Update book
    
    mongo.db.books.update({"_id": ObjectId(book_id)},{ "$set": 
        {
            "title": "Test Book 1",
            "author": "No one",
            "genre": "Test",
            "blurb": "This is a test book, updated",
            "publisher": "Me",
            "cover_image": "None"
        }
    })


if __name__ == "__main__":
    app.run(host= os.environ.get("IP"),
    port= int(os.environ.get("PORT")),
    debug= True)