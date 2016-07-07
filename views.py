import webapp2


class Email(webapp2.RequestHandler):
    def post(self):
        from google.appengine.api import mail
        name = self.request.get('name', '')
        address = self.request.get('address', '')
        body = self.request.get('message', '')

        message = mail.EmailMessage()
        message.sender = '{} <{}>'.format(name, 'colin-fahy@appspot.gserviceaccount.com')
        message.subject = 'Email on behalf of: {}, {}'.format(name, address)
        message.to = 'colin@cfahy.com'
        message.body = body

        message.send()

        data = 'Message Sent Successfully!'
        self.response.headers.add_header("Access-Control-Allow-Origin", "*")
        self.response.write(data)
