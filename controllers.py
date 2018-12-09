#!/usr/bin/env python

import cherrypy

class Root(object):

   def __init__(self, data):
      self.data = data

   @cherrypy.expose
   def index(self):
      return 'Hi! Welcome to your application'

def main(filename):
   data = {} # will be replaced with proper functionality later

   # configuration file
   cherrypy.config.update({
      'tools.encode.on': True, 'tools.encode.encoding': 'utf-8',
      'tools.decode.on': True,
      'tools.trailing_slash.on': True,
      'tools.staticdir.root': os.path.abspath(os.path.dirname(__file__)),
   })

   cherrypy.quickstart(Root(data), '/', {
      '/media': {
         'tools.staticdir.on': True,
         'tools.staticdir.dir': 'static'
      }
   })
    
if __name__ == '__main__':
main(sys.argv[1])