
file1 = open('form_base copy.html', 'r')
file2 = open('form_base copy.html', 'w')

Lines = file1.readlines()

for line in Lines:
    if line.find('assets'):
        print('dsa')

