from bot import TelegramChatBot

bot = TelegramChatBot("config.cfg")


def make_reply(msg):
    reply = "Ok"
    return reply


update_id = None

while True:

    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = item["message"]["text"]
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, from_)
            bot.send_group_message(item["message"]["text"], 351110135)
