import os
import pdfplumber

def checker(name: str) -> bool:
    cnt = 0
    for ch in name:
        if ch == '-':
            continue
        if ord(ch) < 1025 or ord(ch) > 1257:
            return False
    return True


num_pdf = 0
dir_path = r'/home/lemon/practical_works/extract/data'

for path in os.scandir(dir_path):
    if path.is_file():
        num_pdf += 1

with open('sample_data', 'w') as f:
    pass

col = ['овог, нэр', 'овог', 'нэр', 'эцэг/эхийн нэр', 'оюутны овог']
sets = []

for num in range(num_pdf):
    with pdfplumber.open(r'data/sample{}.pdf'.format(num)) as pdf:
        num_pages = len(pdf.pages)
        cols_num = []
        for row_idx, row in enumerate(pdf.pages[0].extract_table()):
            for col_idx, col_name in enumerate(row):
                if col_name is None:
                    continue
                col_name = col_name.lower()
                if col_name in col:
                    cols_num.append(col_idx)
            if row_idx > 5:
                break

        for i in range(num_pages):
            page = pdf.pages[i].extract_table()
            if page is None:
                continue
            for row in page:
                #print(row)
                for col_num in cols_num:
                    if col_num >= len(row):
                        continue
                    
                    fixing = str(row[col_num]).replace('-\n', '-')
                    fixing = fixing.replace('.', ' ')
                    fixing = fixing.replace(' -', '-')
                    fixing = fixing.replace('- ', '-')
                    fixing = fixing.replace('\n', ' ')
                    names = fixing.split()
                    with open('sample_data', 'a') as result:
                        for name in names:
                            name = name.strip('.,')
                            if name.lower() in col or len(name) < 2 or name == 'None':
                                continue
                            if not checker(name):
                                continue
                            if name.endswith('гын'):
                                name = name[:-3]
                            if name.endswith('гийн'):
                                name = name[:-4]
                            if name.endswith('ын'):
                                name = name[:-2]
                            if name.endswith('ийн'):
                                name = name[:-3]
                            if name == 'Диплом':
                                continue

                            for ch in name:
                                if ord(ch) == 1111:
                                    name.replace(ch, chr(1199))
                                    

                            if name not in sets:
                                sets.append(name)
                                result.writelines(str(name) + '\n')
