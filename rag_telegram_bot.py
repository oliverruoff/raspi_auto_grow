import telebot
from dotenv import load_dotenv
import os


connected_chat_ids = []


def listener(tb, messages):
    """
    This function is called when a message arrives
    """
    global connected_chat_ids
    for m in messages:
        chatid = m.chat.id
        if m.content_type == 'text':
            text = m.text
            if text == '/connect':
                connected_chat_ids.append(chatid)
                # deleting duplicates
                connected_chat_ids = lsit(set(connected_chat_ids))
                tb.send_message(
                    chatid,
                    'Raspi Smart Grow Bot connected with chatid: ' +
                    str(chatid))
            else:
                tb.send_message(chatid, 'Command not recognized!')


def send_message(message):
    """Sends a text message to all connected chatids.
    Returns the list of chatids, the message was sent to.

    Arguments:
        message {String} -- A text that will be send to all connected chatids

    Returns:
        [int] -- List of chatids
    """
    for chatid in connected_chat_ids:
        tb.send_message(chatid, message)
    return connected_chat_ids


def start_tb_listener():
    load_dotenv()
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    tb = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
    tb.set_update_listener(listener)  # register listener
    tb.polling()
    # Use none_stop flag let polling will
    #  not stop when get new message occur error.
    tb.polling(none_stop=True)
    # Interval setup. Sleep 3 secs between request new message.
    tb.polling(interval=3)
    return tb
