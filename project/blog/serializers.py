from rest_framework import serializers
from .models import Post

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'  # or ['id', 'title', 'content', 'author']
