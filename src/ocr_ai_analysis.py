```python
import pytesseract
from PIL import Image

def ocrScan(file):
    # Check if the file is an image
    if file['type'] not in ['jpg', 'png', 'jpeg']:
        raise ValueError("Invalid file type for OCR. Please upload an image file.")

    # Open the image file
    image = Image.open(file['name'])

    # Use pytesseract to perform OCR on the image
    text = pytesseract.image_to_string(image)

    # Update the file's text content and type
    file['text'] = text
    file['type'] = 'txt'

    # Call the updateFile function to update the file in userFiles
    updateFile(file)

    return text
```