import os
import random
from flask import Flask, render_template
from data import BIO, PROJECTS, SKILLS

app = Flask(__name__)

@app.route('/')
def index():
    # Only Home Page (Curated Top 6)
    return render_template('index.html', bio=BIO, projects=PROJECTS[:6], skills=SKILLS)

@app.route('/archive')
def archive():
    # Full Works Page (All projects jumbled)
    jumbled = list(PROJECTS)
    random.shuffle(jumbled)
    return render_template('gallery.html', bio=BIO, projects=jumbled)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port)