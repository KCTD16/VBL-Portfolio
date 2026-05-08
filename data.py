import os

# Your Cloudinary Config
CLOUD_NAME = "dtnypuixy"
# Cloudinary uses different URLs for videos and images
VID_BASE = f"https://res.cloudinary.com/{CLOUD_NAME}/video/upload/vbl/"
IMG_BASE = f"https://res.cloudinary.com/{CLOUD_NAME}/image/upload/vbl/"

BIO = {
    "name": "VBL",
    "full_name": "Visuals By Laurine",
    "role": "Cinematographer & Creative Director",
    "location": "Manchester, UK",
    "experience": "8+ Years",
    "est_year": "2020", 
    "bio": "I create cinematic visuals and authentic imagery that turn moments into stories. Through photography and videography, my goal is to craft work that feels real, evokes emotion, and leaves a lasting impact.",
    "hero_video": f"{VID_BASE}vblvid.mp4", 
    "content_photo": f"{IMG_BASE}content-photo.jpg", 
    "contact": {
        "email": "Laurinejagui@gmail.com",
        "instagram": "instagram.com/visualsbylaurine"
    }
}

PROJECTS = [
    {"id": "1", "title": "KLAT x Alex Spencer", "video": f"{VID_BASE}klat-project.mp4", "is_video": True, "tags": ["Cinema"]},
    {"id": "2", "title": "KLAT MAG", "video": f"{VID_BASE}noir-project.mp4", "is_video": True, "tags": ["Editorial"]},
    {"id": "3", "title": "STYLE 'N' SHOW EP2", "image": f"{IMG_BASE}aesthetic-new.jpg", "is_video": False, "tags": ["Film"]},
    {"id": "4", "title": "STYLE 'N' SHOW EP1", "video": f"{VID_BASE}city-project.mp4", "is_video": True, "tags": ["Urban"]},
    {"id": "5", "title": "BLACK GIRL HAIR SHOP", "image": f"{IMG_BASE}shadow-form.jpg", "is_video": False, "tags": ["Editorial"]},
    {"id": "6", "title": "BLACK GIRL HAIR SHOP PT2", "image": f"{IMG_BASE}final-reel.jpg", "is_video": False, "tags": ["Brand"]}
]

# Smart Loader for the 19 Archive pieces (Now pulling from Cloud)
for i in range(1, 20):
    PROJECTS.append({
        "id": f"c{i}",
        "title": f"Work {i}",
        "image": f"{IMG_BASE}work-{i}.webp", # Assuming you uploaded as WebP for speed
        "is_video": False,
        "tags": ["Full Works"]
    })

SKILLS = [{"name": "Cinema", "level": 98}]