from tabnanny import verbose
from django import forms
from django.core.exceptions import ValidationError

from mainapp.models import News

class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return title


PAGINATE_BY =(
("10", "10"),
("20", "20"),
("50", "50"),
)


class PaginateForm(forms.Form):
    paginate_by = forms.ChoiceField(choices = PAGINATE_BY, label="Количество новостей страницы")
