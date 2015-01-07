from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from tweet.models import Tweet

# Create your views here.

def tweets(request):
	output = Tweet.objects.order_by('-date_created')[:5]
	return HttpResponse(output)