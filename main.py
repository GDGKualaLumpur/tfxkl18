import webapp2

class SlashRedirect(webapp2.RequestHandler):
  def get(self, *args, **kwargs):
    self.redirect('//' + self.request.host + '/tfxkl18/')

class TensorflowExteneded(webapp2.RequestHandler):
  def get(self, *args, **kwargs):
    path = self.request.path_qs.split('/')
    if (path[1] != 'tfxkl'):
        self.redirect('https://www.gdgkl.org')
    else:
        self.redirect('//' + self.request.host + '/tfxkl18/' + '/'.join(path[2:]))

app = webapp2.WSGIApplication([
    ('/tfxkl18.*', SlashRedirect),
    ('/tfxkl.*', TensorflowExteneded)
], debug=True)