from django import forms
from .models import Category


def populate_categories():
    # fecth all categories from db
    categories = Category.objects.all()

    choices = [("", "Please Select Category")]

    db_choices = [(category.id, category.name) for category in categories]
    choices.extend(db_choices)
    #select_message = ("", "Please Select Category")
    #choices.index(select_message, 0)
    return choices


choices = populate_categories()

# categories = [
#     ("", "Please Select Category"),
#     (1, "HOME"),
#     (2, "Office"),
#     (3, "Family")
#]

class CreateTaskForm(forms.Form):
    title = forms.CharField(required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
    due_date = forms.DateField(widget=forms.SelectDateWidget)
    category = forms.ChoiceField(choices=choices, required=True)

class UpdateTaskForm(CreateTaskForm):
    completed_date = forms.DateField(widget=forms.SelectDateWidget)