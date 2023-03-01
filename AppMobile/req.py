with open('requirements.txt', 'r') as f:
    lines = f.readlines()

with open('arquivo_com_virgulas.txt', 'w') as f:
    for line in lines:
        f.write(line.rstrip() + ',\n')
