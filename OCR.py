import pytesseract
from PIL import Image

def ocr(image_path):
    try:
        # Image ko open karein
        img = Image.open(image_path)
        
        # Image se text extract karein
        text = pytesseract.image_to_string(img)
        
        # Extracted text ko return karein
        return text
    except Exception as e:
        print("Error during OCR:", e)
        return None

def main():
    image_path = input("Enter path to the image file: ")
    extracted_text = ocr(image_path)
    
    if extracted_text:
        print("Extracted text:")
        print(extracted_text)
    else:
        print("OCR failed. Unable to extract text from the image.")

if __name__ == "__main__":
    main()
