import json


with open('emojis.json') as f:
    emoji = json.load(f)
print(emoji['question_mark'])
