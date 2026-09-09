from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Any, Literal, Tuple

app = FastAPI()

class Properties(BaseModel):
    size: Tuple[int, int] = (10, 10) #px
    link_to: Any | None = None
    bg_color: str = 'white'
    img: bool = False
    text: bool = False
    text_content: str | None = None
    text_font: str|None = None

def insert_at(html: str, content: str):
    count = 0
    opening_tag: str = ''
    closing_tag: str = ''
    for letter in html:
        count += 1
        if letter == '>':
            opening_tag = html[:count-1]
            closing_tag = html[count-1:]
            count = 0
    return opening_tag + content + closing_tag

@app.post('/edit/{page}')
def make_changes(
        page: str,
        properties: Properties
        ):
    html: str = ''
    if properties.link_to is not None:
        html = '<a></a>'
    if properties.img:
        #needs a helper function to check what html currently looks like and decid where to insert 
        #i have written it
        insert_at(html, '<img></img>')
    #etc
    return html
