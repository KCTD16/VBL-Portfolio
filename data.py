import os

basedir = os.path.abspath(os.path.dirname(__file__))
static_folder = os.path.join(basedir, 'static')

BIO = {
    "name": "VBL",
    "full_name": "Visuals By Laurine",
    "role": "Cinematographer & Creative Director",
    "location": "Manchester, UK",
    "experience": "8+ Years",
    "est_year": "2020", 
    "bio": "I create cinematic visuals and authentic imagery that turn moments into stories. Through photography and videography, my goal is to craft work that feels real, evokes emotion, and leaves a lasting impact.",
    "hero_video": "vblvid.mp4", 
    "content_photo": "content-photo.jpg", 
    "contact": {
        "email": "Laurinejagui@gmail.com",
        "instagram": "instagram.com/visualsbylaurine"
    }
}

# The main 6 (Manually checking extensions)
PROJECTS = [
    {"id": "1", "title": "KLAT x Alex Spencer", "video": "klat-project.MP4", "is_video": True, "tags": ["Cinema"]},
    {"id": "2", "title": "KLAT MAG", "video": "Noir-project.mp4", "is_video": True, "tags": ["Editorial"]},
    {"id": "3", "title": "STYLE 'N' SHOW EP2", "image": "aesthetic-new.jpg", "is_video": False, "tags": ["Film"]},
    {"id": "4", "title": "STYLE 'N' SHOW EP1", "video": "city-project.mp4", "is_video": True, "tags": ["Urban"]},
    {"id": "5", "title": "BLACK GIRL HAIR SHOP", "image": "shadow-form.JPG", "is_video": False, "tags": ["Editorial"]},
    {"id": "6", "title": "BLACK GIRL HAIR SHOP PT2", "image": "final-reel.JPG", "is_video": False, "tags": ["Brand"]}
]

# Smart Loader for work-1 to work-40
for i in range(1, 41):
    for ext in ['.mp4', '.MP4', '.jpg', '.JPG', '.png', '.PNG', '.webp', '.WEBP']:
        filename = f"work-{i}{ext}"
        if os.path.exists(os.path.join(static_folder, filename)):
            is_vid = ext.lower() == '.mp4'
            entry = {"id": f"w{i}", "title": f"Work {i}", "is_video": is_vid, "tags": ["Archive"]}
            if is_vid: entry["video"] = filename
            else: entry["image"] = filename
            PROJECTS.append(entry)
            break

SKILLS = [{"name": "Cinema", "level": 98}]