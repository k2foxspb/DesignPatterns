from wsgiref.simple_server import make_server

from framework.main import Framework, DebugApplication, FakeApplication
from urls import fronts
from views import routes

application = FakeApplication(routes, fronts)
with make_server('', 8000, application) as httpd:

    print('Serving on port 8000... http://127.0.0.1:8000')
    httpd.serve_forever()

