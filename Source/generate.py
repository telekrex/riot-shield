def build():
    with open('targets.txt', 'r') as file:
        targets = file.read().split('\n')

    assembly = ''

    for target in targets:
        assembly += f'127.0.0.1 www.{target}.com\n'
        assembly += f'127.0.0.1 {target}.com\n'

    with open('generated.txt', 'w') as file:
        file.write(assembly)