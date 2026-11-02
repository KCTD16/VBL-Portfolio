import os
import random
from flask import Flask, render_template, url_for, request
from flask_limiter import Limiter
from flask_talisman import Talisman
from data import BIO, PROJECTS, SKILLS


def get_remote_address():
    return request.remote_addr

app = Flask(__name__)

# 1. ADD SECURITY HEADERS (Flask-Talisman)
# We configure the Content Security Policy (CSP) to only allow your specific media sources.
csp = {
    'default-src': [
        '\'self\'',
        'https://res.cloudinary.com',
        'https://images.unsplash.com',
        'https://cdn.tailwindcss.com',
        'https://cdnjs.cloudflare.com',
        'https://fonts.googleapis.com',
        'https://fonts.gstatic.com',
        'https://grainy-gradients.vercel.app'
    ],
    # Allowing unsafe-inline because Tailwind CDN and your custom scripts require it
    'script-src': ['\'self\'', '\'unsafe-inline\'', '\'unsafe-eval\'', 'https://cdn.tailwindcss.com'],
    'style-src': ['\'self\'', '\'unsafe-inline\'', 'https://cdnjs.cloudflare.com', 'https://fonts.googleapis.com'],
    'img-src': ['\'self\'', 'data:', 'https://res.cloudinary.com', 'https://images.unsplash.com', 'https://via.placeholder.com'],
    'media-src': ['\'self\'', 'https://res.cloudinary.com']
}

# Only force HTTPS if we are running in the production environment (Render)
is_production = os.environ.get("RENDER") is not None
Talisman(app, content_security_policy=csp, force_https=is_production)

# 2. ADD RATE LIMITING (Protects against bots and scrapers)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["500 per day", "100 per hour"],
    storage_uri="memory://"
)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 31536000 

@app.context_processor
def inject_methods():
    def get_url(filename):
        if not filename: return ""
        if filename.startswith('http'): return filename
        return url_for('static', filename=filename)
    return dict(get_url=get_url)

@app.route('/')
@limiter.limit("30 per minute") # Strict limit for the home page
def index():
    return render_template('index.html', bio=BIO, projects=PROJECTS[:6], skills=SKILLS)

@app.route('/archive')
@limiter.limit("30 per minute") # Strict limit for the archive page
def archive():
    jumbled = list(PROJECTS)
    random.shuffle(jumbled)
    return render_template('gallery.html', bio=BIO, projects=jumbled)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', bio=BIO), 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    # 3. TURN OFF DEBUG MODE
    app.run(host='0.0.0.0', port=port, debug=False)