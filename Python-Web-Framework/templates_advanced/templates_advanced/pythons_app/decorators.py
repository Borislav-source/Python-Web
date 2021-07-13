from django.http import HttpResponse


def authorised_users_only(groups=[]):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            if not request.user.is_authenticated:
                return HttpResponse('You need to be authorised user')
            if not request.user.groups.exists():
                return HttpResponse(f'You have to be in at least one of these groups: {", ".join(groups)}')
            user_groups = [gr.name for gr in request.user.groups.all()]
            if not set(user_groups).intersection(groups):
                return HttpResponse(f'You have to be in at least one of these groups: {", ".join(groups)}')
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
