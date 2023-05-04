from django.shortcuts import render
from rest_framework.decorators import api_view
from myapp.utils import process_data, getAllowedSubjects
from myapp.forms import CheckboxForm
import json
from django.http import HttpResponse, JsonResponse


@api_view(['GET', 'POST'])
def index(request):
    print("\n\n\n")
    if request.method == 'POST':
        print("***********************************************")
        form_data = json.loads(request.body.decode('utf-8'))
        print(form_data)
        form = CheckboxForm(form_data)
        if form.is_valid():
            title = form.cleaned_data['title']
            rm_null_attr = form.cleaned_data['rm_null_attr']
            cld_words = form.cleaned_data['cld_words']
            lang_dist = form.cleaned_data['lang_dist']
            data_dist = form.cleaned_data['data_dist']
            stance_dist = form.cleaned_data['stance_dist']
            local_dist = form.cleaned_data['local_dist']
            topic_detection = form.cleaned_data['topic_detection']
            print("form post succeeded")
            print(title, rm_null_attr, cld_words, lang_dist, data_dist, stance_dist, local_dist, topic_detection)
            images = process_data(title, rm_null_attr, cld_words, lang_dist, data_dist, stance_dist, local_dist)
            response_data = {'images':images}

            print("\n\n\n")
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            print("form post failed")

            print("\n\n\n")
            return HttpResponse(json.dumps({"error": "failed"}), content_type="application/json")
    return render(request, 'index.html')


@api_view(['GET', 'POST'])
def get_subjects(request):
    return JsonResponse(getAllowedSubjects(), safe=False)
