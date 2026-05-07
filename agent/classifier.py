from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

LABELS = [
    "Meeting",
    "Sales",
    "Support",
    "Complaint",
    "HR",
    "Follow-up",
    "General"
]

def classify_email(email_text):
    result = classifier(email_text, LABELS)
    return result["labels"][0]