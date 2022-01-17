import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("blue room", 15)
        self.room_2 = Room("green room", 15)
        self.guest_1 = Guest("Homer Simpson", 50)
        self.guest_2 = Guest("Bart Simpson", 20)
        self.song_1 = Song("artist_1", "title_1") 
        self.song_2 = Song("artist_2", "title_2") 

    def test_guest_has_name(self):
        self.assertEqual("Homer Simpson", self.guest_1.name)

    def test_guest_has_money(self):
        self.assertEqual(50, self.guest_1.wallet)
