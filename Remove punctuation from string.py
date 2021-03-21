pun="!@##$%^&*()_-}{];[:'?/\|.,~`"
str="hello &%^ YADAv ;'.. G"
no_pun=" "
for i in str:
    if i not in pun:
        no_pun=no_pun+i;
print(no_pun)
        
