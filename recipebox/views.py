from django.shortcuts import render
from recipebox.models import Author, Recipe


def home_index(req):
    recipes = Recipe.objects.all()
    return render(req, 'index.html', {
        'recipes': recipes,
    }
    )


def author(req, author_id):
    author = Author.objects.get(id=author_id)
    recipes = Recipe.objects.filter(author=author)
    return render(req, 'author.html', {
        'author': author,
        'recipes': recipes,
    }
    )


def authors(req):
    authors = Author.objects.all()
    return render(req, 'authors.html', {
        'authors': authors,
    }
    )


def recipe(req, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(req, 'recipe.html', {
        'recipe': recipe
    }
    )
