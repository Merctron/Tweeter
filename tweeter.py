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
	'It will change the way the world works.'
	'I will not be denied.'
	'He is a total and complete loser.'
	'In 25 years it will be what everyone eats.'
	'That is attractive.'
	'What is the big deal?'
	'No need to be scared'
]


@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()