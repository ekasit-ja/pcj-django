from django import forms
from .models import Project

class ProjectForm(forms.Form):
    country = forms.ChoiceField()
    year = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        projects = Project.objects.all()
        # c = kwargs['initial']['country']
        # y = kwargs['initial']['year']

        # if c and c != 'all':
        #     projects = projects.filter(country=c)
        # if y and y != 'all':
        #     projects = projects.filter(year=y)

        # Distinct for SQLite is not supported
        # Therefore, have to implement distinct value manually
        countries = set()
        years = set()

        for p in projects:
            countries.add((p.country, p.country))
            years.add((p.year, p.year))

        countries = list(countries)
        years = list(years)

        # Sort ascending order
        countries.sort()
        years.sort()

        countries.insert(0, ('all', 'all'))
        years.insert(0, ('all', 'all'))

        self.fields['country'].choices = countries
        self.fields['year'].choices = years
