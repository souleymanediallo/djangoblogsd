from .models import Post, Category

post_category_all = Category(name='Toutes les Catégories')

def get_category_and_posts(category):
    posts = Post.objects.filter(published=True)
    if category == post_category_all.slug():
        category = post_category_all
    else:
        try:
            category = Category.objects.get(name__iexact=category)
            posts = posts.filter(category=category)
        except Category.DoesNotExist:
            category = Category(name=category)
            posts = Post.objects.none()

    posts = posts.order_by('-created')
    return category, posts

def get_categories():
    categories = list(Category.objects.all().order_by('name'))
    categories.insert(0, post_category_all)
    return categories