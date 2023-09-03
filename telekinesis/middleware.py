import os
from django.middleware.security import MiddlewareMixin
from django.shortcuts import redirect

class EnforceHttpsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if os.environ.get('DJANGO_ENV') == 'production' and not request.is_secure():
            return redirect(request.build_absolute_uri().replace("http://", "https://"))
