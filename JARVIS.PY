import requests
from groq import Groq

client = Groq(api_key="YOUR_API_KEY")

def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    response = requests.get(url)
    return response.text

def get_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    data = response.json()
    return f"{data['setup']} ... {data['punchline']}"

messages = [
    {"role": "system", "content": "You are Jarvis, a helpful AI assistant. Answer in clear English. When weather data is provided, summarize it nicely. When a joke is provided, tell it properly - first the setup, then the punchline. Don't explain the joke."}]

while True:
    user_input = input("Tu: ")
    if user_input == "quit":
        break

    if "weather" in user_input.lower():
        city = user_input.split()[-1]
        weather = get_weather(city)
        messages.append({"role": "user", "content": f"{user_input}. Weather data: {weather}"})
    
    elif "joke" in user_input.lower():
        joke = get_joke()
        messages.append({"role": "user", "content": f"Tell me this joke: {joke}"})

    else:
        messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )
    

    reply = response.choices[0].message.content
    print(f"Jarvis: {reply}")
    messages.append({"role": "assistant", "content": reply})