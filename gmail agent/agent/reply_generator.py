from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


def generate_reply(email_text, tone):

    prompt = f"""
    You are SmartMail AI.

    Generate a {tone} professional email reply.

    Email:
    {email_text}

    Keep the response concise and polite.
    """

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True
    )

    outputs = model.generate(
        **inputs,
        max_length=150
    )

    return tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )