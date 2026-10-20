"""Spits out boilerplate templates for every page"""

 
import msgspec
from string import Template
import config

def meta_make(name =False, content=False, charset=False):
    if name:
        return (Template('<meta name="$name" content="$content" >') if content else
                Template('<meta name="$name">'))
    if charset:
        return (Template('<meta charset="$charset" >'))


def head_make():
    return Template('''
                    <head>\n$metas\n$links\n$scripts\n</head>
                    ''')

def html_make():
    return Template('<DOCTYPE Html>\n$head\n$body')

def body_make():
    return Template('''
    <body>$layer</body>
    ''')

def layer_make():
    return Template('''
    <div id=$id_name class="layer_$id_name>\n$content\n</div>
    ''')

'''
Now The Pages
'''
def page():
    return Template('''
                    <div id="main_page">\n$layers\n</div>
                    ''')


#Specific Template

