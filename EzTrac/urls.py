from django.conf.urls import url
from .controllers.index import *
from .controllers.login import *
from .controllers.register import *
from .controllers.works import *
from .controllers.logout import *
from .controllers.graph import *

urlpatterns = [
    url(r'^$', index_req, name="index"),
    url(r'^login$', login, name="login"),
    url(r'^register$', register, name="register"),
    url(r'^how-it-works$', works, name="works"),
    url(r'^logout$', logout, name="logout"),
    url(r'^(?P<id>[0-9]+)$', graph, name="graph")
]