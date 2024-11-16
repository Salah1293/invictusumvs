from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from django.utils.deprecation import MiddlewareMixin



class TokenRefreshMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user, token = JWTAuthentication().authenticate(request)

        if token and token.is_valid():
            return None 

       
        refresh_token = request.COOKIES.get('refresh_token')

        if refresh_token:
            try:
                refresh = RefreshToken(refresh_token)
                access_token = str(refresh.access_token)

                response = self.get_response(request)
                response['Authorization'] = f'Bearer {access_token}'

                return response
            except Exception as e:
                return Response({'error': 'Token refresh failed'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({'error': 'Access token expired, no valid refresh token'}, status=status.HTTP_401_UNAUTHORIZED)