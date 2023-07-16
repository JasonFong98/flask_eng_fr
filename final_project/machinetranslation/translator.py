""" Translate Languages
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """ Translates English to French
    """
    french_text = MyMemoryTranslator(source = "en-US", target = "fr-CA").translate(english_text)
    return french_text

def french_to_english(french_text):
    """ Translates French to English
    """
    english_text = MyMemoryTranslator(source = "fr-CA", target = "en-US").translate(french_text)
    return english_text