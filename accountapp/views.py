from rest_framework import mixins, viewsets, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .models import Account
from .serializers import AccountSerializer


class AccountRegistrationGenericViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    
    
class SignoutView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        """
        Handle the HTTP POST request.

        This method is responsible for handling the HTTP POST request made to the endpoint. It takes in a `request` object as a parameter, which contains the request data.

        Parameters:
            request (HttpRequest): The HTTP request object containing the request data.

        Returns:
            Response: The HTTP response object with the appropriate status code.

        Raises:
            Exception: If an error occurs during the processing of the request.

        This function attempts to extract the "refresh" token from the request data and create a `RefreshToken` object. It then adds the token to the blacklist, effectively invalidating it. If the process is successful, the function returns a response with the status code `HTTP_205_RESET_CONTENT`. If an exception occurs during the process, the function returns a response with the status code `HTTP_400_BAD_REQUEST`.
        """
        
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            
            return Response(status=status.HTTP_400_BAD_REQUEST)