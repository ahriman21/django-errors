
# ERROR:
==> # 'EmailField' object has no attribute name 'strip'

# CODE :
class UserRegisterApi(APIView):
    """ this API is used for registering new users """
    serializer_class = UserRegisterSerializer
    def post(self,request):
        srz_data = self.serializer_class(data=request.data)

        if srz_data.is_valid():
            # User.objects.create_user(email=srz_data['email'],password=srz_data['password1']) ==> this will cause an error
            User.objects.create_user(email=srz_data.get('email'),password=srz_data.get('password1'))

            return Response(data=srz_data.data,status=status.HTTP_201_CREATED)

        return Response(srz_data.errors,status=status.HTTP_400_BAD_REQUEST)

      
      
# NOTE :
# SOMETIMES THIS WAY OF WRITING CAUSES AN ERROR :
User.objects.create_user(email=srz_data['email'],password=srz_data['password1']) 

# THE RIGHT WAY :
User.objects.create_user(email=srz_data.get('email'),password=srz_data.get('password1'))
