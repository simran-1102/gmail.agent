from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "facebook/bart-large-cnn"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


def summarize_email(email_text):

    prompt = f"""
    Summarize this email in a concise professional way:

    {email_text}
    """

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=1024
    )

    outputs = model.generate(
        **inputs,
        max_length=60,
        min_length=15
    )

    return tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )