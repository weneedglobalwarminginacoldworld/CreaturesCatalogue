'''mixes the functions from make to make logical html'''

from os import name
from make import *
import config

#All funcs in this moduke take a templat and data from a config file. My next task 
#will be preparing the data
def welcome_mix(data: config.SiteData):
    #the idea is this expects to just substitute 
    the_page = page()
    layers = [layer_make() for _ in range(3)]
    b = body_make()
    full_page = html_make()
    h = head_make()
    m = meta_make(name=True, content=True)
    m1 = None
    if data.METAS != []:
        for mc in data.METAS:
            if mc.name.startswith('meta'):
                m1 = m.substitute(name=mc.name, content=mc.content)
                print('m1')
    h1=h.safe_substitute(metas=m1)



