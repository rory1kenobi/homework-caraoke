import unittest

from classes.song import Song
from classes.guest import Guest
from classes.room import Room


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("blue room", 15)
        self.room_2 = Room("green room", 15)
        self.guest_1 = Guest("Homer Simpson", 50)
        self.guest_2 = Guest("Bart Simpson", 20)
        self.song_1 = Song("artist_1", "title_1") 
        self.song_2 = Song("artist_2", "title_2") 

    def test_room_has_name(self):
        self.assertEqual("blue room", self.room_1.name)

    def test_guests_in_room(self):
        self.assertEqual(0, self.room_1.number_of_guests())
        self.assertEqual(0, self.room_2.number_of_guests())


    def test_number_of_song_on_song_list(self):
        self.assertEqual(0, self.room_1.number_of_songs())
        self.assertEqual(0, self.room_2.number_of_songs())

    def test_add_guest_to_list(self):
        self.room_1.add_guest_to_list(self.guest_1)
        self.room_2.add_guest_to_list(self.guest_2)
        self.assertEqual(1, self.room_1.number_of_guests())
        self.assertEqual(1, self.room_2.number_of_guests())

    def test_remove_guest_form_list(self):
        self.room_1.add_guest_to_list(self.guest_1)
        self.room_2.add_guest_to_list(self.guest_2)
        self.room_1.remove_guest_from_list(self.guest_1)
        self.room_2.remove_guest_from_list(self.guest_2)
        self.assertEqual(0, self.room_1.number_of_guests())
        self.assertEqual(0, self.room_2.number_of_guests())

    def test_add_song_to_song_list(self):
        self.room_1.add_song_to_song_list(self.song_1)
        self.room_2.add_song_to_song_list(self.song_1)
        self.assertEqual(1, self.room_1.number_of_songs())
        self.assertEqual(1, self.room_2.number_of_songs())

    def test_room_capacity(self):
        self.assertEqual(15, self.room_1.capacity)
        self.assertEqual(15, self.room_2.capacity)

  


        



    

    

    
