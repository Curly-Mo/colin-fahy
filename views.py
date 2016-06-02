import webapp2


class Email(webapp2.RequestHandler):
    def post(self):
        from google.appengine.api import mail
        name = self.request.get('name', '')
        address = self.request.get('address', '')
        body = self.request.get('message', '')

        message = mail.EmailMessage()
        message.sender = address
        message.headers = {'On-Behalf-Of': '{} <{}>'.format(name, address)}
        message.subject = 'Email form (cfahy.com)'
        message.to = 'colin@cfahy.com'
        body = """
        this is a test
        """
        message.body = body

        message.send()

        data = 'Message Sent Successfully!'
        self.response.headers.add_header("Access-Control-Allow-Origin", "*")
        self.response.write(data)
