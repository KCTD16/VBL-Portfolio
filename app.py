import os
import random
from flask import Flask, render_template
from data import BIO, PROJECTS, SKILLS

app = Flask(__name__)

@app.route('/')
def index():
    # Shows the first 6 projects on the home page
    return render_template('index.html', bio=BIO, projects=PROJECTS[:6], skills=SKILLS)

@app.route('/archive')
def archive():
    # Jumbles the projects for the Full Works page
    jumbled = list(PROJECTS)
    random.shuffle(jumbled)
    return render_template('gallery.html', bio=BIO, projects=jumbled)

if __name__ == '__main__':
    # Mac/Render compatible port logic
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port)