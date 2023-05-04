from django import forms

class CheckboxForm(forms.Form):
    title = forms.CharField(max_length=100)
    rm_null_attr = forms.BooleanField(required=False)
    cld_words = forms.BooleanField(required=False)
    lang_dist = forms.BooleanField(required=False)
    data_dist = forms.BooleanField(required=False)
    stance_dist = forms.BooleanField(required=False)
    local_dist = forms.BooleanField(required=False)
    topic_detection = forms.BooleanField(required=False)