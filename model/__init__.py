from google.appengine.ext import db

class Framesheet(db.Model):
  """Models a framesheet entry containing only content."""
  content = db.TextProperty()
  fps = db.StringProperty()
  date = db.DateTimeProperty(auto_now_add=True)

class Piskel(db.Model):
  title = db.TextProperty()
  description = db.TextProperty()
  