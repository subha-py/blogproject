from rest_framework.generics import(
        CreateAPIView,
        ListAPIView,
        RetrieveAPIView,
        RetrieveUpdateAPIView,
        RetrieveDestroyAPIView,
    )
from ..models import Post
from .serializers import(
        PostDetailSerializer,
        PostListSerializer,
        PostCreateSerializer
    )

class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects .all()
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class PostListAPIView(ListAPIView):
    queryset = Post.objects .all()
    serializer_class = PostListSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'


class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
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
