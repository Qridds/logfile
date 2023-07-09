```python
import pytesseract
from PIL import Image

def ocr_scan(file_path):
    """
    Function to perform OCR on a given file.
    """
    try:
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        print(f"Error in OCR scan: {e}")
        return None

def summarize_text(text):
    """
    Function to summarize the scanned text using AI.
    """
    # Placeholder for AI text summarization. This can be replaced with any AI model for text summarization.
    summarized_text = text[:100] + "..."
    return summarized_text

def process_document(file_path):
    """
    Function to process a document file. It performs OCR and then summarizes the text.
    """
    scanned_text = ocr_scan(file_path)
    if scanned_text is not None:
        summarized_text = summarize_text(scanned_text)
        return summarized_text
    else:
        return None
```