'''
This is the first iteration of the concept. 
I will use path parameters to receive edit
proposals from a client and return the relevant changes
'''

from typing import List, Dict
import typing
import msgspec
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import HTMLResponse, JSONResponse
import markupsafe
import sqlite3
import string

from starlette.routing import Route

user_file: Dict[str, list[str]] = {'':[]}

class Properties(msgspec.Struct):
    bg_color: str = 'red'

decoder = msgspec.json.Decoder(type=Properties)

'''
I will have the html as a list of strings and simply
loop and do different string operations on the different
strings as needed
'''
class parser(msgspec.Struct, kw_only=True):
    html_list: list[str]

    @classmethod
    def find(cls, to_find: str, list_html: list):
        position = -1
        for i in list_html:
            position+=1
            if to_find in i:
                return {position:i}
            

    @classmethod
    def modify(cls, to_modify: dict, template: string.Template):
        #The idea here is we add the to_modify dict to a relevant template
        pass


test_template = string.Template('''
                                <html>
                                  <head></head>
                                  <body>
                                    <h1>${h1}</h1>
                                  </body>
                                </html>
                                ''')

def main_grid(request):
    html = '''<!DOCTYPE html>
<html>
  <head></head>
  <body>
    <h1>Hello There</h1>
  </body>
</html>'''
    return HTMLResponse(html)

async def pick_bg(request: Request):
    r_bytes = await request.body()
    properties = decoder.decode(r_bytes)
    color = properties.bg_color
    user_file['bg_color'] = color
    #atp i should somehow make the html elem have a style tag
    #but for now i'll just return a whole thing
    return HTMLResponse(f'''<!DOCTYPE html>
<html style='background-color: {color}'>
  <head></head>
  <body>
    <h1>Hello There</h1>
  </body>
</html>''')

app = Starlette(routes=[Route('/', main_grid),
                        Route('/pick_bg', pick_bg, methods=['POST'])],)

