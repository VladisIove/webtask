from django import forms 


class SearchForm( forms.Form ):
	body = forms.CharField(max_length=120, label='')


class CommentForm( forms.Form ):
	body = forms.CharField(max_length=240, label='')