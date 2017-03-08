from django import forms
from ginthusiasm.models import Article

class ArticleFilter(forms.ModelForm):

    CATHERINE = 'catherine'
    ROZZ = 'name'
    MATT = '-name'
    ROBERT = 'price'
    ALICE = '-price'
'

    ORDER_BY_CHOICES = (

        (CATHERINE, 'Catherine'),
        (ROZZ, 'Rozz'),
        (MATT, 'Matt'),
        (ROBERT, 'Robert'),
        (ALICE, 'Alice'),
    )

    authors = forms.ChoiceField(choices=AUTHOR_CHOICES)
