import ollama

prompt = "Why people die?"
instructions = "give funny sarcastic replies, keep answer short"
response = ollama.chat(model='llama3', messages=[{
    'role': 'user',
    'content': prompt + " " + instructions,
}])
print(response['message']['content'])
