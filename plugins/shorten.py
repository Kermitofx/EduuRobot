
# Copyright (C) 2018-2019 Amano Team <contact@amanoteam.ml>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import requests

from config import bot


def shorten(msg):
    if msg.get('text'):
        if msg['text'].startswith('/shorten'):
            text = msg['text'][9:]
            if text == '':
                bot.sendMessage(msg['chat']['id'],
                                '*Uso:* `/shorten google.com` - _Encurta uma URL. Powered by _🇧🇷.ml', 'Markdown',
                                reply_to_message_id=msg['message_id'])
            else:
                r = requests.post('https://xn--f77h6a.ml/api/encurtar_url/', data=dict(url=text))
                bot.sendMessage(msg['chat']['id'], '*Resultado:* `{}`'.format(r.json()['link']), 'Markdown',
                                reply_to_message_id=msg['message_id'])
