#!/usr/bin/python3
""" Unittest for Place """
import unittest
import models
from models.place import Place
from models.base_model import BaseModel
from datetime import datetime


class TestUser(unittest.TestCase):
    """ Test """

    def test_user(self):
        """ Test """
        place = Place()
        self.assertEqual(str, type(place.user_id))
        self.assertEqual(str, type(place.name))
        self.assertEqual(int, type(place.price_by_night))
        self.assertEqual(list, type(place.amenity_ids))
        self.assertEqual(str, type(place.city_id))
        self.assertEqual(int, type(place.number_rooms))
        self.assertEqual(int, type(place.number_bathrooms))
        self.assertEqual(int, type(place.max_guest))
        self.assertEqual(float, type(place.latitude))
        self.assertEqual(float, type(place.longitude))


if __name__ == '__main__':
    unittest.main()
