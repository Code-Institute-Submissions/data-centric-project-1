from bson.objectid import ObjectId
import unittest
import run


class test_books(unittest.TestCase):
    """
    Test Suite
    """
    def test_find_book(self):
        """
        Find book record by ID
        """
        book = run.find_test_book("5b55febe207f2b4319b8c010")
        
        test_book = {
            "_id": ObjectId("5b55febe207f2b4319b8c010"),
            "title": "Test Book",
            "author": ["No one"],
            "genre": ["Test"],
            "blurb": "This is a test book",
            "publisher": ["Me"],
            "ISBN": "None",
            "views": 0,
            "reviews": [],
            "ratings": []
        }
        
        self.assertEqual(test_book, book)
        
    def test_update_book(self):
        """
        Update book record by ID
        """
        run.update_test_book("5b56efbe207f2b5a522cd07d")
        book = run.find_test_book("5b56efbe207f2b5a522cd07d")
        
        test_book = {
            "_id": ObjectId("5b56efbe207f2b5a522cd07d"),
            "title": "Test Book 1",
            "author": ["Me", "No one"],
            "genre": ["Test 1"],
            "blurb": "This is a test book, updated",
            "publisher": ["No one", "Me"],
            "ISBN": "None",
            "views": 0,
            "reviews": [],
            "ratings": []
        }
        
        
        self.assertEqual(test_book, book)
        
    def test_get_genres(self):
        """
        Test get genre list
        """
        _genres = run.get_genres()
        test_genre = "History"
        
        self.assertIn(test_genre, _genres)
        
    def test_get_authors(self):
        """
        Test get author list 
        """
        _authors = run.get_authors()
        test_author = "Robyn Young"
        
        self.assertIn(test_author, _authors)
        
    def test_insert_book(self):
        """
        Test that the book inserted correctly
        """
        run.insert_test_book()
        
        last_book = run.find_last_test()
        
        test_book = {
            "title": "Test Book 2",
            "author": ["Me"],
            "genre": ["Test 1"],
            "blurb": "This is a test book",
            "publisher": ["No one"],
            "ISBN": "None",
            "views": 0,
            "reviews": [],
            "ratings": []
        }
        
        self.assertEqual(test_book, last_book)
        
    def test_update_reviews(self):
        """
        Test for updating reviews and rating by ID
        """
        run.update_test_reviews("5b55ff10207f2b4522d99830")
        book = run.find_test_book("5b55ff10207f2b4522d99830")
        
        book_reivew = book["reviews"]
        
        test_review = {
                "name": "Me",
                "review": "This is a test"
                }
        
        self.assertIn(test_review, book_reivew)
        
    def test_text_search(self):
        """
        Test to check text search returns correct results
        """
        books = run.text_search_test("Book 1")
        
        test_book = {
            "_id": ObjectId("5b56efbe207f2b5a522cd07d"),
            "title": "Test Book 1",
            "author": ["Me", "No one"],
            "genre": ["Test 1"],
            "blurb": "This is a test book, updated",
            "publisher": ["No one", "Me"],
            "ISBN": "None",
            "views": 0,
            "reviews": [],
            "ratings": []
        }
        
        self.assertIn(test_book, books)
        
if __name__ == '__main__':
    unittest.main()