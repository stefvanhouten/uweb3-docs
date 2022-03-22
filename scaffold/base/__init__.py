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
  - The execution path, internally used to find templates etc.
  """
  return uweb3.uWeb(pages.PageMaker,
      [
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
      ('/documentation/beta/login_example', 'LoginExample'),
      ('/documentation/beta/pagemaker', 'BetaPageMaker'),
      ('/static/(.*)', 'Static'),
      ('/(.*)', 'FourOhFour'),
      ],
      os.path.dirname(__file__)
  )
