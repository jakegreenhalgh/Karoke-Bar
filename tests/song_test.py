import unittest

from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.songsoftcell = Song("Tainted Love", "Soft Cell")
    
    def test_song_has_title(self):
        self.assertEqual("Tainted Love", self.songsoftcell.title)

    def test_song_has_artist(self):
        self.assertEqual("Soft Cell", self.songsoftcell.artist)
