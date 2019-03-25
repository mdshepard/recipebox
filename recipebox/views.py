from django.shortcuts import render, redirect
from django.shortcuts import reverse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from recipebox.forms import AddAuthor, AddRecipe, SignupForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from recipebox.models import Author, Recipe, User


def home_index(req):
    recipes = Recipe.objects.all()
    return render(
        req,
        'index.html',
        {
            'recipes': recipes,
            }
    )


def recipe(req, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(req, 'recipe.html', {'recipe': recipe})


def author(req, author_id):
    author = Author.objects.get(id=author_id)
    recipes = Recipe.objects.filter(author=author)
    return render(
        req,
        'author.html',
        {
            'author': author,
            'recipes': recipes,
        }
    )


def authors(req):
    authors = Author.objects.all()
    return render(
        req,
        'authors.html',
        {
            'authors': authors
        }
    )


@login_required()
@staff_member_required(login_url='error')
def add_author(req):

    form = None

    if req.method == 'POST':
        form = AddAuthor(req.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data['name'],
                bio=data['bio'],
                user=data['user']
            )
            return render(req, 'updated.html')
    else:
        form = AddAuthor()

    return render(req, 'add_author.html', {'form': form})


@login_required()
def add_recipe(req):

    if req.method == 'POST':
        form = AddRecipe(req.POST)

        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data['title'],
                description=data['description'],
                instructions=data['instructions'],
                author=req.user.author,
                time_required=data['time_required']
            )
            return redirect(reverse('home'))
    else:
        form = AddRecipe(req, req.user.is_staff)

    return render(req, 'add_recipe.html', {'form': form})


def login_view(request):

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'], password=data['password']
                )

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', '/'))
    else:
        form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})


def logout_view(request):

    logout(request)
    return HttpResponseRedirect(request.GET.get('next', '/'))


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                data['username'],
                data['email'],
                data['password']
            )
            login(request, user)
            Author.objects.create(
                name=data['name'],
                user=user
            )
            return HttpResponseRedirect(reverse('index'))
    else:
        form = SignupForm()
    return render(request, 'generic_form.html', {"form": form})
