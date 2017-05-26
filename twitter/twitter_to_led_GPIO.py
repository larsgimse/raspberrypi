import time
from time import sleep
from TwitterAPI import TwitterAPI
import RPi.GPIO as GPIO       ## Import GPIO library

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)      ## Use board pin numbering
GPIO.setup(12, GPIO.OUT)      ## Setup GPIO Pin 11 to OUT


stringToTrack = "#trump"

from auth_robotgimse import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


while True:
    api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)
    r = api.request('statuses/filter', {'track':stringToTrack})
    for item in r.get_iterator():
      if 'text' in item:
#        print item['user']['screen_name'].encode('utf-8') + ' tweeted: ' + item['text'].encode('utf-8')# Print screen name and the tweet text
        tweet = item['text'].encode('utf-8')
#        print tweet.split()

        if '#nato' in tweet.split():
            print item['user']['screen_name'].encode('utf-8') + ' tweeted: ' + item['text'].encode('utf-8')
            print 'Blink LED'        
            GPIO.output(12,True)  ## Turn on Led
            time.sleep(1)         ## Wait for one second
            GPIO.output(12,False) ## Turn off Led
            time.sleep(1)         ## Wait for one second
            print '---'
