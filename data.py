BIO = {
    "name": "VBL",
    "full_name": "Visuals By Laurine",
    "role": "Cinematographer & Creative Director",
    "location": "Manchester, UK",
    "experience": "8+ Years",
    "est_year": "2020", 
    "bio": "I create cinematic visuals and authentic imagery that turn moments into stories. Through photography and videography, my goal is to craft work that feels real, evokes emotion, and leaves a lasting impact.",
    "hero_video": "https://res.cloudinary.com/dtnypuixy/video/upload/v1778262526/vblvid_owcto7.mp4", 
    "content_photo": "https://res.cloudinary.com/dtnypuixy/image/upload/vbl/content-photo.jpg", 
    "contact": {
        "email": "Laurinejagui@gmail.com",
        "instagram": "instagram.com/visualsbylaurine"
    }
}

# Add your 6 main links here. 
# IMPORTANT: Use the full https link for every single one!
PROJECTS = [
    {"id": "1", "title": "KLAT x Alex Spencer", "video": "https://res.cloudinary.com/dtnypuixy/video/upload/vbl/klat-project.mp4", "is_video": True, "tags": ["Cinema"]},
    {"id": "2", "title": "KLAT MAG", "video": "https://res.cloudinary.com/dtnypuixy/video/upload/vbl/noir-project.mp4", "is_video": True, "tags": ["Editorial"]},
    {"id": "3", "title": "STYLE 'N' SHOW EP2", "image": "https://res.cloudinary.com/dtnypuixy/image/upload/vbl/aesthetic-new.jpg", "is_video": False, "tags": ["Film"]},
    {"id": "4", "title": "STYLE 'N' SHOW EP1", "video": "https://res.cloudinary.com/dtnypuixy/video/upload/vbl/city-project.mp4", "is_video": True, "tags": ["Urban"]},
    {"id": "5", "title": "BLACK GIRL HAIR SHOP", "image": "https://res.cloudinary.com/dtnypuixy/image/upload/vbl/shadow-form.jpg", "is_video": False, "tags": ["Editorial"]},
    {"id": "6", "title": "BLACK GIRL HAIR SHOP PT2", "image": "https://res.cloudinary.com/dtnypuixy/image/upload/vbl/final-reel.jpg", "is_video": False, "tags": ["Brand"]}
]

# For the rest of the 19 photos, update these links with your Cloudinary URLs
for i in range(1, 20):
    PROJECTS.append({
        "id": f"cloud-{i}",
        "title": f"Work {i}",
        "image": f"https://res.cloudinary.com/dtnypuixy/image/upload/vbl/work-{i}.jpg",
        "is_video": False,
        "tags": ["Full Works"]
    })

SKILLS = [{"name": "Cinema", "level": 98}]