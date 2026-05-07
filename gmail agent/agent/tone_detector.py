from transformers import pipeline

tone_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base"
)

def detect_tone(email_text):

    result = tone_classifier(email_text)

    return result[0]["label"]