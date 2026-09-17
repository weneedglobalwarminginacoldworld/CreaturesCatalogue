import msgspec

class Properties(msgspec.Struct):
    faction: str #type
    bg_color: str
    href: str

