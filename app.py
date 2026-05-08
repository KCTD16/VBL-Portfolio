import os
import random
from flask import Flask, render_template, url_for
from data import BIO, PROJECTS, SKILLS

app = Flask(__name__)

# This is the "Secret Sauce" that fixed your Home Page images
@app.context_processor
def inject_methods():
    def get_url(filename):
        if not filename: return ""
        if filename.startswith('http'): return filename
        return url_for('static', filename=filename)
    return dict(get_url=get_url)

@app.route('/')
def index():
    # Only Home Page (Perfect as is)
    return render_template('index.html', bio=BIO, projects=PROJECTS[:6], skills=SKILLS)

@app.route('/archive')
def archive():
    # Full Works Page logic
    jumbled = list(PROJECTS)
    random.shuffle(jumbled)
    return render_template('gallery.html', bio=BIO, projects=jumbled)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port)