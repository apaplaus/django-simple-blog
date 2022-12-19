from django.shortcuts import render
from django.http import HttpResponse

test_posts = [
    {
        'autor': 'Igorochek228',
        'title': 'Big ass TITLE',
        'content': 'Placeholder post content.',
        'date_posted': '2/2/1488'
    },
    {
        'autor': 'Tvoj papasha',
        'title': 'Prodam garaz',
        'content': 'Prodam garaz nedorogo tel. +1488 132-793-163-14',
        'date_posted': '2/12/2022'
    },
    {
        'autor': 'Vi\'ka',
        'title': 'Papich fan story',
        'content': 'Ishu molodogo (net) dotera po klichke vPopich ili chto-to vrode togo.',
        'date_posted': '12/12/2023'
    }
]

def home(request):
    context = {
        'posts': test_posts,
    }
    return render(request, 'blog_app/home.html', context)

def about(request):
    return render(request, 'blog_app/about.html', {'title': 'Obout club Pinguine'})
