from twython import TwythonStreamer

import sys
import time

import scrollphat

from auth_robotgimse import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

scrollphat.set_brightness(2)
scrollphat.set_rotate(True)


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print(data['text'])
            #tweet = data['text']
            scrollphat.write_string(data['text'])
            length = scrollphat.buffer_len()

            for i in range(length):
                try:
                    scrollphat.scroll()
                    time.sleep(0.1)
                except KeyboardInterrupt:
                    scrollphat.clear()
                    sys.exit(-1)
                    
stream = MyStreamer(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

stream.statuses.filter(track='@potus')
