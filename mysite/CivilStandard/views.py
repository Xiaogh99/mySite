from django.shortcuts import render
from django.http import HttpResponse
from .forms import ArticleForm
from .models import Standard


# Create your views here.
def add_a_standard(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            codeID = form.cleaned_data["codeID"]
            date = form.cleaned_data["date"]
            a_standard = Standard(title=title, codeID=codeID, published_date=date)
            a_standard.save()
            # a_standard.save()
            return HttpResponse("Standard saved!")
    else:
        form = ArticleForm
    return render(request, "home.html", {"form": form})
