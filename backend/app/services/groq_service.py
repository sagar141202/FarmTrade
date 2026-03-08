import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)


def negotiation_coach(question: str, language: str):

    prompt = f"""
You are an expert agricultural investment advisor.

A farmer is preparing to talk to investors about funding their crop project.

Farmer question:
{question}

Respond with a confident and practical negotiation answer.

Language: {language}

Keep the response practical and farmer-friendly.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You help farmers negotiate with investors."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content