import unittest
import test_basic_best_fit

def best_fit(memoria, req, inicio):

    if not memoria:
        return None


    if isinstance(req, int):
        req = [req]

    memoria = memoria[:] 
    resultados = []

    for proceso in req:
        tamañoProceso = proceso
        best_index = -1  
        best_fit_size = float('inf')

        n = len(memoria)
        recorrido = 0 


        i = inicio
        while recorrido < n:
            base, limite = memoria[i]

            if limite >= tamañoProceso and limite < best_fit_size:
                best_index = i
                best_fit_size = limite

            i = (i + 1) % len(memoria)
            recorrido += 1

        if best_index == -1:
            return None

        base, limite = memoria[best_index]

        nueva_base = base

        nuevo_limite = limite - tamañoProceso 

        if nuevo_limite == 0:
            print(f"Se elimina el bloque {hex(base)} porque quedó completamente asignado.")
            del memoria[best_index]

            if len(memoria) > 0:
                best_index = best_index % len(memoria)
            else:
                best_index = 0
        else:
            memoria[best_index] = (base + tamañoProceso, nuevo_limite)

        nuevo_indice = best_index

        resultados.append((memoria[:], nueva_base, tamañoProceso, nuevo_indice))

    return resultados[0] if len(resultados) == 1 else resultados

if __name__ == '__main__':
    print("\n Prueba manual:")
    memoria_prueba = [
        (0x06D01000, 0x00500000),
        (0x06100C00, 0x00C00000),
        (0x05200400, 0x00F00000),
        (0x04800000, 0x00A00000),
        (0x01E00000, 0x00400000),
        (0x02500000, 0x01400000),
        (0x07201800, 0x01200000),
        (0x08402C00, 0x00700000)
    ]
    req_prueba = [0x00C00000, 0x00A00000, 0x00B00000]
    index_prueba = 0

    print(f"Memoria antes de asignar: {memoria_prueba}")
    resultado_prueba = best_fit(memoria_prueba, req_prueba, index_prueba)
    print(f"Resultado de best_fit: {resultado_prueba}")

    print("\nEjecutando pruebas del profesor...\n")
    unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromModule(test_basic_best_fit))
