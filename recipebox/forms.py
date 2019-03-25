from django import forms
from recipebox.models import Author, User


class AddRecipe(forms.Form):
    author = forms.Select(
        choices=[(add.id, add.user.username) for add in Author.objects.all()])
    title = forms.CharField(max_length=120)
    total_time = forms.DurationField()
    instructions = forms.CharField(widget=forms.Textarea)
    description = forms.CharField(max_length=300)

    def __init__(self, req, user_is_staff, *args, **kwargs):
        pass
        super(AddRecipe, self).__init__(*args, **kwargs)
        if user_is_staff:
            self.choices = [
                (a.id, a.user.username) for a in Author.objects.all()]
        else:
            self.choices = [(req.user.id, req.user.username)]

        self.fields['author'] = forms.ChoiceField(choices=self.choices)


class AddAuthor(forms.Form):
    user = forms.Select(
        choices=[(u.id, u.username) for u in User.objects.all()])
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.Form):
    name = forms.CharField(max_length=60)
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
