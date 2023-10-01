from django.shortcuts import render

# Create your views here.
def blog_view(request):
    return render(request, 'blog/blog-home.html')

def blog_single(request):
    context={'title':'Bitcoin Crashed', 'content':'Bitcoin uses peer-to-peer technology to operate with no central authority or banks; managing transactions and the issuing of bitcoins is carried out collectively by the network. Bitcoin is open-source; its design is public, nobody owns or controls Bitcoin and everyone can take part. Through many of its unique properties, Bitcoin allows exciting uses that could not be covered by any previous payment system.', 'author':'Mohammad Mahdi Niknam'}
    return render(request, 'blog/blog-single.html', context)