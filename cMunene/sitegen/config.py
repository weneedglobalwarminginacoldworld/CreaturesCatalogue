import msgspec
from msgspec import structs
import uuid

class _DataThing(msgspec.Struct):
    name: str
    type_is: str
    content: list
    data_id: uuid.UUID = uuid.uuid8()



class SiteData(msgspec.Struct):
    TEXT: list[_DataThing] = []
    IMAGES: list[_DataThing] = []
    LINKS: list[_DataThing] = []
    MUSIC: list[_DataThing] = []
    METAS: list[_DataThing] = []
    ATTRIBUTION: list[_DataThing] = []

def create_thing(n, t, c) -> _DataThing:
    return _DataThing(n, t, c)


#MySiteData. I'm Going for a spec-bio aesthetic

MY_SITE_DATA = SiteData()
tl = ['Work With Me', 'What Im Upto', 'What I believe', 'What Ive Done', 'Bored?']
for c in tl:
    n = f"opt-{c.split()[0]}"
    t = "test"
    MY_SITE_DATA.TEXT.append(create_thing(n, t, c))
