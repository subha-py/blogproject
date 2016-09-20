from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
)

from ..models import Post

post_detail_url=HyperlinkedIdentityField(
        view_name='posts-api:detail',
        lookup_field='slug',
    )
class PostCreateSerializer(ModelSerializer):
    class Meta:
        model=Post
        fields=[
            'title',
            'content',
            'publish',
        ]


class PostListSerializer(ModelSerializer):
    url=post_detail_url
    user=SerializerMethodField()
    image=SerializerMethodField()
    html = SerializerMethodField()
    class Meta:
        model=Post
        fields=[
            'title',
            'url',
            'content',
            'publish',
            'user',
            'image',
            'html',
        ]
    def get_user(self,obj):
        return str(obj.user.username)

    def get_image(self,obj):
        try:
            image=obj.image.url
        except:
            image=None
        return image

    def get_html(self,obj):
        return obj.get_markdown()

class PostDetailSerializer(ModelSerializer):
    url=post_detail_url
    class Meta:
        model=Post
        fields=[
            'id',
            'title',
            'slug',
            'content',
            'publish',
            'url'
        ]