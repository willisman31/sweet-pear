import AMPM


class Alarm:

    on = False
    repeat = False
    name = "Alarm"

    def __init__(self, name: str, hour: int, minute: int, ampm: AMPM, repeat: bool):
        self.name = name
        self.hour = hour
        self.minute = minute
        self.ampm = ampm
        self.on = True
        self.repeat = repeat

    def __init__(self, hour: int, minute: int, ampm: AMPM):
        self.hour = hour
        self.minute = minute
        self.ampm = ampm
        self.on = True

    def __init__(self, hour: int, minute: int):
        self.hour = hour
        self.minute = minute
        self.on = True

    def __init__(self, name: str, hour: int, minute: int):
        self.name = name
        self.hour = hour
        self.minute = minute
        self.on = True

    def activate(self):
        self.on = True

    def deactivate(self):
        self.on = False

    def set(self, hour: int, minute: int, ampm: AMPM):
        self.hour = hour
        self.minute = minute
        self.ampm = ampm
        self.on = True

    def get_time(self):
        return self.hour + ":" + self.minute + " " + self.ampm

    def get_name(self):
        return self.name

    def get_repeat(self):
        return self.repeat
