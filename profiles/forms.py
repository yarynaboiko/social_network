from django import forms

from profiles.models import Profile


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'surname', 'image', 'cover', 'city', 'country', 'status', 'type')

    # help_texts = {
    #     'username': None,
    #     'password1': None,
    #     'password2': None,
    # }

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control my-2'})
            if self.errors.get(field_name):
                field.widget.attrs.update({'class': 'form-control my-2 is-invalid'})
