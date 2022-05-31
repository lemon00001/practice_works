
with open('data/sample_data', 'w') as f:
   pass 
    
    
uniq = []
with open('data/sample_data_01', 'r') as f:
    for name in f.readlines():
        if name[0].islower():
            print(name)
            continue
        name.rstrip('- ')
        if name not in uniq:
            uniq.append(name)
            with open('data/sample_data', 'a') as fo:
                fo.writelines(name)
        
