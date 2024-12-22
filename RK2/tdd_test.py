import unittest
from main_test import (
    task1,
    task2,
    task3,
    libraries
)

class TestCDLibrary(unittest.TestCase):
    def setUp(self):
        self.one_to_many = [
            ("The Silence of the Lambs", 512, "Thriller"),
            ("Men in Black", 1024, "Comedy"),
            ("Home Alone", 256, "Comedy"),
            ("Avatar", 2048, "Fiction"),
            ("Interstellar", 4096, "Fiction")
        ]
        
        self.many_to_many = [
            ("The Silence of the Lambs", 512, "Thriller"),
            ("Men in Black", 1024, "Comedy"),
            ("Home Alone", 256, "Comedy"),
            ("Avatar", 2048, "Fiction"),
            ("Interstellar", 4096, "Fiction"),
            ("Avatar", 2048, "Drama")
        ]

    def test_task1(self):
        result = task1(self.one_to_many)
        expected = [
            ("Men in Black", 1024, "Comedy"),
            ("Home Alone", 256, "Comedy")
        ]
        self.assertEqual(result, expected)

    def test_task2(self):
        result = task2(self.one_to_many, libraries)
        expected = [
            ("Fiction", 4096),
            ("Comedy", 1024),
            ("Thriller", 512)
        ]
        self.assertEqual(result, expected)

    def test_task3(self):
        result = task3(self.many_to_many, libraries)
        expected = {
            "Thriller": ["The Silence of the Lambs"],
            "Comedy": ["Men in Black", "Home Alone"],
            "Fiction": ["Avatar", "Interstellar"],
            "Drama": ["Avatar"]
        }

        if result != expected:
            print("\nResult:", result)
            print("\nExpected:", expected)

        self.assertDictEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
