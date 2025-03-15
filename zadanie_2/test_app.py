import unittest

import app

class TestIsPallindrome(unittest.TestCase):
    def test_number(self):
        with self.assertRaises(TypeError):
            app.is_pallindrome(6)

    def test_even_word(self):
        self.assertTrue(app.is_pallindrome("noon"), True)

    def test_odd_word(self):
        self.assertTrue(app.is_pallindrome("kayak"), True)

    def test_upper_case(self):
        self.assertTrue(app.is_pallindrome("KaKak"), True)


class TestRectArea(unittest.TestCase):
    def test_string(self):
        with self.assertRaises(TypeError):
            app.rect_area("2",4)

    def test_positive(self):
        self.assertEqual(app.rect_area(2,4), 8)

    def test_negative(self):
        with self.assertRaises(ValueError):
            app.rect_area(-2,4)

    def test_zero(self):
        with self.assertRaises(ValueError):
            app.rect_area(2,0)



class TestIsPasswordValid(unittest.TestCase):
    def test_number(self):
        with self.assertRaises(TypeError):
            app.is_password_valid(6)
    def test_length(self):
        self.assertFalse(app.is_password_valid("Pa$$wor"))

    def test_uppercase(self):
        self.assertFalse(app.is_password_valid("pa$$word"))

    def test_special_char(self):
        self.assertFalse(app.is_password_valid("Password"))

    def test_whitespace(self):
        self.assertFalse(app.is_password_valid("Pass word"))

    def test_valid(self):
        self.assertTrue(app.is_password_valid("Pa$$word"))


class TestReplaceChar(unittest.TestCase):
    def test_no_char_to_replace(self):
        self.assertEqual(app.replace_char("test", "q", "k"), "test")

    def test_expected(self):
        self.assertEqual(app.replace_char("pesp", "p", "t"), "test")

    def test_uppercase(self):
        self.assertEqual(app.replace_char("test", "T", "a"), "test")

    def test_invalid_format(self):
        with self.assertRaises(ValueError):
            app.replace_char("test", "te", "a")

    def test_number(self):
        with self.assertRaises(TypeError):
            app.replace_char("test", 7, "a")


class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(app.greet("Mark"), "Hello, Mark")

    def test_number(self):
        with self.assertRaises(TypeError):
            app.greet(6)

if __name__ == "__main__":
    unittest.main()
