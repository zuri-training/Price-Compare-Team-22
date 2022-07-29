from django.shortcuts import render
from .models import Comment
from django.shortcuts import render, get_object_or_404 

# Create your views here.

def post_detail(request, slug):
    template_name = 'post_detail.html'
    content = get_object_or_404(content, slug=slug)
    comments = content.Comments.filter(active=True)
    new_comment = None
    if request.method == 'CONTENT':
        comment_serializers = Comment(data=request.CONTENT)
        if comment_serializers.is_valid():
            new_comment = comment_serializers.save(commit=False)
            new_comment.content = content
            new_comment.save()
        else:
            comment_serializers = Comment()

    return render(request, template_name, {'post': content,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_serializers})
