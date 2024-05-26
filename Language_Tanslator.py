from deep_translator import GoogleTranslator

def translate_text(text, target_language='en'):
    translated_text = GoogleTranslator(source='auto', target=target_language).translate(text)
    return translated_text

def main():
    input_text = input("Enter text to translate: ")
    target_language = input("Enter target language (e.g., 'en' for English): ")
    translated_text = translate_text(input_text, target_language)
    print("Translated text:", translated_text)

if __name__ == "__main__":
    main()
