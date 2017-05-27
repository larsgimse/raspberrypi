import time
from time import sleep
from TwitterAPI import TwitterAPI
import RPi.GPIO as GPIO       ## Import GPIO library

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)      ## Use board pin numbering
GPIO.setup(12, GPIO.OUT)      ## Setup GPIO Pin 11 to OUT
GPIO.setup(11, GPIO.OUT)
count = 1
countLed = 1

stringToTrack = "@potus"

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

        if '@potus' in tweet.split():
#            print item['user']['screen_name'].encode('utf-8') + ' tweeted: ' + item['text'].encode('utf-8')
#            print 'Blink LED'
            print tweet
            GPIO.output(12,True)  ## Turn on Led
            time.sleep(0.5)         ## Wait for one second
            GPIO.output(12,False) ## Turn off Led
            time.sleep(0.5)         ## Wait for one second
            print '---'
            print 'Tweets: ', count
            print 'countLed: ', countLed
            print '---'
            count = count + 1
            countLed = countLed + 1
            if countLed > 5:
                for x in range(0, 19):
                    GPIO.output(11,True)
                    time.sleep(0.1)
                    GPIO.output(11,False)
                    time.sleep(0.1)
                countLed = 1
