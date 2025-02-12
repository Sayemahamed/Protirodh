from django import forms
from .models import CrimeReport, Comment

class CrimeReportForm(forms.ModelForm):
    class Meta:
        model = CrimeReport
        fields = ('title', 'description', 'division', 'district', 'image', 'video', 'crime_time')
    
    def clean(self):
        cleaned_data = super().clean()
        image = cleaned_data.get("image")
        video = cleaned_data.get("video")
        if not image and not video:
            raise forms.ValidationError("You must upload at least one image (video is optional).")
        return cleaned_data

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text', 'proof_image', 'proof_video')
    
    def clean(self):
        cleaned_data = super().clean()
        proof_image = cleaned_data.get("proof_image")
        proof_video = cleaned_data.get("proof_video")
        if not proof_image and not proof_video:
            raise forms.ValidationError("You must attach proof (image or video).")
        return cleaned_data