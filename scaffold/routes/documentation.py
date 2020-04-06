import uweb3

class PageMaker(uweb3.DebuggingPageMaker):
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

  def Routing(self):
    return self.parser.Parse('documentation/routing.html')
