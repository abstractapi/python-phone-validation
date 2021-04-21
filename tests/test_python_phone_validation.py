import unittest
import os
from python_phone_validation import AbstractPhoneValidation

from dotenv import load_dotenv

load_dotenv()

PHONE_VAL_API_KEY = os.getenv('PHONE_VAL_API_KEY')

class TestAbstractPhoneValidation(unittest.TestCase):
    def __init__(self, *args, **kwargs):

        super(TestAbstractPhoneValidation, self).__init__(*args, **kwargs)

    def test_no_config(self):

        with self.assertRaises(Exception):
            # tests aren't always run in order, so make sure to
            # clear api_key
            AbstractPhoneValidation.api_key = None
            AbstractPhoneValidation.verify("14154582468")

    def test_config(self):

        AbstractPhoneValidation.configure(PHONE_VAL_API_KEY)
        AbstractPhoneValidation.verify("14154582468")


if __name__ == '__main__':
    unittest.main()