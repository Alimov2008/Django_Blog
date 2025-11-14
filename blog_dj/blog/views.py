from django.shortcuts import render

posts = [
    {
        "author": "josh",
        "title": "applications",
        "content": "First post",
        "data_posted": "Aughust 27, 2020",
    },
    {
        "author": "max",
        "title": "ML",
        "content": "second post",
        "data_posted": "March 3, 2023",
    },
]


def home(request):
    context = {"post": posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
