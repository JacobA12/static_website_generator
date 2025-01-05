from gencontent import *
import unittest


class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        md = "# Hello"
        expected = "Hello"

        self.assertEqual(extract_title(md), expected)

    def test_extract_title_exception(self):
        md = """This is not a tittle
      This is also not a title
      #Close but not a title"""
        with self.assertRaises(Exception) as context:
            extract_title(md)
        self.assertEqual(str(context.exception), "No Title Found")

    def test_extract_title_2(self):
        md = """This is not a title
#This is close to a title
# This is the title"""
        expected = "This is the title"
        self.assertEqual(extract_title(md), expected)
