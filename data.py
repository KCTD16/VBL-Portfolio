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

# THE CURATED TOP 6 (Exactly as they were on your front page)
PROJECTS = [
    {"id": "1", "title": "KLAT x Alex Spencer", "video": "https://res.cloudinary.com/dtnypuixy/video/upload/f_auto,q_auto/klat-project.mp4", "is_video": True, "tags": ["Cinema"]},
    {"id": "2", "title": "KLAT MAG", "video": "https://res.cloudinary.com/dtnypuixy/video/upload/f_auto,q_auto/noir-project.mp4", "is_video": True, "tags": ["Editorial"]},
    {"id": "3", "title": "STYLE 'N' SHOW EP2 STILL", "image": "https://res.cloudinary.com/dtnypuixy/image/upload/f_auto,q_auto/v1778262760/aesthetic-new.jpg", "is_video": False, "tags": ["Film"]},
    {"id": "4", "title": "STYLE 'N' SHOW EP1", "video": "https://res.cloudinary.com/dtnypuixy/video/upload/f_auto,q_auto/city-project.mp4", "is_video": True, "tags": ["Urban"]},
    {"id": "5", "title": "BLACK GIRL HAIR SHOP STILL", "image": "https://res.cloudinary.com/dtnypuixy/image/upload/f_auto,q_auto/shadow-form.jpg", "is_video": False, "tags": ["Editorial"]},
    {"id": "6", "title": "BLACK GIRL HAIR SHOP PT2", "image": "https://res.cloudinary.com/dtnypuixy/image/upload/f_auto,q_auto/final-reel.jpg", "is_video": False, "tags": ["Brand"]}
]

# THE NEW VIDEOS (Moved here so they only show in Full Works)
PROJECTS.append({"id": "w20", "title": "Work 20", "video": "https://res.cloudinary.com/dtnypuixy/video/upload/f_auto,q_auto/work-20.mp4", "is_video": True, "tags": ["Motion"]})
PROJECTS.append({"id": "w21", "title": "Work 21", "video": "https://res.cloudinary.com/dtnypuixy/video/upload/f_auto,q_auto/work-21.mp4", "is_video": True, "tags": ["Motion"]})
PROJECTS.append({"id": "w22", "title": "Work 22", "video": "https://res.cloudinary.com/dtnypuixy/video/upload/f_auto,q_auto/work-22.mp4", "is_video": True, "tags": ["Motion"]})

# Smart Loader for the remaining 19 photos
for i in range(1, 20):
    PROJECTS.append({
        "id": f"bulk-{i}",
        "title": f"Project {i}",
        "image": f"https://res.cloudinary.com/dtnypuixy/image/upload/f_auto,q_auto/work-{i}.jpg",
        "is_video": False,
        "tags": ["Photography"]
    })

SKILLS = [{"name": "Cinema", "level": 98}]