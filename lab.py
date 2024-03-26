class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.status = False
        self.muted = False
        self.volume = self.MIN_VOLUME
        self.channel = self.MIN_CHANNEL

    def power(self):
        if self.status:
            self.status = False

        elif not self.status:
            self.status = True

    def mute(self):
        if not self.muted:
            self.muted = True

        else:
            self.muted = False

    def channel_up(self):
        if self.status:
            if self.channel == self.MAX_CHANNEL:
                self.channel = self.MIN_CHANNEL

            else:
                self.channel += 1

    def channel_down(self):
        if self.status:
            if self.channel == self.MIN_CHANNEL:
                self.channel = self.MAX_CHANNEL

            else:
                self.channel -= 1

    def volume_up(self):
        if self.status:
            if self.volume != self.MAX_VOLUME:
                self.volume += 1

    def volume_down(self):
        if self.status:
            if self.volume != self.MIN_VOLUME:
                self.volume -= 1

    def __str__(self):
        if self.muted:
            return f'TV status: Power = ' + str(self.status) + ', Channel = ' + str(self.channel) + ', Volume = ' + str(
                self.MIN_VOLUME)

        else:
            return f'TV status: Power = ' + str(self.status) + ', Channel = ' + str(self.channel) + ', Volume = ' + str(
                self.volume)
