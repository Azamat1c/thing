from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def log_in(request):
    if ('username' in request.REQUEST) and ('password' in request.REQUEST):
        username = request.REQUEST['username']
        password = request.REQUEST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect("/")
    return render_to_response('thing/login.html')

def log_out(request):
    auth.logout(request)
    return render_to_response('thing/logout.html')
