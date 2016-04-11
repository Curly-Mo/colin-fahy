import urllib
import urllib2

import webapp2

class Translate(webapp2.RequestHandler):
    def get(self):
        lang = self.request.get('lang', '')
        q = self.request.get('q', '')

        tts_url = 'http://translate.google.com/translate_tts?'

        if not lang:
            lang = 'en'
        url = tts_url + 'tl=' + urllib.quote(lang) + '&q=' + urllib.quote(q)

        # Cheat to get around User-Agent deny
        req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
        response = urllib2.urlopen(req)
        data = response.read()

        self.response.headers.add_header("Access-Control-Allow-Origin", "*")
        self.response.write(data)
