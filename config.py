import amanobot
import amanobot.aio
import asyncio


token = "901147654:AAGcf3IQtuh9CXllVpO0f14jC8fU7fhPCnQ"


loop = asyncio.get_event_loop()  # Do not change this


bot = amanobot.aio.Bot(token)
na_bot = amanobot.Bot(token)


me = loop.run_until_complete(bot.getMe())
bot_username = me['username']
bot_id = me['id']


keys = dict(
    here = {'app_id': 'key_id_here', 'app_code': 'key_code_here'},  #You can get a key at https://here.com
    yandex = 'key_here',                                            #You can get a key at https://tech.yandex.com/translate
    giphy = 'key_here',                                             #You can get a key at https://developers.giphy.com
)

git_repo = ('https://github.com/AmanoTeam/EduuRobot', 'master') #Repository where your bot is in

max_time = 60

version = open('version.txt').read()

logs = 1223998042

backups_chat = 1223998042  # Put a 0, False or None to disable.
backup_hours = ['00:00', '12:00']

sudoers = [
    684842099
]

enabled_plugins = [
    'processmsg',
    'start',
    'rules',
    'shorten',
    'sed',
    'kibe',
    'translate',
    'rextester',
    'inlines',
    'welcome',
    'admins',
    'warns',
    'prints',
    'pypi',
    'weather',
    'youtube',
    'ping',
    'gif',
    'git',
    'reddit',
    'coub',
    'sudos',
    'ids',
    'ip',
    'jsondump',
    'dice',
    'misc',
    'antipedro'
]
