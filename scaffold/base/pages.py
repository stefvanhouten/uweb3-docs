#!/usr/bin/python
"""Request handlers for the uWeb3 project scaffold"""

import uweb3

class PageMaker(uweb3.DebuggingPageMaker):
  """Holds all the request handlers for the application"""

  def Uweb(self):
    return self.parser.Parse("uweb.html")

  def About(self):
    return self.parser.Parse('about.html')

  def Contact(self):
    return self.parser.Parse('contact.html')

  def FourOhFour(self, path):
    """The request could not be fulfilled, this returns a 404."""
    self.req.response.httpcode = 404
    return self.parser.Parse('404.html', path=path)

  def Documentation(self):
      return self.parser.Parse('documentation/index.html')

  def Installation(self):
    return self.parser.Parse('documentation/installation.html')

  def GettingStarted(self):
    return self.parser.Parse('documentation/gettingStarted.html')

  def Configuartion(self):
    return self.parser.Parse('documentation/configuartion.html')

  def DocPageMaker(self):
    return self.parser.Parse('documentation/pagemaker.html')

  def DocModel(self):
    return self.parser.Parse('documentation/model.html')

  def DocTemplateParser(self):
    return self.parser.Parse('documentation/templateparser.html')

  def DocRequest(self):
    return self.parser.Parse('documentation/request.html')

  def DocResponse(self):
    return self.parser.Parse('documentation/response.html')

  def Routing(self):
    return self.parser.Parse('documentation/routing.html')

  #BETA
  def Beta(self):
    return self.parser.Parse('documentation/beta/index.html')

  def HotReloading(self):
    return self.parser.Parse('documentation/beta/hot_reload.html')

  def SqlAlchemy(self):
    return self.parser.Parse('documentation/beta/sqlalchemy.html')

  def RouteDetection(self):
    return self.parser.Parse('documentation/beta/route_detection.html')

  def IniManager(self):
    return self.parser.Parse('documentation/beta/ini_manager.html')

  def SecureCookies(self):
    return self.parser.Parse('documentation/beta/secure_cookie.html')

  def XsrfDecorator(self):
    return self.parser.Parse('documentation/beta/xsrf_decorator.html')

  def EscapingModule(self):
    return self.parser.Parse('documentation/beta/escaping_module.html')

  def EventListener(self):
    return self.parser.Parse('documentation/beta/event_listener.html')

  def WebSockets(self):
    return self.parser.Parse('documentation/beta/websockets.html')

  def LoginExample(self):
    return self.parser.Parse('documentation/beta/login_example.html')

  def BetaPageMaker(self):
    return self.parser.Parse('documentation/beta/pagemaker.html')
