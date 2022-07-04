class Room:
    def __init__(self, _name, _capacity, _playlist, _guests, _entry):
        self.name = _name
        self.capacity = _capacity
        self.playlist = _playlist
        self.guests = _guests
        self.entry_fee = _entry

    def at_capacity(self):
        if len(self.guests) < self.capacity:
            return False
        else:
            return True

    def can_afford_entry(self, guest):
        if guest.wallet > self.entry_fee:
            return True
        else:
            return False

    def check_in(self, guest):
        if self.at_capacity() == True:
            return f"Sorry! This room is full!"
        elif self.can_afford_entry(guest) == False:
            return f"Sorry! {guest.name} can't afford the entry fee"
        else:
            guest.wallet -= self.entry_fee
            self.guests.append(guest)

    def check_out(self, guest):
        self.guests.remove(guest)
    
    def clear(self):
        self.guests = []
    
    def add_song(self, song):
        self.playlist.append({"title" : song.title, "artist" : song.artist})

    def find_guest_by_name(self, name):
        for guest in self.guests:
            if guest.name == name:
                return guest
        else:
            return "No guest by that name"

    def find_song_by_title(self, title):
        for song in self.playlist:
            if song["title"] == title:
                return song
