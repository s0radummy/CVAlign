import cloudinary.uploader
import cloudinary
import os
from dotenv import load_dotenv

load_dotenv()

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

def upload_to_cloudinary(file_content, filename):
    response = cloudinary.uploader.upload(
        file_content,
        public_id=filename,
        resource_type="raw"
    )
    return response["secure_url"]
