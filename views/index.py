from django.http import HttpResponse
from django.views import View

class Index(View):
    """
    Just a test View
    """
    def get(self, request):
        return HttpResponse('This is just a test!')
