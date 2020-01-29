from django import forms

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

# (importance, category, status, name, duedate, description) specified for Tasks
# (name, importance, description, category, status, duedate) specified for Tasks
class TasksForm(forms.Form):
    duedate = forms.DateField(widget=forms.SelectDateWidget)
    category = forms.ChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )
