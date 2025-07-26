from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenObtainPairView as DefaultTokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Registration imports
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework import generics

# Custom serializer agar login bisa pakai email atau username
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        User = get_user_model()
        # Jika username berupa email, cari user berdasarkan email
        if username and '@' in username:
            try:
                user_obj = User.objects.get(email=username)
                attrs['username'] = user_obj.username
            except User.DoesNotExist:
                pass  # Akan gagal login jika email tidak ditemukan
        data = super().validate(attrs)
        data['user'] = {
            'id': self.user.id,
            'username': self.user.username,
            'email': self.user.email,
        }
        return data

# Custom view agar login bisa pakai email atau username
class CustomTokenObtainPairView(DefaultTokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


# Registration serializer and view
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = get_user_model()
        fields = ("id", "username", "email", "password")

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )
        return user

class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', include('products.urls')),
    path('api/shop/', include('shop.urls')),
    path('api/auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/register/', RegisterView.as_view(), name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)