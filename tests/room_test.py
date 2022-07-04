import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.jim = Guest("Jim", 10)
        self.bob = Guest("Bob", 15)
        self.mary = Guest("Mary", 13)
        self.liz = Guest("Liz", 40)
        self.ann = Guest("Ann", 30)
        self.john = Guest("John", 4)

        self.songsoftcell = Song("Tainted Love", "Soft Cell")
        self.songfrankie = Song("Relax", "Frankie Goes to Hollywood")

        self.room = Room("Eighties Room", 4, [{"title" : "Tainted Love", "artist" : "Soft Cell"}], [self.jim, self.bob, self.mary], 10)

    def test_room_has_name(self):
        self.assertEqual("Eighties Room", self.room.name)

    def test_room_has_capacity(self):
        self.assertEqual(4, self.room.capacity)

    def test_can_check_in(self):
        self.room.check_in(self.liz)
        self.assertEqual(4, len(self.room.guests))

    def test_cant_afford(self):
        self.assertEqual("Sorry! John can't afford the entry fee", self.room.check_in(self.john))
    
    def test_at_capacity(self):
        self.room.check_in(self.liz)
        self.assertEqual("Sorry! This room is full!", self.room.check_in(self.ann))

    def test_find_guest_by_name(self):
        self.assertEqual(self.jim, self.room.find_guest_by_name("Jim"))

    def test_can_check_out(self):
        self.room.check_out(self.jim)
        self.assertEqual("No guest by that name", self.room.find_guest_by_name("Jim"))

    def test_can_clear_room(self):
        self.room.clear()
        self.assertEqual(0, len(self.room.guests))

    def test_can_find_song_by_title(self):
        self.assertEqual({"title" : "Tainted Love", "artist" : "Soft Cell"}, self.room.find_song_by_title("Tainted Love"))

    def test_can_add_song(self):
        self.room.add_song(self.songfrankie)
        self.assertEqual({"title" : "Relax", "artist" : "Frankie Goes to Hollywood"}, self.room.find_song_by_title("Relax"))