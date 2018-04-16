import unittest
from homework3 import create_dataframe

class test_hw3(unittest.TestCase):

    # Each method in the class to execute a test
    def test_smoke(self):
        create_dataframe('class.db')

    def test_check_colnames(self):
        self.assertEqual(list(create_dataframe("class.db")),["video_id","category_id","language"])

    def test_nrows(self):
        self.assertTrue(len(create_dataframe('class.db').index) >= 10)

    def test_key(self):
        self.assertTrue(len(create_dataframe('class.db').index) == len(create_dataframe('class.db').groupby(["video_id","language"])))

    #test to check that the correct exception is generated when an invalid path is provided.
    def test_exception(self):
        self.assertRaises(ValueError, create_dataframe, 'class.db')


if __name__=='__main__':
	unittest.main()

