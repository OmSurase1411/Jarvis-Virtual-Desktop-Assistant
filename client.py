from openai import OpenAI

#pip install openai
#If you saved the key under a different envirionment variable name, you can do something like:

client = OpenAI(
    api_key="<Your Open AI API Key",
)



completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa, Google, Siri and Google Cloud."},
        {
            "role": "user",
            "content": "What is coding."
        }
    ]
)

print(completion.choices[0].message.content)