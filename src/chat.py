import os
from openai import OpenAI

def chat_openai(model, message):
    
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {   
                "role": "system",
                "content": """ You are a helpful python assistant """},
            {
                "role": "user",
                "content": f"Context: {message}",
            }
        ],
        model=model,
    )

    response = chat_completion.choices[0].message.content

    return response