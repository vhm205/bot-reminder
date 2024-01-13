import telegram_bot
import random
from utils.logging import setup_logger

logger = setup_logger(__name__, True)

messages = (
    "Uống nước đi bạn gì ơi!",
    "Da của bạn đang khô queo lại đó, uống nước nào!",
    "Có thể bạn chưa biết, một ngụm nước có thể bạn trẻ tăng độ cute của bạn lên đó",
    "Tới giờ uống nước ròi bạn gì đó ơi",
    "Bạn cute ơi uống nước i!!",
    "Nếu bạn đang khó chịu vì tui nhắc quá nhìu... thì kệ bạn chứ tui sẽ khum dừng lại đâu",
    "Đứng lên đi lại cho khỏe khoắn nào bạn trẻ!",
    "Hít 5s, giữ 5s, thở 5s 💪"
)

stickers = (
    # "CAACAgUAAxkBAAEJxdhku6dZlaEMVCOQaxxg5ph0fVwRlwAC8ggAAse52FVFe-rjvHer6C8E",
    # "CAACAgUAAxkBAAEJxdxku6s816185LClmRoT7LJI7lIp8gAC7QgAAqh84FX-jP-3qYEqvC8E",
    # "CAACAgUAAxkBAAEJxeZku7ECHzaZxfGb2Y5tezpVRBr2rAAC5AkAAsPm4FX6C_eHYaJNfC8E",
    # "CAACAgUAAxkBAAEJ7TZkzgGSsFhRwRtAMY-9qAQaHoSjvwAClgkAAnjYcVZTDtTfvklieS8E",
    # "CAACAgUAAxkBAAEJ7ThkzgGjsC40g-ygiyfbBldCGr0JDwACvgcAAtvDcFZSPOS2l3vEdy8E",
    # "CAACAgUAAxkBAAEJ7TpkzgGs5ZxbuDQNYF7pqSXmpavnRAAC2gkAAs9DcFak0qJqpBKVHC8E",
    "CAACAgUAAxkBAAELK7tlorN74tU1pgkWrTrYrJyY-2s2wgACFgwAArXIEFXCAyLQtuwYxDQE",
    "CAACAgUAAxkBAAELK71lorOIuYo_OeAy97CH_f3FpFsJSwACmQsAAveHGFX0ItqhfljcwDQE",
    "CAACAgUAAxkBAAELK79lorOQoSutFEqpNg43CDgJsMeqpQACQQ0AArRzEFUI8O7UPyt7ZTQE",
    "CAACAgUAAxkBAAELK8FlorOao2vPyIgiC1pNzNlV7M0fIwACKgwAAj0vGFUN91-dmJaz9DQE",
    "CAACAgUAAxkBAAELK6llorL14vmBQsEQhgz5PIp9lflxcQACjg8AAqbAGVXL4VrWv0JrfjQE",
    "CAACAgUAAxkBAAELK6tlorMGecfrTNGouefmfpcHoTANWgACIg4AAiuAGVVz69vETg_cXzQE",
    "CAACAgUAAxkBAAELK61lorMQjX06TigER4pDlszevteVBQACKQ0AAtQ2EVWHjk9LkHxCwDQE",
    "CAACAgUAAxkBAAELK69lorMYaUb7AWPORKDQasTFeZ_YzwACMg0AAgkCEFXUPaPUGk_NRzQE",
    "CAACAgUAAxkBAAELK7FlorMhg3YbcSrpeVh68Y_b8dZvwwACrA0AAofwEFXx01g7c8wavzQE",
    "CAACAgUAAxkBAAELK7NlorMpOTM57mVzOqpCbITtJIZsJAACZAwAAmQmEVV-1G6pWiMSaDQE",
    "CAACAgUAAxkBAAELK7VlorMwYi-m9JTRX0drjq2TNukIBAAC3gwAAiUjGVWciajd9lqQPjQE",
    "CAACAgUAAxkBAAELK7dlorM4_vWcVarjxqbq_Y0Z0DRIzQACvg0AAq49GVWvaq2LcW--1jQE",
)


def remind_drink_water():
    message = random.choice(messages)
    sticker_id = random.choice(stickers)
    telegram_bot.send_sticker(sticker_id)
    telegram_bot.send_message(message)
    logger.info('Send reminder successfully!!')


if __name__ == '__main__':
    print('Scheduling for reminder...')
    remind_drink_water()

    # schedule.every(5).seconds.do(drink_water)

    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(drink_water())
