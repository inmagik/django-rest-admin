
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.authtoken import views

class LoginView(APIView):

    """
    
    """
    permission_classes = (AllowAny,)
    
    def post(self, request, *args, **kwargs):
        if 'username' in request.data and 'password' in request.data:
            user = authenticate(username=request.data['username'], password=request.data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # Redirect to a success page.
                else:
                    # Return a 'disabled account' error message
                    pass
            else:
                # Return an 'invalid login' error message.
                return Response({"error": "Cannot login with provided credentials"},
                        status=status.HTTP_403_FORBIDDEN)

        else:
            return Response({"error": "missing fields for login"},
                        status=status.HTTP_400_BAD_REQUEST)
                
        


class LogoutView(APIView):

    """
    Calls Django logout method and delete the Token object
    assigned to the current User object.
    Accepts/Returns nothing.
    """
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            request.user.auth_token.delete()
        except:
            pass

        logout(request)

        return Response({"success": "Successfully logged out."},
                        status=status.HTTP_200_OK)




