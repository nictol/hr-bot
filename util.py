from datetime import datetime

# TODO: add loging
def send_answer(bot, chat_id, answer_file, log_str):
    bot.send_message(chat_id, open(answer_file, encoding='utf-8').read())
    print('(' + log_str + ')\t' + str(chat_id) + ' ' + get_current_time())


def get_current_time():
    return datetime.now().strftime("%H:%M:%S")
