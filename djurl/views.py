import random
import string
import json
from djurl.models import Url
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.template.context_processors import csrf
from django.shortcuts import render, get_object_or_404


def index(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'djurl/index.html', c)


def redirect_original(request, short_id):
    # get object, if not found return 404 error
    url = get_object_or_404(Url, pk=short_id)
    url.count += 1
    url.save()
    return HttpResponseRedirect(url.httpurl)


def shorten_url(request):
    url = request.POST.get("url", '')
    if not (url == ''):
        try:
            url_present = Url.objects.get(httpurl=url)
            short_id = url_present.short_id
        except (Url.DoesNotExist):
            short_id = get_short_code()
        b = Url(httpurl=url, short_id=short_id)
        b.save()

        response_data = {}
        response_data['url'] = settings.SITE_URL + "/" + short_id
        return HttpResponse(json.dumps(response_data),
                            content_type="application/json")
    return HttpResponse(json.dumps({"error": "error occurs"}),
                        content_type="application/json")


def get_short_code():
    length = 6
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    # if the randomly generated short_id is used then generate next
    while True:
        short_id = ''.join(random.choice(char) for x in range(length))
        try:
            temp = Url.objects.get(pk=short_id)
            return temp
        except:
            return short_id
