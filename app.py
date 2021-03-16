from flask import Flask, render_template
import random
app = Flask(__name__)
images = [
"https://media3.giphy.com/media/l2QE73aOjxO1fkd6E/giphy.gif",
"https://media.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif",
"https://media.giphy.com/media/du3J3cXyzhj75IOgvA/giphy.gif",
"https://media.giphy.com/media/kH6CqYiquZawmU1HI6/giphy.gif",
"https://media.giphy.com/media/d8iBSenW36aQE0isva/giphy.gif",
"https://media.giphy.com/media/xULW8PLGQwyZNaw68U/giphy-downsized-large.gif",
"https://media.giphy.com/media/eYilisUwipOEM/giphy.gif",
"https://media.giphy.com/media/DBPEwTU6klcac/giphy.gif",
"https://media.giphy.com/media/TaBJhZTUALPlm/giphy.gif"
]
@app.route('/')
def index():
    url= random.choice(images)
    return render_template('index.html', url=url)
if __name__ == "__main__":
    app.run(host="0.0.0.0")
