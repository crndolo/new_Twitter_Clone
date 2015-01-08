from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader, Context
from django.template.loader import get_template
from tweet.models import Tweet

# Create your views here.

def tweets(request):
    output = Tweet.objects.order_by('-date_created')[:5]
    return HttpResponse(output)

def latest_tweets(request):
	#name = "Ndolo"
	#temp = get_template('tweets.html')
	#html = temp.render(Context({'name':name}))
	#return HttpResponse(html)
	#name = "Ndolo"
	#return render_to_response('tweets.html', {'name': name})
	return render_to_response('tweets.html', {'tweets': Tweet.objects.all()})
