class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capasity = capacity 
        self.songs_list = []
        self.guest_list = []

    
    def number_of_guests(self):
        return len(self.guest_list)

    def number_of_songs(self):
        return len(self.songs_list)

    def add_guest_to_list(self, guest):
        self.guest_list.append(guest)

    def remove_guest_from_list(self, guest):
        self.guest_list.remove(guest)

    def add_song_to_song_list(self, song):
        self.songs_list.append(song)