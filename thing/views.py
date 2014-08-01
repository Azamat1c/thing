from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

def log_in(request):
    c = {}
    c.update(csrf(request))
    if ('username' in request.REQUEST) and ('password' in request.REQUEST):
        username = request.REQUEST['username']
        password = request.REQUEST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return render_to_response("thing/login_right.html", c)
        else:
            return render_to_response("thing/login_fatal.html")
    return render_to_response('thing/login.html', c)

def log_out(request):
    auth.logout(request)
    return render_to_response('thing/logout.html')
