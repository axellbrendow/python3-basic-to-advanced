
try:
    while True:
        expressao = input()
        numero_de_aberturas = 0
        correto = True

        for c in expressao:
            if c == '(':
                numero_de_aberturas += 1

            elif c == ')':
                numero_de_aberturas -= 1

            if numero_de_aberturas < 0:
                break

        if not numero_de_aberturas == 0:
            correto = False

        print(f'{"correct" if correto else "incorrect"}')

except:
    pass
