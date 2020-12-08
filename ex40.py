class song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = song (["Happy Birthdat to you", " I don't want to get sued", "so i will stop right there!"])            

bullds_on_prade = song (["They rally around tha family","With pockets full of shells"])

happy_bday.sing_me_a_song()
bullds_on_prade.sing_me_a_song()
