def process_string(input_string):
    vowels = 'аеєиіїоуюяАЕЄИІЇОУЮЯ'
    consonants = 'бвгґджзйклмнпрстфхцчшщБВГҐДЖЗЙКЛМНОПРСТФХЦЧШЩ'
    
    # Збираємо голосні та приголосні літери
    found_vowels = [char for char in input_string if char in vowels]
    found_consonants = [char for char in input_string if char in consonants]
    
    # Зворотній алфавітний порядок
    found_vowels.sort(reverse=True)
    found_consonants.sort(reverse=True)
    
    # Перший елемент - всі голосні в зворотньому алфавітному порядку
    vowels_str = ''.join(found_vowels)
    
    # Другий елемент - перевірка на кількість голосних
    is_few_vowels = len(found_vowels) < 2
    
    # Третій елемент - всі приголосні в зворотньому алфавітному порядку
    consonants_str = ''.join(found_consonants)
    
    return (vowels_str, is_few_vowels, consonants_str)

# Приклад використання:
try:
    input_string = input()
    result = process_string(input_string)
    print(result)
except Exception as e:
    print(f"Виникла помилка: {e}")