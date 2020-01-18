from bot import TelegramChatBot

bot = TelegramChatBot("config.cfg")


def make_reply(msg):
    reply = "Ok"
    return reply


def greetings(msg):
    reply = "Olá! Seja bem vindo ao bot de pedidos!\n Poderia informar seu nome para eu anotar seu pedido?"
    return reply


def adress_request(msg):
    reply = "Agora que já sei o seu nome, gostaria de saber qual o endereço de entrega"
    return reply

def order_request(msg):
    reply = "tudo certo até agora! Qual o seu pedido?"
    return reply


def new_order(msg):
    global complete_order
    reply = "um novo pedido chegou:\n nome: {}\n endereço: {}\n pedido: {}".format(complete_order[0],complete_order[1],complete_order[2])
    return reply


update_id = None

complete_order = [] #name, adress, order

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
            reply = greetings(message)
            bot.send_message(reply, from_)


    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = item["message"]["text"]
                complete_order.append(message)
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = adress_request(message)
            bot.send_message(reply, from_)


    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = item["message"]["text"]
                complete_order.append(message)
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = order_request(message)
            bot.send_message(reply, from_)

    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = item["message"]["text"]
                complete_order.append(message)
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, from_)


    message = complete_order
    reply = new_order(message)
    bot.send_group_message(reply, 351110135)


'''
send greeting message to client
receive name

send adress request to client
receive adress

send order request to client
receive order

send confirmation message
if it is not rigth: correct flaw
if it is right:
    send confirmation message to client
    send (name, adress, order) to central



'''