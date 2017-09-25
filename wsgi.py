#!/usr/bin/env python

import falcon
import os
from wsgiref import simple_server

class StaticResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        with open('index.html', 'r') as f:
            resp.body = f.read()

application = falcon.API()
application.add_route('/', StaticResource())

if __name__ == '__main__':
    httpd = simple_server.make_server('0.0.0.0', 8000, application)
    httpd.serve_forever()
