#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    conteo = len(sys.argv) - 1
    suma = 0
    for i in range(1, conteo + 1):
        suma = suma + int(argv[i])
    print(suma)
