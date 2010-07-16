#!/usr/bin/env python
import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util, template

class MainHandler(webapp.RequestHandler):
    def get(self):
        name = 'People'
        
        try:
            name = self.request.GET.items()[0][0]
        except IndexError:
            pass

        template_values = {
            'name': name,
        }

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))


def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
