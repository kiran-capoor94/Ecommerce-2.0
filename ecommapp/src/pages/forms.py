from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Full Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Message'}))

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if not "gmail.com" in email:
    #         raise forms.ValidationError("Email has to be GMAIL!")
    #     return email

    # def clean_content(self):
    #     raise forms.ValidationError("Content is worng", code='invalid')