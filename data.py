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
    {"id": "v-hero", "title": "VBL Showreel", "video": "https://res.cloudinary.com/dtnypuixy/video/upload/f_auto,q_auto/v1778262526/vblvid.mp4", "is_video": True, "tags": ["Motion"], "meta": "Director's Cut"},
    {"id": "v-city", "title": "City Project", "video": "https://res.cloudinary.com/dtnypuixy/video/upload/f_auto,q_auto/v1778262766/city-project.mp4", "is_video": True, "tags": ["Urban"], "meta": "4K Anamorphic"},
    {"id": "v-20", "title": "Work 20", "video": "https://res.cloudinary.com/dtnypuixy/video/upload/f_auto,q_auto/work-20.mp4", "is_video": True, "tags": ["Motion"], "meta": "Cinematography"},
    {"id": "v-21", "title": "Work 21", "video": "https://res.cloudinary.com/dtnypuixy/video/upload/f_auto,q_auto/work-21.mp4", "is_video": True, "tags": ["Motion"], "meta": "Visual Narrative"},
    {"id": "v-22", "title": "Work 22", "video": "https://res.cloudinary.com/dtnypuixy/video/upload/f_auto,q_auto/work-22.mp4", "is_video": True, "tags": ["Motion"], "meta": "Experimental"},
    {"id": "1", "title": "KLAT x Alex Spencer", "video": "https://res.cloudinary.com/dtnypuixy/video/upload/f_auto,q_auto/klat-project.MP4", "is_video": True, "tags": ["Cinema"], "meta": "Arri Alexa"},
    {"id": "2", "title": "KLAT MAG", "video": "https://res.cloudinary.com/dtnypuixy/video/upload/f_auto,q_auto/Noir-project.mp4", "is_video": True, "tags": ["Editorial"], "meta": "Commercial"}
]

# Smart Archive Loader
for i in range(1, 41):
    if i not in [20, 21, 22]:
        # Using f_auto without an extension is the safest way for Cloudinary
        link = f"https://res.cloudinary.com/dtnypuixy/image/upload/f_auto,q_auto/work-{i}"
        PROJECTS.append({
            "id": f"w{i}",
            "title": f"Project {i}",
            "image": link, 
            "is_video": False,
            "tags": ["Archive"],
            "meta": "VBL Production"
        })

SKILLS = [{"name": "Cinema", "level": 98}]