#!/usr/bin/env python

import time
import requests
from threading import Thread


class Bot:
    def __init__(self):
        try:
            self.token = open('token').read().split()[0]
        except:
            raise Exception("The token file is invalid")

        self.api = 'https://api.telegram.org/bot%s/' % self.token
        try:
            self.offset = int(open('offset').read().split()[0])
        except:
            self.offset = 0
        self.me = self.botq('getMe')
        self.running = False

    def botq(self, method, params=None):
        url = self.api + method
        params = params if params else {}
        return requests.post(url, params).json()

    def msg_recv(self, msg):
        ''' method to override '''
        pass

    def text_recv(self, txt, chatid):
        ''' method to override '''
        pass

    def updates(self):
        data = {'offset': self.offset}
        r = self.botq('getUpdates', data)
        for up in r['result']:
            self.msg_recv(up['message'])
            try:
                txt = up['message']['text']
                self.text_recv(txt, self.get_to_from_msg(up['message']))
            except:
                pass
            self.offset = up['update_id']
            self.offset += 1
        open('offset', 'w').write('%s' % self.offset)

    def get_to_from_msg(self, msg):
        to = ''
        try:
            to = msg['chat']['id']
        except:
            to = ''
        return to

    def reply(self, to, msg):
        if type(to) not in [int, str]:
            to = self.get_to_from_msg(to)
        resp = self.botq('sendMessage', {'chat_id': to, 'text': msg})
        return resp

    def run(self):
        self.running = True
        while self.running:
            self.updates()
            time.sleep(1)

    def run_threaded(self):
        t = Thread(target=self.run)
        t.start()

    def stop(self):
        self.running = False


if __name__ == '__main__':
    bot = Bot()
    bot.run()
