from django.shortcuts import render, get_object_or_404, redirect
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404
from .models import Tweet


# Creating the view here

def index(request):
    return render(request, 'index.html')


def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})


# Tweet form creation

@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweet_list")
    else:
        form = TweetForm()
    return render(request, "tweet_form.html", {"form": form})


# Editing the tweet form

@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweet_list")
    else:
        form = TweetForm(instance=tweet)
    return render(request, "tweet_form.html", {"form": form})


# Deleting the tweet

@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect("tweet_list")
    return render(request, "Tweet_confirm_delete.html", {"tweet": tweet})


# Register views

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


# Search for tweets

def search_view(request):
    query = request.GET.get('q', '')  # Get the search query from the request
    results = Tweet.objects.filter(text__icontains=query) if query else []  # Search tweets by the 'text' field
    return render(request, 'search_results.html', {'results': results, 'query': query})



#  tweet details fro searching the accurate tweet

def tweet_detail(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    return render(request, 'tweet_detail.html', {'tweet': tweet})



def search_view(request):
    query = request.GET.get('q', '')  # Get the search query
    results = Tweet.objects.filter(text__icontains=query) if query else []  # Filter tweets by text
    return render(request, 'search_results.html', {'results': results, 'query': query})
