string = input('Please enter a string: ')

word_count = 0
for char in string:
    if char == ' ':
        word_count += 1

word_count += 1

print('Here are the number of words in your string: ', word_count)
