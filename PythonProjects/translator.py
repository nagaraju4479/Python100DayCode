from google.cloud import translate_v2 as translate

# Instantiates a client
translate_client = translate.Client()

# The text to translate
text = 'Hello, world!'

# The target language
target = 'es'

# Translates the text into Spanish
translation = translate_client.translate(text, target_language=target)

print(f'Translation: {translation["input"]}\n{translation["translatedText"]}')
