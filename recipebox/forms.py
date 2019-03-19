from django import forms
from recipebox.models import Author, User


class AddRecipe(forms.Form):
    author = forms.Select(
        choices=[(add.id, add.user.username) for add in Author.objects.all()])
    title = forms.CharField(max_length=120)
    total_time = forms.DurationField()
    instructions = forms.CharField(widget=forms.Textarea)
    description = forms.CharField(max_length=300)

    def clean_recipe_data(self):
        pass


class AddAuthor(forms.Form):
    user = forms.Select(
        choices=[(u.id, u.username) for u in User.objects.all()])
