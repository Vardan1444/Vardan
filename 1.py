vowels = 'ауоыиэяюёе'
vowels_answer = []
text = input('Введите текст: ').lower()

for letter in text:
    if letter in vowels:
        vowels_answer.append(letter)

print(vowels_answer, len(vowels_answer))
print(vowels_answer, len(vowels_answer))
