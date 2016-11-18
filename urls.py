from django.conf.urls import url
from mainsite.views.index import Index

urlpatterns = [
    url(r'^$', Index.as_view())
]
