import os

# Absolute path setup for Render stability
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

# Your 6 main featured projects (Updated to .jpg)
PROJECTS = [
    {"id": "1", "title": "KLAT x Alex Spencer", "video": "klat-project.mp4", "is_video": True, "tags": ["Cinema"]},
    {"id": "2", "title": "KLAT MAG", "video": "noir-project.mp4", "is_video": True, "tags": ["Editorial"]},
    {"id": "3", "title": "STYLE 'N' SHOW EP2 STILL", "image": "aesthetic-new.jpg", "is_video": False, "tags": ["Film"]},
    {"id": "4", "title": "STYLE 'N' SHOW EP1", "video": "city-project.mp4", "is_video": True, "tags": ["Urban"]},
    {"id": "5", "title": "BLACK GIRL HAIR SHOP STILL", "image": "shadow-form.jpg", "is_video": False, "tags": ["Editorial"]},
    {"id": "6", "title": "BLACK GIRL HAIR SHOP PT2", "image": "final-reel.jpg", "is_video": False, "tags": ["Brand"]}
]

# Universal Smart Loader (Checks for work-1.mp4 through work-40.jpg)
for i in range(1, 41):
    v_name = f"work-{i}.mp4"
    if os.path.exists(os.path.join(static_folder, v_name)):
        PROJECTS.append({"id": f"v{i}", "title": f"Work {i}", "video": v_name, "is_video": True, "tags": ["Motion"]})
        continue
    
    # Checking for .jpg extension
    j_name = f"work-{i}.jpg"
    if os.path.exists(os.path.join(static_folder, j_name)):
        PROJECTS.append({"id": f"j{i}", "title": f"Work {i}", "image": j_name, "is_video": False, "tags": ["Project"]})

SKILLS = [{"name": "Cinema", "level": 98}]