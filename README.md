# Data Centric Development Project - Books You'll Love

Books You'll Love is an Online library where you can add books you love to share
with others. You can search for books others have addded where they can be sorted
or filtered to help you find what you're looking for. When you have found what
you're looking for you can write a review or recommend it to a friend.

## UX

Books You'll Love is for people who love books and want to share them with others.
Users want to be able to share what they like or have written, so whether they are
part of a book club or a amateur author they can share what they are reading with
other users. 

This means the user can find, review and recommend the books they love to others.
With a full text search function the user can easily find what they are looking 
for, they can filter and sort the results to help them. The user can leave a 
review so they can tell others what they think and if they like the book they can
recommend it to other users.

As a User I would want:
- to be able to easily navigate website
- to be informed about the website
- to be able to search
    
As a User I would want:
- to easily understand and read the form
- to be clearly told where information goes
- to be informed that the record was added successfully or why it wasn't successful

As a User I would want:
- to be clearly shown the search results
- to be able to filter the results
- to be able to sort the results
- to be able to view results by page if many results returned
- to be able to click on a result to view more about it
- to be able to clear filters

As a User I would want:
- to be able to clearly view a record details
- to be able to edit or delete a record
- to be able to add to a user reading list

Mock ups can be viewed for each page below:
- [Index](/mock_ups/Index.jpg/)
- [Add Book](/mock_ups/Insert_Form.jpg/)
- [Book Record](/mock_ups/Record_Details.jpg/)
- [Search Results](/mock_ups/Search_results.jpg/)


## Features

### Existing Features

- CRUD Operations
    - Insert Book - allows users to add a book, by filling in add book form.
    - Find Book - allows users find books, by using the search bar.
    - Update Book - allows users to update books, by filling in edit book form.
    - Remove Book - allows users to delete books, by using the delete button.

- Full Text Search - allows users to search, by using a word or pharse. 
    - Search By Word
    - Filter By Option
    - Sort By Option

- Book Record - allows users to view books with the detail listed below, by using the "view book" button.
    - Rating
    - Average Rating
    - Reviews
    - Number Of Reviews
    - Views

- My Books - allows users to login to view books the have been recommended, by using the login on My Books page.
    - User Book list
    - Recommendations

- Most Viewed Chart - allows users to see what other users are viewing most.
    - Row Chart By View Count
    - Pie Chart By Genre Count

- Rating Chart - allows users to see how many of each rating a book has recieved.

### Planned Features

- Book Cover API

## Technology Used

- [Flask](http://flask.pocoo.org/)
    - **Flask** is a microframework for Python.
- [MongoDB](https://www.mongodb.com/)
    - **MongoDB** is a NoSQL Database which uses documents to store data.
- [Bootstrap](http://getbootstrap.com/)
    - **Bootstrap** is used to give a responsive layout.
- [JQuery](https://jquery.com)
    - **JQuery** is used to give better UX.

## Testing

I developed Books You'll Love using Test Driven Development approach to build the CRUD Operations then used manual test to check the UI. The testing was done using Python Unit Test Framework with a Test suite 
which can be found in [test_run.py](/tests/test_run.py/).

The tests can be run by using the following command:

    1. cd tests
    2. python3 test_run.py

I conducted manual tests through development to check each stage worked. I have documented these test here in [User Tests](/tests/user_tests.md/).
I have also tested my project for responsiveness and on different browsers which is detailed in [Browser Tests](/tests/browser_tests.pdf/)


