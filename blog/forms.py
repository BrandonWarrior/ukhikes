from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """
    Form for creating or editing a blog post.
    """

    class Meta:
        model = Post
        fields = ('title', 'content', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean(self):
        """
        Validates that both the title and content are provided.
        """
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if not title:
            self.add_error('title', 'A title is required.')
        if not content:
            self.add_error('content', 'Content is required.')
        return cleaned_data


class CommentForm(forms.ModelForm):
    """
    Form for creating or editing a comment.
    """
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'required': False
        }),
        required=True,
        error_messages={'required': 'A comment is required.'}
    )

    class Meta:
        model = Comment
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        """
        Initialise CommentForm and remove 'required'
        attribute from its widget.
        """
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.pop('required', None)

    def clean_content(self):
        """
        Validates that the comment content is not empty.
        """
        content = self.cleaned_data.get('content')
        if not content:
            raise forms.ValidationError("A comment is required.")
        return content
