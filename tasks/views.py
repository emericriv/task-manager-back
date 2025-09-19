from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


class RegisterView(APIView):
    permission_classes = []  # Accessible sans authentification

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")

        if not username or not password:
            return Response(
                {"error": "Username and password required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create_user(
            username=username, password=password, email=email
        )
        return Response({"message": "User created"}, status=status.HTTP_201_CREATED)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response(
            {
                "username": user.username,
                "email": user.email,
            }
        )


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()  # Ajouté pour DRF router
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(assigned_to=user)

    def perform_create(self, serializer):
        serializer.save(assigned_to=self.request.user)
