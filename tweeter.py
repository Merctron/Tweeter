import random

from flask import Flask
app = Flask(__name__)

adj_list = [
    'Fire-breathing',
    'Pretty',
    'Flying',
    'Beautifully scented',
    'Hideous',
    'Massive',
    'Bigly',
    'Little',
    'Pointy',
    'Blue',
    'Red',
    'Green',
    'Purple',
    'Angry',
    'Fast',
    'Super Duper',
    'Freckled'
]

obj_list = [
    'Gandhi',
    'Fake News',
    'Quantum Mechanics',
    'Dragon',
    'Turd',
    'Shithole',
    'Pikachu',
    'The Void',
    'Herpes',
    'Cancer',
    'London Bridge',
    'PS4',
    'Planking',
    'The distributed ledger',
    'Unagi',
    'Futurama',
    'Chemical reactions',
    'Geology',
    'Scientology',
    'Batman',
    'The touch down',
    'The meme economy',
    'Rocket ships',
    'Ponies',
    'Chimp',
    'Sphere'

]

antecedent_list = [
    'I am a stable genius. I invented/independently came up with {0}.',
    'I love {0}.',
    'I hate {0}.',
    'I dont know about {0}.'    
]

postcedent_list = [
    'It will change the way the world works.',
    'I will not be denied.',
    'He is a total and complete loser.',
    'In 25 years it will be what everyone eats.',
    'That is attractive.',
    'What is the big deal?',
    'No need to be scared'
]


def generate_tweet():
    adj_index = random.randint(0, len(adj_list) - 1)
    obj_index = random.randint(0, len(obj_list) - 1)
    ant_index = random.randint(0, len(antecedent_list) - 1)
    post_index = random.randint(0, len(postcedent_list) - 1)
    tweet_subj = "{} {}".format(adj_list[adj_index], obj_list[obj_index])
    tweet = "{} {}".format(antecedent_list[ant_index].format(tweet_subj), postcedent_list[post_index])
    return tweet



@app.route("/")
def hello():
    return "Hello World!"

@app.route("/tweet")
def tweet():
    return generate_tweet()

@app.route("/stats")
def stats():
    adj_len = len(adj_list)
    obj_len = len(obj_list)
    ant_len = len(antecedent_list)
    post_len = len(postcedent_list)

    stat_string_1 = " Tweeter Stats - Number of adjectives: {},".format(adj_len)
    stat_string_2 = " Number of objects: {},".format(obj_len)
    stat_string_3 = " Number of antecedents: {},".format(ant_len)
    stat_string_4 = " Number of postcedents: {}".format(post_len)

    return stat_string_1 + stat_string_2 + stat_string_3 + stat_string_4

# 

@app.route("/reversedtweet")
def reversedtweet():

    tweet = generate_tweet()

    reversed_tweet = tweet[::-1]

    return reversed_tweet

 #  Alternative to string reversal solution above
 #   for x in range(len(tweet)):
 #       reverse_x = len(tweet) - x - 1
 #       reversed_tweet = reversed_tweet + tweet[reverse_x]
 #  return reversed_tweet




if __name__ == "__main__":
    app.run()