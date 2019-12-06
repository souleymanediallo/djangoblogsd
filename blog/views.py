from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from .models import Post, Comment
from blog import model_helpers
from .forms import CreateCommentForm
from django.core.paginator import Paginator

# Create your views here.
def home(request, category=model_helpers.post_category_all.slug()):
    category, posts = model_helpers.get_category_and_posts(category)
    categories = model_helpers.get_categories()

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {'posts': posts, 'category': category, 'categories': categories}

    return render(request, "blog/index.html", context)

def post_detail(request, post_id, message=''):
    post = get_object_or_404(Post, pk=post_id)
    post_same_category = Post.objects.filter(published=True, category=post.category).exclude(pk=post_id)
    categories = model_helpers.get_categories()
    comments = post.comments.all().exclude(status=Comment.STATUS_HIDDEN).order_by('created')

    if request.method == 'POST':
        comment_form = CreateCommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            args = [post.pk, "Votre message a été posté"]
            return HttpResponseRedirect(reverse('blog:post_detail_message', args=args) + '#comments')
    else:
        comment_form = CreateCommentForm()

    context = {
        'post': post,
        'categories': categories,
        'post_same_category': post_same_category,
        'comments': comments,
        'comment_form': comment_form,
        'message': message
    }
    return render(request, "blog/post_detail.html", context)


def about(request):
    return render(request, "blog/about.html")