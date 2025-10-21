# Personal Mental Health Journal 
# Author: Aditi Singh
# Beginner-friendly command-line Python project to track daily mood

mood_log = []

print("Welcome to your Personal Mental Health Journal!")
print("Track your mood daily. Type 'quit' to exit, 'log' to see past entries.\n")

while True:
    mood = input("How are you feeling today? (happy/sad/angry/anxious/neutral): ").lower()
    
    if mood == "quit":
        print("Bye! Take care of yourself 😊")
        break
    elif mood == "log":
        if mood_log:
            print("\nYour mood log so far:")
            for i, m in enumerate(mood_log, 1):
                print(f"{i}. {m}")
            print()
        else:
            print("No moods recorded yet 😶\n")
    elif mood in ["happy", "sad", "angry", "anxious", "neutral"]:
        mood_log.append(mood)
        print(f"Mood '{mood}' saved! ✅\n")
    else:
        print("Oops! Invalid mood. Try again 😅\n")
