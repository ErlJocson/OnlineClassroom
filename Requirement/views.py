from django.shortcuts import render

# Create your views here.
def postView(requets):
    context = {
        'title':'Post'
    }
    return render(requets, 'post.html', context)

