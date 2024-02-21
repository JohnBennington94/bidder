# pylint: disable=too-many-ancestors
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import get_user_model

from .models import Property


# Login
class MyLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Email Address'
        self.fields['password'].label = 'Password'


class MyUserCreationForm(UserCreationForm):
    viewable_properties = forms.ModelMultipleChoiceField(
        queryset=Property.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name='Viewable Properties',
            is_stacked=False
        ),
        help_text='Select properties this user can view.'
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'surname', 'password', 'is_active', 'is_staff', 'viewable_properties')

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        if commit:
            user.save()
            if self.cleaned_data['viewable_properties']:
                user.viewable_properties.set(self.cleaned_data['viewable_properties'])
        return user


class MyUserChangeForm(UserChangeForm):
    viewable_properties = forms.ModelMultipleChoiceField(
        queryset=Property.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name='Viewable Properties',
            is_stacked=False
        ),
        help_text='Select properties this user can view.'
    )

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'surname', 'password', 'is_active', 'is_staff', 'viewable_properties')
