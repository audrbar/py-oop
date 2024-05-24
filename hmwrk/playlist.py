class Playlist:
    def __init__(self, songs: list):
        self.songs = songs

    def add_song(self, new_song):
        self.songs.append(new_song)
        print(f"The song '{new_song}' was successfully added to a list.")

    def remove_song(self, rm_song):
        self.songs.remove(rm_song)
        print(f"The song '{rm_song}' was successfully removed from a list.")

    def list_songs(self):
        print(f'Well... We have these songs in a list: {', '.join(self.songs)}.')


playlist_1 = Playlist(['Sun', 'Flower', 'Sky'])
playlist_1.list_songs()
playlist_1.remove_song('Sun')
playlist_1.add_song('Wind')
playlist_1.list_songs()
