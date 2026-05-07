import random
from flask import Flask, render_template
from data import BIO, PROJECTS, SKILLS

app = Flask(__name__)

@app.route('/')
def index():
    # Home always shows the top 6 in order
    return render_template('index.html', bio=BIO, projects=PROJECTS[:6], skills=SKILLS)

@app.route('/archive')
def archive():
    # Jumbles the order for the Full Works page every time it loads
    jumbled_projects = list(PROJECTS)
    random.shuffle(jumbled_projects)
    return render_template('gallery.html', bio=BIO, projects=jumbled_projects)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port)