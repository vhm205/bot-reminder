import json
import requests
import os
import env
from utils.custom_logging import get_logger

env.set_default()
logger = get_logger(__name__)

telegram_api = 'https://api.telegram.org'
telegram_channel = os.environ['CHANNEL_NAME']
telegram_chat_id = os.environ['BOT_CHAT_ID']
telegram_token = os.environ['BOT_TOKEN']
telegram_bot = f'bot{telegram_chat_id}:{telegram_token}'


def send_message(text=''):
    try:
        response = requests.get('%s/%s/%s' % (telegram_api, telegram_bot, 'sendMessage'),
                                params={'chat_id': telegram_channel, 'text': text})
        return json.loads(response.content)
    except Exception as e:
        logger.error(e)


def send_sticker(sticker_id=''):
    try:
        response = requests.get('%s/%s/%s' % (telegram_api, telegram_bot, 'sendSticker'),
                                params={'chat_id': telegram_channel, 'sticker': sticker_id})
        return json.loads(response.content)
    except Exception as e:
        logger.error(e)
