from functools import wraps
from rest_framework.response import Response
from rest_framework import status


#DECORATOR TO MAKE SPECIFIC ROLES ACCESS VIEWS
def roles_required(*roles):
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                print('login user is:', request.user)
                user_roles = request.user.profile.role.all().values_list('name', flat=True) 
                print('user roles:', user_roles) 
                if any(role in user_roles for role in roles):  
                    return func(request, *args, **kwargs)
            return Response({'error': 'You do not have permission to do this action.'}, status=status.HTTP_403_FORBIDDEN)
        return wrapper
    return decorator