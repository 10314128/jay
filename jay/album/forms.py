from django import forms
from album.models import Category, Page

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, label='專輯名稱', help_text='請輸入專輯名稱')
    
    class Meta:
        model = Category
        fields = ('name', )
        
class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, label='專輯名稱', help_text='請輸入專輯名稱')
    url = forms.URLField(max_length=128, label='網址', help_text='請輸入頁面網址')
    
    class Meta:
        model = Page
        exclude = ('category', 'views')