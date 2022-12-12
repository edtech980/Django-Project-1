from django import forms


class CreateNewPost(forms.Form):
    title = forms.CharField(label="Title", max_length=50)
    #post = forms.CharField(label="Post", max_length=1000)
    #post1 = forms.CharField(label="Title2", max_length=5000)
    post = forms.CharField(widget=forms.Textarea(
        attrs={'name': 'body', 'rows': 5, 'cols': 25}))
    #post2 = forms.TextInput()
    #posts = forms.Textarea()
