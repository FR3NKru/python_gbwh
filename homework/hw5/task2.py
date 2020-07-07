def clear_list(dyrt: list) -> int:
    clear = []
    for i in dyrt:
        clear.extend(i)
    return len(clear)

with open('task2.txt', 'r', encoding='UTF-8') as my_file:
    line = 0
    words = []
    for ln in my_file:
        line += 1
        words.append(ln.split(' '))
    total_words = clear_list(words)

print(line)
print(total_words)