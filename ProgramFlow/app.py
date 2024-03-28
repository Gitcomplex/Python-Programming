from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    answer = random.randint(1, 10)
    tries = 0
    guesses = []

    while True:
        guess = int(request.form['guess'])
        tries += 1
        guesses.append(guess)

        if guess < answer:
            message = "Too low! Guess higher."
        elif guess > answer:
            message = "Too high! Guess lower."
        else:
            message = "Congratulations! You guessed it right!"
            break

    return render_template('result.html', message=message, tries=tries, guesses=guesses)

if __name__ == '__main__':
    app.run(debug=True)
