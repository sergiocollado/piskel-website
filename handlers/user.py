import webapp2
from webapp2_extras import jinja2

class UserHandler(webapp2.RequestHandler):
  @webapp2.cached_property
  def jinja2(self):
    # Returns a Jinja2 renderer cached in the app registry.
    return jinja2.get_jinja2(app=self.app)

  @webapp2.cached_property
  def is_logged_in(self):
    return True

  @webapp2.cached_property
  def username(self):
    return "Julian"   
      
  def get(self, userpage):
    self.render("user.html")
    # self.response.write(userpage)

  def get_showcase_piskel_ids(self):
    return [12, 15, 18]

  def render(self, template_name):
    # read the template or 404.html
    try:
      values = {
        'username': self.username if self.is_logged_in else False,
        #'session': self.auth.get_user_by_session() if self.logged_in else False,
        'is_logged_in': self.is_logged_in,
        'showcase_piskels' : self.get_showcase_piskel_ids()
      }
      #directory = os.path.dirname(__file__)
      #templates = os.path.join(directory, os.path.pardir, 'templates', template_name)
      self.response.write(self.jinja2.render_template(template_name, **values))
    except TemplateNotFound:
      self.abort(404)