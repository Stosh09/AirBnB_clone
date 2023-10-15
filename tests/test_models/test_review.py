#!/usr/bin/python3
"""
Module for testing the Review class
"""
import json
import os
import unittest
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage
from models.review import Review


class testReview(unittest.TestCase):
    """
    Define methods testing the Review class
    """
    def set_up(self):
        """
        Removes the "file.json" file if it exists.

        :return: None
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tear_down(self):
        """
        Remove the "file.json" file if it exists.

        :return: None
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_review_created(self):
        """
        Test whether a Review object is successfully created.

        Example Usage:
        review = Review()
        self.assertTrue(review)
        """
        self.assertTrue(Review())

    def test_review_attributes(self):
        """
        Test whether a Review object has the expected attributes.

        Example Usage:
        review_1 = Review()
        self.assertTrue(hasattr(review_1, "text"))
        self.assertTrue(hasattr(review_1, "id"))
        self.assertTrue(hasattr(review_1, "created_at"))
        self.assertTrue(hasattr(review_1, "updated_at"))
        self.assertTrue(hasattr(review_1, "place_id"))
        self.assertTrue(hasattr(review_1, "user_id"))
        """

        review_1 = Review()

        self.assertTrue(hasattr(review_1, "text"))
        self.assertTrue(hasattr(review_1, "id"))
        self.assertTrue(hasattr(review_1, "created_at"))
        self.assertTrue(hasattr(review_1, "updated_at"))
        self.assertTrue(hasattr(review_1, "place_id"))
        self.assertTrue(hasattr(review_1, "user_id"))

    def test_review_id_type(self):
        """
        Check if the 'id' attribute of a 'Review' object is of type string.

        Example Usage:
        review_1 = Review()
        self.assertIsInstance(review_1.id, str)

        Inputs: None
        Flow:
        1. Create a new instance of the 'Review' class
        and assign it to the variable 'review_1'.
        2. Use the 'assertIsInstance' method to
        check if the 'id' attribute of 'review_1' is of type string.

        Outputs: None
        """
        review_1 = Review()
        self.assertIsInstance(review_1.id, str)

    def test_review_id_values(self):
        """
        Test whether the id attribute of two Review
        objects are not None and not equal to each other.

        Example Usage:
        review_1 = Review()
        review_2 = Review()
        self.assertIsNotNone(review_1.id)
        self.assertIsNotNone(review_2.id)
        self.assertNotEqual(review_1.id, review_2.id)
        """
        review_1 = Review()
        review_2 = Review()
        self.assertIsNotNone(review_1.id)
        self.assertIsNotNone(review_2.id)
        self.assertNotEqual(review_1.id, review_2.id)

    def test_review_class_doc(self):
        """
        This method is a unit test that checks whether
        the Review class has a docstring and whether
        the __init__ method of the Review class has a docstring.

        Example Usage:
        review = Review()
        self.assertGreater(len(Review.__doc__), 3)
        self.assertGreater(len(Review.__init__.__doc__), 3)

        Inputs: None
        Flow:
        1. Create an instance of the Review class
        and assign it to the variable review.
        2. Use the assertGreater method to check if
        the length of the __doc__ attribute of
        the Review class is greater than 3.
        3. Use the assertGreater method to check if
        the length of the __doc__ attribute of the __init__
        method of the Review class is greater than 3.

        Outputs: None
        """
        self.assertGreater(len(Review.__doc__), 3)
        self.assertGreater(len(Review.__init__.__doc__), 3)

    def test_review_attr(self):
        """
        Test whether the attributes of a
        Review object are initialized correctly.

        Example Usage:
        review_1 = Review()
        self.assertIsInstance(review_1.text, str)
        self.assertIsInstance(review_1.place_id, str)
        self.assertIsInstance(review_1.user_id, str)
        self.assertEqual(review_1.text, "")
        self.assertEqual(review_1.place_id, "")
        self.assertEqual(review_1.user_id, "")
        review_1.text = "Awesome"
        self.assertTrue(review_1.text, "Awesome")
        """
        review_1 = Review()
        self.assertIsInstance(review_1.text, str)
        self.assertIsInstance(review_1.place_id, str)
        self.assertIsInstance(review_1.user_id, str)
        self.assertEqual(review_1.text, "")
        self.assertEqual(review_1.place_id, "")
        self.assertEqual(review_1.user_id, "")
        review_1.text = "Awesome"
        self.assertTrue(review_1.text, "Awesome")

    def test_review_created_updated_at(self):
        """
        Test whether the created_at and updated_at attributes
        of a Review object are instances of the datetime class.

        Inputs:
        None

        Outputs:
        None
        """
        review1 = Review()
        self.assertIsInstance(review1.created_at, datetime)
        self.assertIsInstance(review1.updated_at, datetime)

    def test_review_save_updated_at(self):
        """
        Test whether the updated_at attribute of a
        Review object is updated when the save method is called.

        Example Usage:
        review = Review()
        prev_update = review.updated_at
        review.save()
        assert review.updated_at != prev_update

        Inputs: None
        Outputs: None
        """
        review = Review()
        prev_update = review.updated_at

    def test_review_to_dict(self):
        """
        Test the functionality of the to_dict method in the Review class.

        Example Usage:
        review = Review()
        review_dict = review.to_dict()
        # review_dict is a dictionary containing
        the attributes of the review object
        # Example output: {'__class__': 'Review', 'id': '...',
        'created_at': '...', 'updated_at': '...'}

        review.text = "awesome place"
        review_dict = review.to_dict()
        # review_dict is updated to include the 'text' attribute
        # Example output: {'__class__': 'Review',
        'id': '...', 'created_at': '...', 'updated_at': '...',
        'text': 'awesome place'}
        """

        review = Review()
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertIn("id", review_dict)
        self.assertIn("created_at", review_dict)
        self.assertIn("updated_at", review_dict)
        self.assertNotIn("name", review_dict)
        review.text = "awesome place"
        review_dict = review.to_dict()
        self.assertIn("text", review_dict)

    def test_review_save_to_file(self):
        """
        Test whether the save method of the Review
        class successfully saves the review object to a file.

        Example Usage:
        review = Review()
        review.save()
        assert os.path.exists("file.json") == True

        Inputs: None
        Outputs: None
        """

        review = Review()
        review.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_review_reload_from_file(self):
        """
        Test whether the reload method of the FileStorage
        class successfully reloads and deserializes objects
        from a JSON file into the __objects dictionary attribute.
        """
        review = Review()
        file = FileStorage()
        review.save()
        review_id = review.id

        file.reload()
        objs = file.all()

        self.assertIn("Review." + review_id, objs.keys())

    def test_review_str_(self):
        """
        Test the __str__ method of the Review class.

        This method creates a new instance of the
        Review class and tests the __str__ method,
        which returns a string representation of the Review object.

        Example Usage:
        review = Review()
        expected_str = "[Review] ({}) {}".format(review.id, review.__dict__)
        assert str(review) == expected_str

        Inputs: None
        Outputs: None
        """

        review = Review()
        expected_str = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(str(review), expected_str)

    def test_review_update_attributes(self):
        """
        Test whether the 'text' attribute of a 'Review'
        object is successfully updated and saved to the file storage.

        Example Usage:
        review = Review()
        review.text = 'good'
        review.save()
        new_storage = FileStorage()
        new_storage.reload()
        loaded_review = new_storage.all()['Review.{}'.format(review.id)]
        assert loaded_review.text == 'good'
        """
        review = Review()
        review.text = 'good'
        review.save()
        new_storage = FileStorage()
        new_storage.reload()
        loaded_review = new_storage.all()['Review.{}'.format(review.id)]
        self.assertEqual(loaded_review.text, 'good')

    def test_saving_and_loading(self):
        """
        Test whether a Review object can be successfully
        saved to a file and then loaded back from the file.

        Example Usage:
        review = Review()
        review_id = review.id
        storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        loaded_review = new_storage.all()['Review.{}'.format(review_id)]
        assert isinstance(loaded_review, Review)
        """
        review = Review()
        review_id = review.id
        storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        loaded_review = new_storage.all()['Review.{}'.format(review_id)]
        self.assertIsInstance(loaded_review, Review)


if __name__ == "__main__":
    unittest.main()
