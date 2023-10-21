from string import ascii_lowercase

with open('text-utf8.txt', 'w', encoding='utf8') as f:
    f.write(ascii_lowercase + '🏈')

with open('text-utf16.txt', 'w', encoding='utf16') as f:
    f.write(ascii_lowercase + '🏈')

with open('text-utf32.txt', 'w', encoding='utf32') as f:
    f.write(ascii_lowercase + '🏈')

with open('text-windows1252.txt', 'w', encoding='cp1252') as f:
    f.write(ascii_lowercase + '🏈')
