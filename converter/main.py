

with open('data/en', 'r') as f:
    en = [ch[:-1] for ch in f.readlines()]

with open('data/mn', 'r') as f:
    mn = [ch[:-1] for ch in f.readlines()]

converter = dict(zip(mn, en))

with open('latin_names_data', 'w') as file:
    pass

special_case = ['е', 'ё', 'ю', 'я']
vowel = ['а', 'э', 'о', 'у', 'ө', 'ү', 'и']


with open('data/sample_data', 'r') as f:
    cyrillic_names = [name.lower().strip() for name in f.readlines()]
    latin_names = []
    for name in cyrillic_names:
        a_name: str = ''
        prev = False
        for ch in name:
            if ch.isalpha():
                if not prev or ch not in vowel:
                    a_name += converter[ch]
                prev = False
                if ch in special_case:
                    prev = True
                continue

            a_name += ch
        latin_names.append(a_name)
        with open('latin_names_data', 'a') as file:
            file.write(a_name + '\n')
