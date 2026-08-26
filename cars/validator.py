import os 
from django.core.exceptions import ValidationError
from PIL import Image

MAX_UPLOAD_SIZE_MB = 5 
ALLOWED_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.webp']
ALLOWED_CONTENT_TYPES = ['image/jpeg', 'image/png', 'image/webp']

def validate_IMG_file(file) :
    # size 
    max_seiz_byte = MAX_UPLOAD_SIZE_MB * 1024 * 1024 
    if file.size > max_seiz_byte : 
        raise ValidationError(f'unsuported file >> size :{MAX_UPLOAD_SIZE_MB}MB')
    # extension check 
    ext = os.path.splitext(file.name)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise ValidationError(f'unsuported file :{ext}')
    # content Type
    if hasattr(file , 'content_type') and file.content_type not in ALLOWED_CONTENT_TYPES :
        raise ValidationError(f"Unsupported content type: {file.content_type}")
    # rename the file 
    try : 
        img = Image.open(file)
        img.verify()
    except Exception:
        raise ValidationError("uplaoded file is not a valid img")

    file.seek(0)