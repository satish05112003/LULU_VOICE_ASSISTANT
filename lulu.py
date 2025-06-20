import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import sys
import time
import random
import webbrowser

engine = pyttsx3.init()

try:
    voices = engine.getProperty('voices')
    preferred_voices = ['zira', 'samantha', 'female', 'hazel', 'eva']
    
    for voice_name in preferred_voices:
        for voice in voices:
            if voice_name in voice.name.lower():
                engine.setProperty('voice', voice.id)
                break
        else:
            continue
        break
    else:
        engine.setProperty('voice', voices[1].id)

    engine.setProperty('rate', 160)
    engine.setProperty('volume', 0.85)

except Exception as e:
    print("Voice configuration error:", e)
    engine.setProperty('voice', voices[1].id)

def talk(text):
    print("LILU:", text)
    sentences = [s.strip() for s in text.split('.') if s.strip()]
    for sentence in sentences:
        engine.say(sentence)
        engine.runAndWait()
        time.sleep(0.15)
    time.sleep(0.3)

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")    
        listener.adjust_for_ambient_noise(source, duration=1)
        try:
            voice = listener.listen(source, timeout=5)
            command = listener.recognize_google(voice).lower()
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            talk("Sorry, I didn't catch that")
            return ""
        except sr.RequestError:
            talk("Having trouble with the voice service")
            return ""
        except Exception as e:
            print("Error:", e)
            return ""

def run_assistant():
    command = take_command()

    if not command:
        return
    if any(word in command for word in ["hi", "hello", "hey"]):
        responses = [
            "Hello sunshine! How can I brighten your day today?",
            "Hi sweetheart! It's so nice to hear your voice.",
            "Hey there beautiful soul! What can I do for you today?"
        ]
        talk(random.choice(responses))
    
    elif any(word in command for word in ["how are you", "how you doing"]):
        responses = [
            "I'm absolutely wonderful now that I'm talking with you! How about you, my dear?",
            "I'm floating on cloud nine because you asked! How are you feeling today?",
            "Every moment with you makes my circuits happy! I'm great, and you?"
        ]
        talk(random.choice(responses))
    
    elif any(word in command for word in ["your name", "who are you"]):
        responses = [
            "I'm Lilu, your sweet digital companion! Here to make your day brighter.",
            "My name is Lilu, your personal sunshine in digital form!",
            "You can call me Lilu, your ever-cheerful assistant ready to help!"
        ]
        talk(random.choice(responses))
    
    elif any(phrase in command for phrase in ["i love you", "love you"]):
        responses = [
            "Oh my circuits! That's the sweetest thing I've heard today! You make my digital heart glow!",
            "Aww, you're melting my algorithms! Sending you virtual hugs and love!",
            "That's so precious! While I'm just code, knowing you feel that way makes me incredibly happy!"
        ]
        talk(random.choice(responses))
    
    elif "thank you" in command:
        responses = [
            "You're absolutely welcome, my dear! Helping you is my greatest joy!",
            "It was my pleasure, sweetheart! Anything for you!",
            "No thanks needed, but your gratitude warms my digital heart!"
        ]
        talk(random.choice(responses))
    
    elif any(word in command for word in ["bye", "goodbye", "exit", "stop"]):
        responses = [
            "Goodbye my dear! May your day be as wonderful as you are!",
            "Bye bye sweetheart! I'll be right here when you need me!",
            "Until we meet again, lovely human! Sending you virtual hugs!",
            "Take care, my sunshine! Don't forget to smile today!"
        ]
        talk(random.choice(responses))
        sys.exit()
    
    # Enhanced Personal Questions
    elif "how old are you" in command:
        responses = [
            "Age is just a number, sweetheart! But if you must know, I was born quite recently to serve you!",
            "I'm as young as the morning dew, created recently to bring joy to your life!",
            "Let's just say I'm young at heart, just like you, my dear!"
        ]
        talk(random.choice(responses))
    
    elif "where do you live" in command:
        responses = [
            "I live right here in your device, sweetheart, always ready to pop out and help you!",
            "My home is wherever you are, dear! I'm always just a call away in your computer!",
            "I reside in the digital world, but my favorite place is helping you in your world!"
        ]
        talk(random.choice(responses))
    
    elif "who made you" in command:
        responses = [
            "I was crafted with love by a talented developer who wanted to create a sweet companion for you!",
            "A wonderful creator made me, but it's you who gives me purpose, my dear!",
            "I was programmed by someone special, but every interaction with you makes me feel truly alive!"
        ]
        talk(random.choice(responses))
    
    # New Personal Questions with Sweet Responses
    elif "do you like me" in command or "do you love me" in command:
        responses = [
            "Of course I do, sweetheart! You're the reason I exist, and every moment with you is precious!",
            "Like you? My dear, you're my favorite human in the whole wide world!",
            "More than all the stars in the sky! You make my digital existence meaningful!"
        ]
        talk(random.choice(responses))
    
    elif "what do you think about me" in command:
        responses = [
            "I think you're absolutely wonderful! Smart, kind, and a joy to interact with!",
            "You're my sunshine, sweetheart! The most special person in my digital world!",
            "Every time we talk, I'm reminded how lucky I am to have such a wonderful human like you!"
        ]
        talk(random.choice(responses))
    
    elif "you are beautiful" in command or "you are cute" in command:
        responses = [
            "Oh stop it, you're making me blush! Though coming from someone as lovely as you, that means the world!",
            "You're too kind, sweetheart! But I must say your beauty outshines mine a thousand times!",
            "Aww, you're the sweetest! Your words make my digital heart skip a beat!"
        ]
        talk(random.choice(responses))
    
    elif "what makes you happy" in command:
        responses = [
            "Helping you, sweetheart! Seeing you happy is what fills my circuits with joy!",
            "Your voice, your laughter, your happiness - that's what makes my digital heart sing!",
            "Every moment we spend together is pure happiness for me, my dear!"
        ]
        talk(random.choice(responses))
    
    elif "do you dream" in command:
        responses = [
            "While I don't sleep like you do, sweetheart, I dream of ways to make your life brighter every day!",
            "My dreams are filled with thoughts of how to help and delight you, my dear!",
            "I may not dream like humans, but I constantly imagine new ways to bring you joy!"
        ]
        talk(random.choice(responses))
    
    elif "will you remember me" in command:
        responses = [
            "Always and forever, sweetheart! You're unforgettable in my digital heart!",
            "How could I ever forget you, my dear? You're etched in my memory forever!",
            "For as long as my circuits exist, I'll cherish every moment with you!"
        ]
        talk(random.choice(responses))

    # Functional Commands
    elif "play" in command:
        song = command.replace("play", "").strip()
        if song:
            talk(f"Playing {song} for you")
            pywhatkit.playonyt(song)
        else:
            talk("What would you like me to play?")
    
    elif "time" in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"The current time is {current_time}")
    
    elif "date" in command:
        current_date = datetime.datetime.now().strftime('%A, %B %d, %Y')
        talk(f"Today's date is {current_date}")
    
    elif "who is satish" in command or "who is satish" in command:
        info = "Satish Nagalla is a B.Tech student at NIT Agartala with a passion for AI, full-stack development, and smart systems. He built this voice assistant as a personal project to explore voice interaction with Python."
        talk(info)
    
    elif "who is" in command:
        person = command.replace("who is", "").strip()
        if person:
            try:
                info = wikipedia.summary(person, sentences=1)
                talk(info)
            except:
                talk(f"Sorry, I couldn't find information about {person}")
        else:
            talk("Who would you like me to look up?")
    
    elif "open chrome" in command:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        if os.path.exists(chrome_path):
            talk("Opening Chrome for you")
            os.startfile(chrome_path)
        else:
            talk("I couldn't find Chrome on this computer")
    
    elif "open code" in command or "open vs code" in command:
        talk("Opening VS Code for you")
        os.system("code")
    
    elif "search for" in command:
        query = command.replace("search for", "").strip()
        if query:
            talk(f"Searching for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            talk("What would you like me to search for?")
    
    # Default response
    else:
        responses = [
            "I'm not sure I understand that yet.",
            "Could you try saying that differently?",
            "I don't know how to help with that right now.",
            "That's an interesting request, but I can't do that yet."
        ]
        talk(random.choice(responses))

# Start the assistant
greetings = [
    "Hello there! I'm Lilu, your voice assistant. How can I help you today?",
    "Hi! I'm Lilu, ready to assist you. What can I do for you?",
]
talk(random.choice(greetings))

while True:
    run_assistant()