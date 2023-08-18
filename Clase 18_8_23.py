#Recorrer string y string

def main():
    nombre = input("Ingrese un nombre: ")
    for letra in nombre:
        print(letra)

lista = ["elemento1", "elemento2", "elemento3", "elemento4", "elemento5"]
print(len(lista))
for elemento in lista[::-1]:
    print(elemento)
    print(elemento[::-1])
    #for letra in elemento[::-1]:
    #    print(letra, end="")

if __name__ == '__main__':
    main()