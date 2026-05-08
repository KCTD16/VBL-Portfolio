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

PROJECTS = [
    {"id": "1", "title": "KLAT x Alex Spencer", "video": "https://res.cloudinary.com/dtnypuixy/video/upload/f_auto,q_auto/klat-project.mp4", "is_video": True, "tags": ["Cinema"]},
    {"id": "2", "title": "KLAT MAG", "video": "https://res.cloudinary.com/dtnypuixy/video/upload/f_auto,q_auto/noir-project.mp4", "is_video": True, "tags": ["Editorial"]},
    {"id": "3", "title": "STYLE 'N' SHOW EP2", "image": "https://res.cloudinary.com/dtnypuixy/image/upload/f_auto,q_auto/aesthetic-new.jpg", "is_video": False, "tags": ["Film"]},
    {"id": "4", "title": "STYLE 'N' SHOW EP1", "video": "https://res.cloudinary.com/dtnypuixy/video/upload/f_auto,q_auto/city-project.mp4", "is_video": True, "tags": ["Urban"]},
    {"id": "5", "title": "BLACK GIRL HAIR SHOP", "image": "https://res.cloudinary.com/dtnypuixy/image/upload/f_auto,q_auto/shadow-form.jpg", "is_video": False, "tags": ["Editorial"]},
    {"id": "6", "title": "BLACK GIRL HAIR SHOP PT2", "image": "https://res.cloudinary.com/dtnypuixy/image/upload/f_auto,q_auto/final-reel.jpg", "is_video": False, "tags": ["Brand"]}
]

# Adding exactly 19 archive pieces to avoid broken links
for i in range(1, 20):
    # This checks for the common formats. If you renamed them all to .webp, it finds them.
    # If one is a .png, it finds that too.
    PROJECTS.append({
        "id": f"w{i}",
        "title": f"Project {i}",
        "image": f"https://res.cloudinary.com/dtnypuixy/image/upload/f_auto,q_auto/work-{i}",
        "is_video": False,
        "tags": ["Archive"]
    })

SKILLS = [{"name": "Cinema", "level": 98}]