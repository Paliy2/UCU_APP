from django.contrib import admin
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe

from events.models import Event
from django import forms
from string import Template


def make_published(modeladmin, request, queryset):
    queryset.update(status='p')

class CommaSeparatedSelectInteger(forms.MultipleChoiceField):
    def to_python(self, value):
        if not value:
            return ''
        elif not isinstance(value, (list, tuple)):
            raise ValidationError(
                self.error_messages['invalid_list'], code='invalid_list'
            )
        return ','.join(value) #    ,'.join([str(val) for val in value])

    def validate(self, value):
        if self.required and not value:
            raise ValidationError(
                self.error_messages['required'], code='required'
            )

        # Validate that each value in the value list is in self.choices.
        for val in value.split(','):
            print(val)
            print(self.valid_value(val))
            if not self.valid_value(val):
                raise ValidationError(
                    self.error_messages['invalid_choice'],
                    code='invalid_choice',
                    params={'value': val},
                )

    def prepare_value(self, value):
        """ Convert the string of comma separated integers in list"""
        if value:
            value = value.split(',')
        return value


class PictureWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None, **kwargs):
        html = Template("""<img src="$link"/>""")
        return mark_safe(html.substitute(link=value))


class CategoryForm(forms.ModelForm):
    CATEGORIES = (('1', "Sociology"),
                  ('2', "Programming"),
                  ('3', "Lifeworks"),
                  )

    CATEGORIES = (('Sociology', "Sociology"),
                  ('Programming', "Programming"),
                  ('Lifeworks', "Lifeworks"),
                  )
    category = CommaSeparatedSelectInteger(widget=forms.CheckboxSelectMultiple, choices=CATEGORIES)

    def save(self, commit=True):
        instance = super(CategoryForm, self).save(commit=False)
        if commit:
            instance.save()
        return instance

    def clean_category(self):
        field = ""
        for data in self.cleaned_data['category']:
            field += str(data)
        return field.strip(",")


@admin.register(Event)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    ordering = ['name']
    actions = [make_published]
    form = CategoryForm
