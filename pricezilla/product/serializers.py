from rest_framework import serializers
from datetime import datetime
from serializers import CommentSerializer

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length = 200)
    created = serializers.DateTimeField()

class Comment(object):
    def __init__(self, name, email, content, created = None):
        self.name = name
        self.email = email
        self.content = content
        self.created = created or datetime.now()
comment = Comment(name ='leila', email ='leila@example.com', content ='foo bar')
serializer = CommentSerializer(Comment)
serializer.data