from django.shortcuts import render
from forum.models import Post, Replies
from forum.forms import PostForm, RepliesForm
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def show_forum(request):
    post_data = Post.objects.all()
    user = request.user

    context = {
        'list_of_post': post_data,
        #'list_of_answers': answer_data,
        'username': user.username,
    }
    
    return render(request, 'forum.html', context)

def show_discussion(request, id):
    selected_post = Post.objects.get(pk=id)

    context = {
        'post': selected_post,
        'id': id
    }
    return render(request, 'discussion.html', context)

@csrf_exempt
def create_forum_ajax(request):
    form = PostForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        data = Post.objects.last()

        result = {
            'username' : data.username,
            'id': data.id, 
            'date': data.date,
            'title': data.title,
            'content': data.content 
            }
        
        return JsonResponse(result)
    
    context = {'form': form}
    return render(request, "create_post.html", context)
    
def delete_forum(request, id):
    post = Post.objects.get(pk=id)
    post.delete()

    return HttpResponseRedirect(reverse('forum:show_forum'))

def get_post_json(request):
    data = Post.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_replies_json(request, id):
    selected_post = Post.objects.get(pk=id)
    replies = Replies.objects.filter(post=selected_post) 

    return HttpResponse(serializers.serialize("json", replies), content_type="application/json")

@csrf_exempt
def add_replies_ajax(request, id):
    selected_post = Post.objects.get(pk=id)
    form = RepliesForm(request.POST or None) 
    if request.method == 'POST' and form.is_valid:
        user = request.user
        post = selected_post
        content = request.POST.get('content') 

        new_replies = Replies.objects.create(
            user = user,
            username = request.user.username,
            post = post,
            content = content
        )

        result = {
        'username' : new_replies.username,
        'id': new_replies.id, 
        'date': new_replies.date,
        'content': new_replies.content 
        }
        
        return JsonResponse(result)


        



    

    


    
     

