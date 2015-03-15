import os
import re
import glob
import urllib
import urllib2
import logging

from google.appengine.api import files, app_identity
import jinja2
import webapp2
from webapp2_extras.routes import RedirectRoute


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


# class MainPage(webapp2.RequestHandler):
#     def get(self):
#         template_values = {
#         }

#         template = JINJA_ENVIRONMENT.get_template('index.html')
#         self.response.write(template.render(template_values))

class Translate(webapp2.RequestHandler):
    def get(self):
        lang = urllib.quote(self.request.get('lang', ''))
        q = urllib.quote(self.request.get('q', ''))

        tts_url = 'http://translate.google.com/translate_tts?'

        url = tts_url + 'tl=' + lang + '&q=' + q

        # Cheat to get around User-Agent deny
        req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
        response = urllib2.urlopen(req)
        data = response.read()

        self.response.headers.add_header("Access-Control-Allow-Origin", "*")
        self.response.write(data)

class Index(webapp2.RequestHandler):
    def get(self, subdir):
        dir = os.path.join('static', subdir)
        contents = glob.glob(os.path.join(dir, '*'))
        contents = [path.replace(dir, '') for path in contents]

        files = []
        dirs = []
        for path in contents:
            if path.startswith('/'):
                path = path[1:]
            full_path = os.path.join('/', subdir, path)
            if '.' in path:
                files.append({'text':path, 'path':full_path, 'dir':False})
            else:
                dirs.append({'text':path, 'path':full_path, 'dir':True})
        dirs.insert(0, {'text':'..', 'path':os.path.join('/', subdir, '..'), 'dir':True})
        template_values = {
            'links': dirs + files,
        }
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    #('/', MainPage),
    ('/tts', Translate),
    ('/([^\.]*/?)', Index),
], debug=True)