secret_word = "ahmed"
attempts = 5
index = 0

print(" You have 5 attempts to guess the word")

while attempts > 0 and index < len(secret_word):
    guess = input(f"Guess the letter number {index + 1}: ")
    if guess == secret_word[index]:
        print("😀 Correct guess")
        index += 1
    else:
        attempts -= 1
        print("🙁 Wrong guess")
        print(f"Remaining attempts: {attempts}")

if index == len(secret_word):
    print("🏆 Congratulations! You won 🤩 The word is:", secret_word)
else:
    print("😔 Game over! The word was:", secret_word)
