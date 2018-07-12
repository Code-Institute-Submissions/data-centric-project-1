from bson.objectid import ObjectId
import unittest
import run


class test_books(unittest.TestCase):
    
    # Test Suite
    
   def test_find_book(self):
        
        book = run.find_book("5b476e68207f2b2e30f64a0c")
        
        test_book = {
            "_id": ObjectId("5b476e68207f2b2e30f64a0c"),
            "title": "Test Book",
            "author": "No one",
            "genre": "Test",
            "blurb": "This is a test book",
            "publisher": "Me",
            "cover_image": "None",
            "views": 0,
            "reviews": [],
            "ratings": []
        }
        
        self.assertEqual(test_book, book)
        
    def test_update_book(self):
        
        run.update_book("5b4773af207f2b49fa5faa0e")
        book = run.find_book("5b4773af207f2b49fa5faa0e")
        
        test_book = {
            "_id": ObjectId("5b4773af207f2b49fa5faa0e"),
            "title": "Test Book 1",
            "author": "No one",
            "genre": "Test",
            "blurb": "This is a test book, updated",
            "publisher": "Me",
            "cover_image": "None",
            "views": 0,
            "reviews": [],
            "ratings": []
        }
        
        self.assertEqual(test_book, book)
        
    
if __name__ == '__main__':
    unittest.main()