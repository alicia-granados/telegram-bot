import telepot
import requests
import sys

# Configuration
secret_key = ''
user_id = ''


# Sends  a new message to the user
def send_message(bot_message):
    send_text = 'https://api.telegram.org/bot' + secret_key + '/sendMessage?chat_id=' + user_id + '&parse_mode=Markdown&text=' + bot_message
    # API request
    response = requests.get(send_text)
    return response.json()
    

if __name__ == "__main__":
    message = sys.argv[1]
    send_message(message)
    print("El mensaje: \"{}\" ha sido enviado con éxito".format(message))