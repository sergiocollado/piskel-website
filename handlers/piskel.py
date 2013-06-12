import webapp2
import model

class Delete(webapp2.RequestHandler):
  def get(self):
    framesheet_key = self.request.get('l')
    admin_key = self.request.get('k')
    if admin_key == "pouet":
      framesheet = db.get(framesheet_key)
      framesheet.delete()

    self.response.headers['Access-Control-Allow-Origin'] = '*'
    self.response.out.write(framesheet_key)

class Get(webapp2.RequestHandler):
  def get(self):
    framesheet=''
    fps = '12'
    framesheet_key = self.request.get('l')
    if framesheet_key:
      framesheetObj = db.get(framesheet_key)
      framesheet = framesheetObj.content
      if framesheetObj.fps:
        fps = framesheetObj.fps

    self.response.headers['Access-Control-Allow-Origin'] = '*'
    self.response.out.write('{"framesheet" : '+framesheet+', "fps" : '+fps+'}')

class Store(webapp2.RequestHandler):
  def post(self):
    framesheet = model.Framesheet()
    framesheet.content = self.request.get('framesheet_content')
    framesheet.fps = self.request.get('fps_speed')

    framesheet.put()
    # only requests coming from the github demo are allowed to store new files 
    self.response.headers['Access-Control-Allow-Origin'] = '*'
    self.response.out.write(framesheet.key())
  def get(self):
    self.response.out.write('You cannot has GET here dude.')

class All(webapp2.RequestHandler):
  def get(self):
    framesheets = model.Framesheet.all()
    framesheets.order("-date")
    
    keys = []
    for framesheet in framesheets:
      keys.append("'%s'" % str(framesheet.key()))

    self.response.headers['Access-Control-Allow-Origin'] = '*'
    self.response.out.write("{keys : [%s]}" % ",".join(keys))