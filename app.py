from flask import Flask, render_template
import random

app = Flask(__name__)

def load_words():
    with open("words.txt", "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]

words = load_words()

@app.route("/")
def home():
    word = random.choice(words)
    return render_template("index.html", word=word)


if __name__ == "__main__":
    app.run()