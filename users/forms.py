from django import forms
from .models import Profile, Experience, Education, Contact

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_image',)

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ('title', 'company', 'location', 'start_date', 'end_date', 'description')

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ('degree', 'institution', 'location', 'start_date', 'end_date')

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('address', 'email', 'linkedin', 'twitter')
