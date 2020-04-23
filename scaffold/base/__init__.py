"""A minimal uWeb3 project scaffold."""

# Standard modules
import os

# Third-party modules
import uweb3

# Application
from . import pages

def main():
  """Creates a uWeb3 application.

  The application is created from the following components:

  - The presenter class (PageMaker) which implements the request handlers.
  - The routes iterable, where each 2-tuple defines a url-pattern and the
    name of a presenter method which should handle it.
  - The configuration file (ini format) from which settings should be read.
  """
  config_file = os.path.join(os.path.dirname(__file__), 'config.ini')
  config = uweb3.read_config(config_file)
  routes = [
      ('/', 'Uweb'),
      ('/about', 'About'),
      ('/contact', 'Contact'),
      ('/documentation', 'Documentation'),
      ('/documentation/installation', 'Installation'),
      ('/documentation/getting_started', 'GettingStarted'),
      ('/documentation/configuartion', 'Configuartion'),
      ('/documentation/routing', 'Routing'),
      ('/documentation/pagemaker', 'DocPageMaker'),
      ('/documentation/model', 'DocModel'),
      ('/documentation/templateparser', 'DocTemplateParser'),
      ('/documentation/request', 'DocRequest'),
      ('/documentation/response', 'DocResponse'),
      #BETA
      ('/documentation/beta', 'Beta'),
      ('/documentation/beta/hotreloading', 'HotReloading'),
      ('/documentation/beta/sqlalchemy', 'SqlAlchemy'),
      ('/documentation/beta/route_detection', 'RouteDetection'),
      ('/documentation/beta/settings_manager', 'IniManager'),
      ('/documentation/beta/secure_cookies', 'SecureCookies'),
      ('/documentation/beta/xsrf_decorator', 'XsrfDecorator'),
      ('/documentation/beta/escaping_module', 'EscapingModule'),
      ('/documentation/beta/event_listener', 'EventListener'),
      ('/documentation/beta/websockets', 'WebSockets'),
      ('/static/(.*)', 'Static'),
      ('/(.*)', 'FourOhFour'),
      ]
  return uweb3.uWeb(pages.PageMaker, routes, config=config)
