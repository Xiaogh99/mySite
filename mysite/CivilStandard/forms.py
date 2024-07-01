from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=100, label="标题")
    content = forms.CharField(max_length=100, label="编号")
    date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}), label="日期")
    # content = forms.CharField(widget=forms.Textarea)
