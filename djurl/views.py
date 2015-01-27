from django.shortcuts import render_to_response, get_object_or_404
import random
import string
import json
from djurl.models import Urls
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.core.context_processors import csrf


def index(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('djurl/index.html', c)


def redirectOriginal(request, short_id):
    # get object, if not found return 404 error
    url = get_object_or_404(Urls, pk=short_id)
    url.count += 1
    url.save()
    return HttpResponseRedirect(url.httpurl)


def shortenUrl(request):
    url = request.POST.get("url", '')
    if not (url == ''):
        short_id = getShortCode()
        b = Urls(httpurl=url, short_id=short_id)
        b.save()

        response_data = {}
        response_data['url'] = settings.SITE_URL + "/" + short_id
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    return HttpResponse(json.dumps({"error": "error occurs"}),
                        content_type="application/json")


def getShortCode():
    length = 6
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    # if the randomly generated short_id is used then generate next
    while True:
        short_id = ''.join(random.choice(char) for x in range(length))
        try:
            temp = Urls.objects.get(pk=short_id)
        except:
            return short_id
