import unittest
from classes.song import Song
from classes.room import Room
from classes.guest import Guest

class TestSong(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("blue room", 15)
        self.room_2 = Room("green room", 15)
        self.guest_1 = Guest("Homer Simpson", 50)
        self.guest_2 = Guest("Bart Simpson", 20)
        self.song_1 = Song("artist_1", "title_1") 
        self.song_2 = Song("artist_2", "title_2") 

    def test_song_has_artist(self):
        self.assertEqual("artist_1", self.song_1.artist)

    def test_song_has_title(self):
        self.assertEqual("title_1", self.song_1.title)
