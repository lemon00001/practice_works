
def encoder(ch):
    if ch == 'ѐ':
        return 'ё'
    if ch == 'є':
        return 'ү'
    if ch == 'ѐ':
        return 'ө'
    if ch == 'ѓ':
        return 'ө'
    if ch == 'ї':
        return 'ү'
    if ch == 'ђ':
        return 'ү'

with open('data/mn', 'r') as f:
    mn = [ch[:-1] for ch in f.readlines()]


with open('data/sample_data_01', 'w') as f1:
    pass


undefined_chr = []
unique_names = []
with open('data/sample_data', 'r') as f:

    for name in f.readlines():
        fixed = ''
        for ch in name.strip():
            if ch == '-':
                fixed += ch
                continue
            if ch.lower() not in mn:
                if ch not in undefined_chr:
                    print(ch)
                    undefined_chr.append(ch)
                ch = encoder(ch.lower())
            fixed += ch
        if fixed not in unique_names:
            unique_names.append(fixed)

            with open('data/sample_data_01', 'a') as f1:
                f1.writelines(fixed + '\n')

