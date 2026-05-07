from datetime import datetime

def log_interaction(email, category, tone):

    with open(
        "logs/interaction_logs.txt",
        "a"
    ) as file:

        file.write(
            f"""
Time: {datetime.now()}
Category: {category}
Tone: {tone}
Email: {email}

=========================
"""
        )