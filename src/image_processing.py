```python
from PIL import Image

def processImage(file_path, action, value):
    image = Image.open(file_path)

    if action == 'crop':
        left, upper, right, lower = value
        cropped_image = image.crop((left, upper, right, lower))
        cropped_image.save(file_path)
    elif action == 'resize':
        width, height = value
        resized_image = image.resize((width, height))
        resized_image.save(file_path)
    else:
        print("Invalid action")

    return file_path
```