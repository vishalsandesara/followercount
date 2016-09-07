#!/usr/bin/env python

import subprocess
import time
import tweepy

ACCESS_TOKEN = ''
ACCESS_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

COUNT_FILE = '/Users/vsandesara/work/counts/countFile'
SCREEN_NAME = '_lab41'


def say(something):
    subprocess.call(['/usr/bin/say', something])

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

newcount = 0
loops = 0
for page in tweepy.Cursor(api.followers_ids,
                          screen_name=SCREEN_NAME,
                          cursor=-1,
                          count=50000).pages():

    newcount += len(page)
    loops += 1
    if loops > 3:
        time.sleep(20)

b = open(COUNT_FILE, 'r')
oldcount = int(b.readline())
b.close()

something = 'currently there are {0} of followers'.format(newcount)
say(something)

if newcount > oldcount:
    a = open(COUNT_FILE, 'w')
    a.write('{0}'.format(newcount))
    diff = newcount - oldcount
    follower = 'follower'

    if diff > 1:
        follower += 's'

    something = '{0} new twitter {1} since last call'.format(diff, follower)
    say(something)
   
