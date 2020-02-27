import cloudinary 
import cloudinary.uploader
from api_credential import api_key,api_secret, cloud_name

api_key=api_key
api_secret= api_secret
cloud_name=cloud_name

cloudinary.config(cloud_name=cloud_name,api_key=api_key, api_secret=api_secret)

img=cloudinary.uploader.upload("images.jpg",public_id="dragon")
print(img["secure_url"])