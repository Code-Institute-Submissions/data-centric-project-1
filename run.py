import os
import re
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from random import randint




app = Flask(__name__)
app.secret_key = "some_secret"

app.config["MONGO_URI"] = "mongodb://admin:r00t_mdbtj@ds039261.mlab.com:39261/project-books-tj"
app.config["MONGODB_NAME"] = "project-books-tj"

mongo = PyMongo(app)

mongo.db.books.create_index(
        [
            ("title", "text"),
            ("author", "text"),
            ("genre", "text"),
            ("publisher", "text")
        ])


@app.route("/")
def index():
    
    """
    Homepage route 
    """
    
    # Books from DB
    _books = mongo.db.books.find()
    books = [book for book in _books]
    
    # Most viewed books
    most_viewed_books = mongo.db.books.find(
        { "$query": {},
            "$orderby": { "views" : -1 }}).limit(10)
            
    most_viewed = []
    
    for book in most_viewed_books:
        _book = {}
        _book["title"] = book["title"]
        _book["genre"] = book["genre"]
        _book["views"] = book["views"]
        
        most_viewed.append(_book)
        
    
    # Randomized featured book
    i = randint(0, (len(books) - 1)) 
    featured_book = books[i]
    
    # List of genres to filter by
    _genres = get_genres()
    
    
    return render_template("index.html",
                            books=books,
                            featured=featured_book,
                            most_viewed=most_viewed,
                            genres=_genres)


@app.route("/search_result")
def search_result():
    
    """
    Search Results for search term 
    """
    
    search_term = request.args.get("search_term")
    
    if search_term == "":
        flash("Search Something?")
    
    # Search Results
    search_result = mongo.db.books.find(
        { "$text":
            { "$search": search_term }
        })
    
    results = [result for result in search_result]
        
    # Number of results
    no_of_results = len(results)
    
    if no_of_results == 0 and search_term != "":
        flash("No Results Found!")
    
    # Genre list for filtering
    genres = get_genres()
    
    # Author list for filtering
    authors = get_authors()
    
    
    return render_template("search_results.html",
                            results=results,
                            search_term=search_term,
                            no_of_results=no_of_results,
                            genres=genres,
                            authors=authors)
                            

@app.route("/<search_term>/sort/<sort_by>")
def sorted_by(sort_by, search_term):
    
    """
    Search Results for search term, sorted by an option
    """
    
    if search_term == "":
        flash("Search Something?")
    
    search_result = mongo.db.books.aggregate(
        [
            { "$match":
                { "$text":
                    { "$search": search_term }
                }
            },
            { "$sort":
                { sort_by : -1 }
            }
        ])
            
    results = [result for result in search_result]
        
    # Number of results
    no_of_results = len(results)
            
    if no_of_results == 0 and search_term != "":
        flash("No Results Found!")
    
    # Genre list for filtering
    genres = get_genres()
    
    # Author list for filtering
    authors = get_authors()
    
    return render_template("search_results.html",
                            results=results,
                            search_term=search_term,
                            sort_by=sort_by,
                            no_of_results=no_of_results,
                            genres=genres,
                            authors=authors)
                            
                            
@app.route("/<search_term>/genre/<filter_by>")
def filter_by_genre(filter_by, search_term):
   
    """
    Search Results for search term, filtered by a genre
    """
    
    if search_term == "":
        flash("Search Something?")
    
    search_result = mongo.db.books.aggregate([
           { "$match": 
               { "$and": 
                   [ 
                       { "$text": 
                           { "$search": search_term }
                       }, 
                       { 
                           "genre": filter_by 
                       } 
                    ]
                }
            }
        ])
        
    results = [result for result in search_result]
        
    # Number of results
    no_of_results = len(results)
    
    if no_of_results == 0 and search_term != "":
        flash("No Results Found!")
    
    # Genre list for filtering
    genres = get_genres()
    
    # Author list for filtering
    authors = get_authors()
    
    return render_template("search_results.html",
                            results=results,
                            search_term=search_term,
                            filter_by=filter_by,
                            no_of_results=no_of_results,
                            genres=genres,
                            authors=authors)
                            
                            
@app.route("/<search_term>/genre/<filter_by>/<sort_by>")
def filtered_sort_by_genre(filter_by, sort_by, search_term):
    
    """
    Search Results for search term, filtered by a genre and sorted by an option
    """
    
    if search_term == "":
        flash("Search Something?")
    
    search_result = mongo.db.books.aggregate([
           { "$match": 
               { "$and": 
                   [ 
                       { "$text": 
                           { "$search": search_term }
                       }, 
                       { 
                           "genre": filter_by 
                       } 
                    ]
                }
            },
            { "$sort":
                { sort_by : -1 }
            }
        ])
        
    results = [result for result in search_result]
        
    # Number of results
    no_of_results = len(results)
            
    if no_of_results == 0 and search_term != "":
        flash("No Results Found!")
    
    # Genre list for filtering
    genres = get_genres()
    
    # Author list for filtering
    authors = get_authors()
    
    return render_template("search_results.html",
                            results=results,
                            search_term=search_term,
                            filter_by=filter_by,
                            sort_by=sort_by,
                            no_of_results=no_of_results,
                            genres=genres,
                            authors=authors)
                            
                            
@app.route("/<search_term>/author/<filter_by>")
def filter_by_author(filter_by, search_term):
    
    """
    Search Results for search term, filtered by a author
    """
    
    if search_term == "":
        flash("Search Something?")
    
    search_result = mongo.db.books.aggregate([
           { "$match": 
               { "$and": 
                   [ 
                       { "$text": 
                           { "$search": search_term }
                       }, 
                       { 
                           "author": filter_by 
                       } 
                    ]
                }
            }
        ])
        
    results = [result for result in search_result]
        
    # Number of results
    no_of_results = len(results)
    
    if no_of_results == 0 and search_term != "":
        flash("No Results Found!")
    
    # Genre list for filtering
    genres = get_genres()
    
    # Author list for filtering
    authors = get_authors()
    
    return render_template("search_results.html",
                            results=results,
                            search_term=search_term,
                            filter_by=filter_by,
                            no_of_results=no_of_results,
                            genres=genres,
                            authors=authors)
                            
                            
@app.route("/<search_term>/author/<filter_by>/<sort_by>")
def filtered_sort_by_author(filter_by, sort_by, search_term):
    
    """
    Search Results for search term, filtered by a author and sorted by an option
    """
    
    if search_term == "":
        flash("Search Something?")
    
    search_result = mongo.db.books.aggregate([
           { "$match": 
               { "$and": 
                   [ 
                       { "$text": 
                           { "$search": search_term }
                       }, 
                       { 
                           "author": filter_by 
                       } 
                    ]
                }
            },
            { "$sort":
                { sort_by : -1 }
            }
        ])
        
    results = [result for result in search_result]
        
    # Number of results
    no_of_results = len(results)
            
    if no_of_results == 0 and search_term != "":
        flash("No Results Found!")
    
    # Genre list for filtering
    genres = get_genres()
    
    # Author list for filtering
    authors = get_authors()
    
    return render_template("search_results.html",
                            results=results,
                            search_term=search_term,
                            filter_by=filter_by,
                            sort_by=sort_by,
                            no_of_results=no_of_results,
                            genres=genres,
                            authors=authors)
                            
                            
@app.route("/<search_term>/genre/<filter_by_1>/author/<filter_by_2>")
def filtered_filter_by(filter_by_1, filter_by_2, search_term):
   
    """
    Search Results for search term, filtered by a genre and author
    """
    
    if search_term == "":
        flash("Search Something?")
    
    search_result = mongo.db.books.aggregate([
           { "$match": 
               { "$and": 
                   [ 
                       { "$text": 
                           { "$search": search_term }
                       },
                       { 
                           "genre": filter_by_1 
                       },
                       { 
                           "author": filter_by_2 
                       } 
                    ]
                }
            }
        ])
        
    results = [result for result in search_result]
        
    # Number of results
    no_of_results = len(results)
                        
    if no_of_results == 0 and search_term != "":
        flash("No Results Found!")
    
    # Genre list for filtering
    genres = get_genres()
    
    # Author list for filtering
    authors = get_authors()
    
    return render_template("search_results.html",
                            results=results,
                            search_term=search_term,
                            filter_by_1=filter_by_1,
                            filter_by_2=filter_by_2,
                            no_of_results=no_of_results,
                            genres=genres,
                            authors=authors)
                            

@app.route("/<search_term>/genre/<filter_by_1>/author/<filter_by_2>/<sort_by>")
def filtered_filter_sort_by(filter_by_1, filter_by_2, sort_by, search_term):
    
    """
    Search Results for search term, 
    filtered by a genre and author, and sorted by an option 
    """
    
    if search_term == "":
        flash("Search Something?")
    
    search_result = mongo.db.books.aggregate([
           { "$match": 
               { "$and": 
                   [ 
                       { "$text": 
                           { "$search": search_term }
                       },
                       { 
                           "genre": filter_by_1 
                       },
                       { 
                           "author": filter_by_2 
                       } 
                    ]
                }
            },
            { "$sort":
                { sort_by : -1 }
            }
        ])
        
    results = [result for result in search_result]
        
    # Number of results
    no_of_results = len(results)
                                
    if no_of_results == 0 and search_term != "":
        flash("No Results Found!")
    
    # Genre list for filtering
    genres = get_genres()
    
    # Author list for filtering
    authors = get_authors()
    
    return render_template("search_results.html",
                            results=results,
                            search_term=search_term,
                            filter_by_1=filter_by_1,
                            filter_by_2=filter_by_2,
                            no_of_results=no_of_results,
                            genres=genres,
                            authors=authors)
                            
                            
                            

 ### Book CRUD Operations
 
@app.route("/book_record/<book_id>")
def book_record(book_id):
    
    # Displays the book record with Edit and Delete opertations
    
    book_record = find_book(book_id)
    
    # Get rating for book record
    avg_rating = book_record["avg_rating"]
    
    ratings = book_record["ratings"]
    
    # Get reviews for book record
    _reviews = book_record["reviews"]
    
    # Increase views
    _views = book_record["views"]
    new_views = _views + 1
    
    mongo.db.books.update({ "_id": ObjectId( book_id )},
    { "$set":
        {
            "views": new_views
        }
    })
    
    return render_template("book_record.html", 
                            book=book_record,
                            rating=avg_rating,
                            ratings=ratings,
                            reviews=_reviews)

@app.route("/update_reviews/<book_id>", methods=["GET", "POST"])
def update_reviews(book_id):
    
    # Update reviews and rating
    
    mongo.db.books.update({"_id": ObjectId(book_id)},
    { "$push":
        {
        "reviews": {
            "name": request.form["review.name"],
            "review": request.form["review.review"],
            "rating": int(request.form["rating"])},
        "ratings": int(request.form["rating"])
        }
    })
    
    book = find_book(book_id)
    
    # Gets the no of reviews for the book
    reviews = book["reviews"]
    no_of_reviews = len(reviews)
    
    mongo.db.books.update({ "_id": ObjectId( book_id )},
    { "$set":
        {
            "no_of_reviews": no_of_reviews
        }
    })
    
    # Gets the avg rating for the book 
    _ratings = book["ratings"]
    ratings = sum(_ratings)/len(_ratings)
    avg_rating = round(ratings, 1)
    
    mongo.db.books.update({ "_id": ObjectId( book_id )},
    { "$set":
        {
            "avg_rating": avg_rating
        }
    })
    
    return redirect(url_for("book_record", book_id=book_id))

@app.route("/add_book")
def add_book():
    
    # Go to add book
    return render_template("add_book.html") 
    
@app.route("/insert_book", methods = ["GET", "POST"])
def insert_book():

    # Insert new book record
    
    mongo.db.books.insert_one({
            "title": request.form["title"],
            "author": request.form["author"],
            "genre": request.form["genre"],
            "blurb": request.form["blurb"],
            "publisher": request.form["publisher"],
            "ISBN": request.form["ISBN"],
            "views": 0,
            "reviews": [],
            "no_of_reviews": 0,
            "ratings": [],
            "avg_rating": 0
        })
        
    last_book = find_last_inserted()
    
    return redirect(url_for("book_record", book_id=last_book._id))
    
@app.route("/edit_book/<book_id>")
def edit_book(book_id):
    
    # Go to edit book
    book_record = find_book(book_id)
    
    return render_template("edit_book.html", book=book_record)
    
@app.route("/update_book/<book_id>", methods = ["GET", "POST"])
def update_book(book_id):
    
    # Update book
    
    mongo.db.books.update(
        {"_id": ObjectId(book_id)},
        { "$set": 
            {
                "title": request.form["title"],
                "blurb": request.form["blurb"],
                "ISBN": request.form["ISBN"],
                "genre": request.form["genre"],
                "author": request.form["author"],
                "publisher": request.form["publisher"]
            }
        })
        
    return redirect(url_for("book_record", book_id=book_id))
        
@app.route("/delete_book/<book_id>")
def delete_book(book_id):
    
    mongo.db.books.remove({"_id": ObjectId(book_id)})
    
    return redirect(url_for("index"))

    
def find_all_books():
    
    _books = mongo.db.books.find()
    books = [book for book in _books]
    
    return books
    
def find_book(book_id):
    
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    
    return book
    
def find_last_inserted():
    
    last_book = mongo.db.books.find_one({ "$query": {}, "$orderby": { "_id" : -1 }})
    
    return last_book

def get_genres():
    
    _genres = mongo.db.books.find({}, { "genre": 1, "_id": 0 })
    genre_list = ["".join(genre["genre"]) for genre in _genres]
    
    genres = []
    for genre in genre_list:
        if genre not in genres:
            genres.append(genre)
    
    return genres
    
def get_authors():
    
    _authors = mongo.db.books.find({}, { "author": 1, "_id": 0 })
    author_list = ["".join(author["author"]) for author in _authors]
    
    authors = []
    for author in author_list:
        if author not in authors:
            authors.append(author)
    
    return authors
    
    
    
    ### Test CRUD Operations
    
def find_test_book(book_id):
    
    # Finding book in Test collection
    
    book = mongo.db.test.find_one({"_id": ObjectId(book_id)})
    
    return book
    
def find_last_test():
    
    # Find last inserted in test collection 
    
    last_book = mongo.db.test.find_one({ "$query": {}, "$orderby": { "_id" : -1 }}, { "_id": 0})
    
    return last_book
    
def insert_test_book():

    # Insert test book record
    
    mongo.db.test.insert_one({
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
        
def update_test_book(book_id):
    
    # Update test book  
    
    mongo.db.test.update(
        {"_id": ObjectId(book_id)},
        { "$set": 
            {
                "title": "Test Book 1",
                "blurb": "This is a test book, updated",
                "ISBN": "None"
            }
        })
    mongo.db.test.update(
        {"_id": ObjectId(book_id)},
        { "$addToSet":
            {
                "genre": "Test 1",
                "author": "No one",
                "publisher": "Me"
            }
        })
        
def update_test_reviews(book_id):
    
    # Update test reviews and rating
    
    mongo.db.test.update({"_id": ObjectId(book_id)},
    { "$push":
        {
            "reviews": {
                "name": "Me",
                "review": "This is a test"
            },
            "rating": 1
        }
    })
    

if __name__ == "__main__":
    app.run(host= os.environ.get("IP"),
    port= int(os.environ.get("PORT")),
    debug= True)