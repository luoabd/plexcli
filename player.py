import mpv

class Player():
    def __init__(self):
        self.player=mpv.MPV(input_default_bindings=True, input_vo_keyboard=True, osc=True)
    def play(self, url):
        self.player.play(url)
        self.player.wait_for_playback()
