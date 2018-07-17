from bson.objectid import ObjectId
import unittest
import run


class test_books(unittest.TestCase):
    
    # Test Suite
    
    def test_find_book(self):
        
        # Find book record by ID
        
        book = run.find_book("5b476e68207f2b2e30f64a0c")
        
        test_book = {
            "_id": ObjectId("5b476e68207f2b2e30f64a0c"),
            "title": "Test Book",
            "author": ["No one"],
            "genre": ["Test"],
            "blurb": "This is a test book",
            "publisher": ["Me"],
            "cover_image": "None",
            "views": 0,
            "reviews": [],
            "ratings": []
        }
        
        self.assertEqual(test_book, book)
        
    def test_update_book(self):
        
        # Update book record by ID
        
        run.update_book("5b4773af207f2b49fa5faa0e")
        book = run.find_book("5b4773af207f2b49fa5faa0e")
        
        test_book = {
            "_id": ObjectId("5b4773af207f2b49fa5faa0e"),
            "title": "Test Book 1",
            "author": ["No one"],
            "genre": ["Test"],
            "blurb": "This is a test book, updated",
            "publisher": ["Me"],
            "cover_image": "None",
            "views": 0,
            "reviews": [],
            "ratings": []
        }
        
        self.assertEqual(test_book, book)
        
    def test_get_genres(self):
        
        # Test get genre list
        
        _genres = run.get_genres()
        test_genre = ["Test"]
        
        self.assertIn(test_genre, _genres)
        
    def test_get_authors(self):
        
        # Test get author list 
        
        _authors = run.get_authors()
        test_author = ["No one"]
        
        self.assertIn(test_author, _authors)
        
    # def test_insert_book(self):
        
    #     # Test that the book inserted correctly
        
    #     run.insert_book()
        
    #     last_book = run.find_last_inserted()
        
    #     test_book = {
    #         "title": "Test Book 2",
    #         "author": ["Me"],
    #         "genre": ["Test 1"],
    #         "blurb": "This is a test book",
    #         "publisher": ["No one"],
    #         "cover_image": "None",
    #         "views": 0,
    #         "reviews": [],
    #         "ratings": []
    #     }
        
    #     self.assertEqual(test_book, last_book)
        
    # def test_update_reviews(self):
        
    #     # Test for updating reviews and rating by ID
        
    #     run.update_reviews("5b4e59be207f2b50a192f8e4")
    #     book = run.find_book("5b4e59be207f2b50a192f8e4")
        
    #     book_reivew = book["reviews"]
        
    #     test_review = {
    #             "name": "Me",
    #             "review": "This is a test"
    #             }
            
        
    #     self.assertIn(test_review, book_reivew)
        
    def search(self):
        
        results = run.search("Test")
        
        for result in results:
            print(result)
    
if __name__ == '__main__':
    unittest.main()