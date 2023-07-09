```python
from PIL import Image

def processImage(file_path, action, value):
    image = Image.open(file_path)

    if action == 'crop':
        left, upper, right, lower = value
        cropped_image = image.crop((left, upper, right, lower))
        return cropped_image

    elif action == 'resize':
        width, height = value
        resized_image = image.resize((width, height))
        return resized_image

    elif action == 'rotate':
        angle = value
        rotated_image = image.rotate(angle)
        return rotated_image

    else:
        print("Invalid action. Please choose from 'crop', 'resize', or 'rotate'.")
        return None
```