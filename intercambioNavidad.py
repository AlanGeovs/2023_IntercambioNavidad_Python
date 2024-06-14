import random

# Definición de los grupos familiares
familias = {
    "Grupo 1": ["Carmen", "Marcelino"],
    "Grupo 2": ["Karina", "Victor", "Samara"],
    "Grupo 3": ["Don Victor", "Tere"],
    "Grupo 4": ["Fernanda", "Alan", "Jared", "Melanie"]
}

def asignar_regalos(familias):
    todos_los_nombres = [nombre for grupo in familias.values() for nombre in grupo]
    intento_maximo = 1000
    for _ in range(intento_maximo):
        regalos_asignados = {}
        for grupo, miembros in familias.items():
            for miembro in miembros:
                posibles_destinatarios = [nombre for nombre in todos_los_nombres if nombre not in familias[grupo] and nombre not in regalos_asignados.values()]
                if posibles_destinatarios:
                    destinatario = random.choice(posibles_destinatarios)
                    regalos_asignados[miembro] = destinatario
                else:
                    break
            else:
                continue
            break
        else:
            # Si se completa el ciclo sin romperlo, se encontró una asignación válida
            return regalos_asignados

    raise Exception("No se pudo encontrar una asignación válida después de varios intentos")

# Realizar la asignación de regalos
asignacion = asignar_regalos(familias)

# Imprimir la asignación de regalos
for dador, receptor in asignacion.items():
    print(f"{dador} dará un regalo a {receptor}")
