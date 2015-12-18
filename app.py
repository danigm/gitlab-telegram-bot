import json
from flask import Flask
from flask import request
from flask import jsonify
from bot import Bot
app = Flask(__name__)


AUTHMSG = 'XXXXXXXXXXXXXXXXXXXXXXX'


class GitlabBot(Bot):
    def __init__(self):
        super(GitlabBot, self).__init__()
        self.chats = {}
        try:
            chats = open('chats', 'r').read()
            self.chats = json.loads(chats)
        except:
            open('chats', 'w').write(json.dumps(self.chats))

    def text_recv(self, txt, chatid):
        ''' registering chats '''
        if txt.strip() == AUTHMSG:
            self.reply(chatid, "OK")
            self.chats[chatid] = True
            open('chats', 'w').write(json.dumps(self.chats))
        elif txt.strip() == 'shutupbot':
            del self.chats[chatid]
            self.reply(chatid, "OK, take it easy\nbye.")
            open('chats', 'w').write(json.dumps(self.chats))
        else:
            self.reply(chatid, "I won't talk to you.")

    def send_to_all(self, msg):
        for c in self.chats:
            self.reply(c, msg)


b = GitlabBot()


@app.route("/", methods=['GET', 'POST'])
def webhook():
    data = request.json
    ok = data['object_kind']
    repo = data['repository']['homepage']
    name = data['repository']['name']
    try:
        user = data['user_name']
    except:
        user = data['user']['username']

    msg = '@%s: new %s in %s\n%s' % (user, ok, name, repo)
    b.send_to_all(msg)

    return jsonify({'status': 'ok'})


if __name__ == "__main__":
    b.run_threaded()
    app.run(host='0.0.0.0', port=10111)
