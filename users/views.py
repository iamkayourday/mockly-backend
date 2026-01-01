from .models import User
from .serializers import UserSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
import random

# Create your views here.

# Returns a list of users with filtering, searching, and ordering capabilities
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['first_name', 'last_name', 'gender', 'email', 'job_title', 'company']
    search_fields = ['first_name', 'last_name', 'email', 'job_title', 'company']
    ordering_fields = ['first_name', 'last_name', 'created_at']

    def get_queryset(self):
        """Override to support limit parameter"""
        queryset = super().get_queryset()
        
        # Support limit parameter for backward compatibility
        limit = self.request.query_params.get('limit')
        if limit and limit.isdigit():
            # Remove pagination for limit parameter
            self.pagination_class = None
            return queryset[:int(limit)]
        
        return queryset

# Returns details of a specific user by ID
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'    

# Creates new User
class UserCreateView(generics.CreateAPIView):
    pass

# Update existing User
class UserUpdateView(generics.UpdateAPIView):
    pass

# Deletes a User
class UserDeleteView(generics.DestroyAPIView):
    pass
    
# Returns a random user
class RandomUserView(APIView):
      
      def get(self, request):
        count = User.objects.count()
        if count == 0:
            return Response(
                {"error": "No users available in database"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        random_index = random.randint(0, count - 1)
        random_user = User.objects.all()[random_index]
        
        serializer = UserSerializer(random_user)
        return Response(serializer.data)

# Returns total number of users
class UsersCountView(APIView):
    
    # Returns total number of users
   
    def get(self, request):
        count = User.objects.count()
        return Response({"count": count})