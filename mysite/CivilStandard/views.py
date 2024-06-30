from django.shortcuts import render
from django.http import HttpResponse
from .forms import ArticleForm


# Create your views here.
def home(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            return HttpResponse("Article saved!")
    else:
        form = ArticleForm
    return render(request, "home.html", {"form": form})
