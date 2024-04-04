from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Post, Comment, Like, Followers, Profile
from .forms import CommentForm

class UserBlogView(ListView):
    model = Post
    template_name = 'user_blog.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return Post.objects.filter(blog__author__id=user_id).order_by('-published_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs.get('user_id')
        context['profile'] = get_object_or_404(Profile, user_id=user_id)
        return context

def comment_list(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'todos/comment_list.html', {'post': post, 'comments': comments})

def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('comment_list', post_id=post_id)
    else:
        form = CommentForm()
    return render(request, 'todos/add_comment.html', {'form': form})

def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
    return redirect('post_detail', post_id=post_id)

def user_followers(request, user_id):
    user = get_object_or_404(User, id=user_id)
    followers = Followers.objects.filter(following=user)
    return render(request, 'todos/user_followers.html', {'user': user, 'followers': followers})

def follow_user(request, user_id):
    return HttpResponse("Follow functionality not implemented yet")
