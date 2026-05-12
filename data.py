import os

BIO = {
    "name": "VBL",
    "full_name": "Visuals By Laurine",
    "role": "Cinematographer & Creative Director",
    "location": "Manchester, UK",
    "experience": "8+ Years",
    "est_year": "2020", 
    "bio": "I create cinematic visuals and authentic imagery that turn moments into stories. Through photography and videography, my goal is to craft work that feels real, evokes emotion, and leaves a lasting impact.",
    "hero_video": "https://res.cloudinary.com/dtnypuixy/video/upload/f_auto,q_auto/v1778262526/vblvid.mp4", 
    "content_photo": "https://res.cloudinary.com/dtnypuixy/image/upload/f_auto,q_auto/v1778262760/content-photo.jpg", 
    "contact": {
        "email": "Laurinejagui@gmail.com",
        "instagram": "https://instagram.com/visualsbylaurine"
    }
}

# The Top 6 (Home Page)
PROJECTS = [
    {"id": "1", "title": "KLAT x Alex Spencer", "video": "https://res.cloudinary.com/dtnypuixy/video/upload/f_auto,q_auto/klat-project.MP4", "is_video": True, "tags": ["Cinema"], "meta": "Arri Alexa • 4:3"},
    {"id": "2", "title": "KLAT MAG", "video": "https://res.cloudinary.com/dtnypuixy/video/upload/f_auto,q_auto/noir-project.mp4", "is_video": True, "tags": ["Editorial"], "meta": "Director's Cut"},
    {"id": "3", "title": "STYLE 'N' SHOW EP2", "image": "https://res.cloudinary.com/dtnypuixy/image/upload/f_auto,q_auto/v1778262760/aesthetic-new.jpg", "is_video": False, "tags": ["Film"], "meta": "Visual Study"},
    {"id": "4", "title": "STYLE 'N' SHOW EP1", "video": "https://res.cloudinary.com/dtnypuixy/video/upload/f_auto,q_auto/v1778262766/city-project.mp4", "is_video": True, "tags": ["Urban"], "meta": "Sony FX3"},
    {"id": "5", "title": "BLACK GIRL HAIR SHOP", "image": "https://res.cloudinary.com/dtnypuixy/image/upload/f_auto,q_auto/shadow-form.JPG", "is_video": False, "tags": ["Editorial"], "meta": "Portrait"},
    {"id": "6", "title": "BLACK GIRL HAIR SHOP PT2", "image": "https://res.cloudinary.com/dtnypuixy/image/upload/f_auto,q_auto/final-reel.JPG", "is_video": False, "tags": ["Brand"], "meta": "Visual ID"}
]

# Smart Archive Loader
for i in range(1, 41):
    if i not in [20, 21, 22]:
        link = f"https://res.cloudinary.com/dtnypuixy/image/upload/f_auto,q_auto/work-{i}"
        PROJECTS.append({
            "id": f"w{i}", "title": f"Project {i}", "image": link, "is_video": False, "tags": ["Archive"], "meta": "VBL Production"
        })

SKILLS = [{"name": "Cinema", "level": 98}]