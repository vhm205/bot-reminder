import schedule
import time
import random
import telegram_bot
# import asyncio

messages = (
    "Uống nước đi bạn gì ơi!",
    "Da của bạn đang khô queo lại đó, uống nước nào",
    "Có thể bạn chưa biết, một ngụm nước có thể tăng độ cute của bạn lên đó",
    "Tới giờ húp nước gòi ròi bạn gì đó ơi",
    "Bật nắp ly nước, sảng khoái cực đỉnh, uống ngay nào!"
)

stickers = (
    "CAACAgUAAxkBAAEJxdhku6dZlaEMVCOQaxxg5ph0fVwRlwAC8ggAAse52FVFe-rjvHer6C8E",
    "CAACAgUAAxkBAAEJxdxku6s816185LClmRoT7LJI7lIp8gAC7QgAAqh84FX-jP-3qYEqvC8E",
    "CAACAgUAAxkBAAEJxeZku7ECHzaZxfGb2Y5tezpVRBr2rAAC5AkAAsPm4FX6C_eHYaJNfC8E"
)


def drink_water():
    message = random.choice(messages)
    sticker_id = random.choice(stickers)
    telegram_bot.send_sticker(sticker_id)
    telegram_bot.send_message(message)


schedule.every(5).seconds.do(drink_water)
print('Scheduling for reminder...')

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(drink_water())
