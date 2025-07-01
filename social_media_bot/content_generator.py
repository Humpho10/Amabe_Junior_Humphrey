# import openai
# import os
# from dotenv import load_dotenv

# load_dotenv()

# openai.api_key = os.getenv("OPENAI_API_KEY")

# def generate_tweet():
#     prompt = "Generate a catchy and positive tweet about productivity and motivation."
    
#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[
#             {"role": "system", "content": "You are a social media expert."},
#             {"role": "user", "content": prompt}
#         ],
#         max_tokens=60,
#         temperature=0.7
#     )
    
#     tweet = response['choices'][0]['message']['content'].strip()
#     return tweet


import random

def generate_message():
    tweets = [
        "Start your day with purpose. 💪 #MondayMotivation",
        "Keep pushing, even when it gets tough. 🔥 #GrindTime",
        "Small steps every day lead to big results. 🚀 #Progress",
        "Believe in your grind and trust the process. 🌟 #Mindset",
        "Stay focused, stay humble. The best is yet to come. 💯",
        "Don’t wait for the opportunity. Create it. 🎯",
        "Consistency beats motivation. Do it anyway. ✅",
        "Discipline is choosing what you want most over what you want now.",
        "You’re closer than you think. Keep going. 🏁",
        "Make it happen. Shock everyone. ⚡️ #NoExcuses"
    ]

    return random.choice(tweets)
