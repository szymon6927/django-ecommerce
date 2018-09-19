from django.shortcuts import render


def home_page(request):
    context = {
        'title': "Home Page!",
        'content': "Welcom to the Home Page"
    }
    return render(request, "hompage.html", context)


def about_page(request):
    context = {
        'title': "About Page!",
        'content': "Welcom to the About Page"
    }
    return render(request, "hompage.html", context)


def contact_page(request):
    context = {
        'title': "Contact Page!",
        'content': "Welcom to the Contact Page"
    }
    return render(request, "hompage.html", context)
