
import random
from chat import chat_logic

def handle_response(message) -> str:
    p_message = message.lower()
    return chat_logic(message);
    
    if p_message == 'hello':
        return 'Hey there!'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return "`Service Currently unaviable call 100`"
    return "`I do not understand  you but soon I will`"
    #  return 'Yeah, I don\'t know. Try typing "!help".'