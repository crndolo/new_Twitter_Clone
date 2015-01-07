from django.contrib import admin
from tweet.models import Tweet, Retweet, Reply

# Register your models here.

admin.site.register(Tweet)
admin.site.register(Retweet)
admin.site.register(Reply)