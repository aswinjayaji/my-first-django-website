from django import forms
from .models import Trial
# form to save files n html itself kinda backend


class ProductForm(forms.ModelForm):
    title = forms.CharField(
        label='', widget=forms.TextInput(
            attrs={
                "placeholder": "title"
            }
        )
    )
    description = forms.CharField(
        label='', required=False, widget=forms.Textarea(
            attrs={
                "placeholder": "Your Description",
                "class":"new-class-name-two",
                "id":"",
                "rows":15,
                "cols":35,   #for columns
            }
        )
    )
    price = forms.DecimalField(label='', widget=forms.TextInput(
            attrs={
                "placeholder": "price"
            }
        ))
    class Meta:
        model = Trial
        fields = [
            'title', 'description', 'price'
        ]

    def clean_title(self,*args,**kwargs):  #def clean_<whatever to clean>
        title=self.cleaned_data.get("title")
        if  not "Zephyr" in title:
            raise forms.ValidationError("This is not a valid Title")
        
class RawProductForm(forms.Form):
    title = forms.CharField(
        label='Title', widget=forms.TextInput(
            attrs={
                "placeholder": "Your Title"
            }
        )
    )
    description = forms.CharField(
        label='Description', required=False, widget=forms.Textarea(
            attrs={
                "placeholder": "Your Description",
                "class":"new-class-name-two",
                "id":"",
                "rows":1,
                "cols":35,   #for columns
            }
        )
    )
    price = forms.DecimalField(label='Price', widget=forms.TextInput(
            attrs={
                "placeholder": "price"
            }
        ))
    # arguments are on form fields in djangosite
    # find on widgets
