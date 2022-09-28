from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "user_name": "Your Name",
            "user_email": "Your Email",
            "text": "Your Comment"
        }
        widgets = {
            'user_name': forms.TextInput(attrs={'class': "form-control"}),
            'user_email': forms.TextInput(attrs={'class': "form-control"}),
            'text': forms.Textarea(attrs={'class': "form-control", "col":5, "row":5}),
        }
         
                