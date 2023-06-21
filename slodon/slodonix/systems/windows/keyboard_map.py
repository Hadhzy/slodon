# https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes

__all__ = ["key_map"]

keyboard_mapping = [
    ("backspace", 0x08),
    ("\b", 0x08),
    ("super", 0x5B),
    ("tab", 0x09),
    ("\t", 0x09),
    ("clear", 0x0C),
    ("enter", 0x0D),
    ("\n", 0x0D),
    ("return", 0x0D),
    ("shift", 0x10),
    ("ctrl", 0x11),
    ("alt", 0x12),
    ("pause", 0x13),
    ("capslock", 0x14),
    ("kana", 0x15),
    ("hanguel", 0x15),
    ("hangul", 0x15),
    ("junja", 0x17),
    ("final", 0x18),
    ("hanja", 0x19),
    ("kanji", 0x19),
    ("esc", 0x1B),
    ("escape", 0x1B),
    ("convert", 0x1C),
    ("nonconvert", 0x1D),
    ("accept", 0x1E),
    ("modechange", 0x1F),
    (" ", 0x20),
    ("space", 0x20),
    ("pgup", 0x21),
    ("pgdn", 0x22),
    ("pageup", 0x21),
    ("pagedown", 0x22),
    ("end", 0x23),
    ("home", 0x24),
    ("left", 0x25),
    ("up", 0x26),
    ("right", 0x27),
    ("down", 0x28),
    ("select", 0x29),
    ("print", 0x2A),
    ("execute", 0x2B),
    ("prtsc", 0x2C),
    ("prtscr", 0x2C),
    ("prntscrn", 0x2C),
    ("printscreen", 0x2C),
    ("insert", 0x2D),
    ("del", 0x2E),
    ("delete", 0x2E),
    ("help", 0x2F),
    ("win", 0x5B),
    ("winleft", 0x5B),
    ("winright", 0x5C),
    ("apps", 0x5D),
    ("sleep", 0x5F),
    ("num0", 0x60),
    ("num1", 0x61),
    ("num2", 0x62),
    ("num3", 0x63),
    ("num4", 0x64),
    ("num5", 0x65),
    ("num6", 0x66),
    ("num7", 0x67),
    ("num8", 0x68),
    ("num9", 0x69),
    ("multiply", 0x6A),
    ("add", 0x6B),
    ("separator", 0x6C),
    ("subtract", 0x6D),
    ("decimal", 0x6E),
    ("divide", 0x6F),
    ("f1", 0x70),
    ("f2", 0x71),
    ("f3", 0x72),
    ("f4", 0x73),
    ("f5", 0x74),
    ("f6", 0x75),
    ("f7", 0x76),
    ("f8", 0x77),
    ("f9", 0x78),
    ("f10", 0x79),
    ("f11", 0x7A),
    ("f12", 0x7B),
    ("f13", 0x7C),
    ("f14", 0x7D),
    ("f15", 0x7E),
    ("f16", 0x7F),
    ("f17", 0x80),
    ("f18", 0x81),
    ("f19", 0x82),
    ("f20", 0x83),
    ("f21", 0x84),
    ("f22", 0x85),
    ("f23", 0x86),
    ("f24", 0x87),
    ("numlock", 0x90),
    ("scrolllock", 0x91),
    ("shiftleft", 0xA0),
    ("shiftright", 0xA1),
    ("ctrlleft", 0xA2),
    ("ctrlright", 0xA3),
    ("altleft", 0xA4),
    ("altright", 0xA5),
    ("browserback", 0xA6),
    ("browserforward", 0xA7),
    ("browserrefresh", 0xA8),
    ("browserstop", 0xA9),
    ("browsersearch", 0xAA),
    ("browserfavorites", 0xAB),
    ("browserhome", 0xAC),
    ("volumemute", 0xAD),
    ("volumedown", 0xAE),
    ("volumeup", 0xAF),
    ("nexttrack", 0xB0),
    ("prevtrack", 0xB1),
    ("stop", 0xB2),
    ("playpause", 0xB3),
    ("launchmail", 0xB4),
    ("launchmediaselect", 0xB5),
    ("launchapp1", 0xB6),
    ("launchapp2", 0xB7),
]


class KeyBoardMap(dict):
    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def __repr__(self):
        return repr(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __delitem__(self, key):
        del self.__dict__[key]

    def clear(self):
        return self.__dict__.clear()

    def copy(self):
        return self.__dict__.copy()

    def has_key(self, k):
        return k in self.__dict__

    def update(self, *args, **kwargs):
        return self.__dict__.update(*args, **kwargs)

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()


def fetch():
    _map = KeyBoardMap()
    for item in keyboard_mapping:
        _map.update({item[0]: item[1]})
    return _map


key_map = fetch()
