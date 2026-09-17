from string import Template

import msgspec

from config import Properties

class HTemplater(msgspec.Struct):
    properties: Properties

    
    @classmethod
    def make_img(cls, properties: Properties) -> Template:
        props = properties
        l_props = {}
        snippets = []
        if props.bg_color:
            l_props['background-color'] = '${bg_color}'
        if props.href:
            l_props['href'] = '${href}'
        for k, v in l_props.items():
            snippets.append(f'{k}="{v}"')

        template = '<img ' + ' '.join(snippets) + ' >'
        return Template(template)
