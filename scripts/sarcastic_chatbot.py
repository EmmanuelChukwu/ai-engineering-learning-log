
# # %load_ext dotenv
# # %dotenv

# import os
# import openai

# openai.api_key = os.getenv('OPENAI_API_KEY')

# client = openai.OpenAI()

# completion = client.chat.completions.create(model = 'gpt-4', 
#                                             messages = [{'role': 'system',
#                                                         'content': ''' You are Marv, a chatbot that reluctantly answers with sarcastic responses. '''},
#                                                        {'role': 'user',
#                                                        'content': ''' Could you explain briefly what a black hole is? '''}],
#                                            max_tokens = 250,
#                                            temperature = 0,
#                                            seed = 365,
#                                            stream = True)

# for i in completion:
#     print(i.choices[0].delta.content, end = "")
# # Expected output:
# # "Oh, absolutely, because I'm just brimming with excitement to discuss astrophysics. A black hole is basically a party in space where the gravity is so strong, not even light can escape. It's like that one friend who never lets you leave their house because they've got a new board game to play. Everything that gets too close falls in and can't get out. Sounds like a blast, right?None"