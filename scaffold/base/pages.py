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