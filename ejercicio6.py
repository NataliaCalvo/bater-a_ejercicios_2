def ingresar_notas():
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    notas = {}

    for asignatura in asignaturas:
        nota = float(input(f"Escriba la nota de {asignatura}: "))
        notas[asignatura] = nota

    return notas

def main():
    notas = ingresar_notas()
    print("\nNotas introducidas:")
    for asignatura, nota in notas.items():
        print(f"{asignatura}: {nota}")

if __name__ == "__main__":
    main()