from channels import Group
import json
# import word2vec
import helpers
from .helpers import analogy

def ws_connect(message):
    Group('users').add(message.reply_channel)
    # ^keep track of the user so we can send data to them
    Group('users').send({
        'text': json.dumps({
            'connected': True
        })
    })
    print(dir(message))
    print("made a friend, their name is " + str(message.reply_channel))

def ws_disconnect(message):
    Group('users').discard(message.reply_channel)
    print(message.reply_channel)
    print("bye bye " + str(message.reply_channel))

def ws_receive(message):
    # Group('users').discard(message.reply_channel)
    print("received message", message.content["text"])

    try:

        analogy_object = json.loads(message.content["text"])

        result = analogy(analogy_object["positive_word_list"], analogy_object["negative_word_list"])

        message.reply_channel.send({
            'text': json.dumps(result)
        })
    except:
        message.reply_channel.send({
            'text': json.dumps({
                'error': 'there was an error parsing your data'
            })
        })






