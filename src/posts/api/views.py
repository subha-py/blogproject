from django.db.models import Q

from rest_framework.generics import(
        CreateAPIView,
        ListAPIView,
        RetrieveAPIView,
        RetrieveUpdateAPIView,
        RetrieveDestroyAPIView,
    )
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)
from .pagination import PostLimitOffsetPagination
from ..models import Post
from .serializers import(
        PostDetailSerializer,
        PostListSerializer,
        PostCreateSerializer
    )

from rest_framework.permissions import (
    IsAdminUser,
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)
from .permissions import IsOwnerOrReadOnly



class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects .all()
    permission_classes = [IsAuthenticated,IsAdminUser]
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class PostListAPIView(ListAPIView):
    serializer_class = PostListSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_field=['title','content','user__first_name']
    pagination_class = PostLimitOffsetPagination
    def get_queryset(self,*args,**kwargs):
        queryset_list=Post.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query)
            ).distinct()
        return queryset_list
class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'


class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsOwnerOrReadOnly,IsAuthenticatedOrReadOnly]
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class PostDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
