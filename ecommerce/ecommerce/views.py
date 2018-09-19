from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from .form import ContactForm, LoginForm, RegisterForm


def home_page(request):
    context = {
        'title': "Home Page!",
        'content': "Welcom to the Home Page",
        'premium_content': "Yeah!"
    }
    return render(request, "hompage.html", context)


def about_page(request):
    context = {
        'title': "About Page!",
        'content': "Welcom to the About Page"
    }
    return render(request, "hompage.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title': "Contact Page!",
        'content': "Welcom to the Contact Page",
        'form': contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/view.html", context)


def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {
        'form': login_form
    }
    print(request.user.is_authenticated())
    if login_form.is_valid():
        print(login_form.cleaned_data)
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print("Error")
            context['form'] = LoginForm()

    return render(request, "auth/login.html", context)


def register_page(request):
    register_form = RegisterForm(request.POST or None)
    context = {
        'form': register_form
    }
    if request.method == 'POST':
        if register_form.is_valid():
            user = get_user_model()
            username = register_form.cleaned_data.get('username')
            password = register_form.cleaned_data.get('password')
            email = register_form.cleaned_data.get('email')
            new_user = user.objects.create_user(username, password, email)
            print(new_user)

    return render(request, "auth/register.html", context)
