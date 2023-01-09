from django.http import HttpResponse
from django.shortcuts import redirect
from .models import BlogPost


def unauthenticated_user(func):
    """This decorator allows only unauthenticated user to access the views & restrict the authenticated user form accessing the same & redirects them to 'home' views."""
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return func(request, *args, **kwargs)
    return wrapper


def allowed_user(allowed_roles=[]):
    """This decorator help in restricting the access to certain pages according to the user's group/groups."""
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return func(request, *args, **kwargs)
            return HttpResponse("Restricted! You are not allowed to visit this page")
        return wrapper
    return decorator


def admin_only(func):
    """This decorator restricts all the users other then admin to access a certain page."""
    def wrapper(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == "admin":
            return redirect("home")
        if group == "customer":
            return func(request, *args, **kwargs)
    return wrapper


def ower_only(func):
    def wrapper(request, *args, **kwargs):
        user_id = post = request.user.id
        post = BlogPost.objects.get(id=kwargs["post_id"])
        post_author_id = post.author.id
        if user_id != post_author_id:
            return HttpResponse("You are not allowed to edit/delete this post!")
        return func(request, *args, **kwargs)
    return wrapper
