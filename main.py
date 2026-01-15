import random

# Clase Environment
class Environment:
    def __init__(self):
        # Temperatura inicial random entre 15 y 30 grados
        self.temperature = random.randint(15, 30)

    def update(self, action):
        # Modifica la temperatura segun la act del agente
        if action == "enfriar":
            self.temperature -= 1
        elif action == "calentar":
            self.temperature += 1
        elif action == "esperar":
            pass  # No cambia la temperatura

    def get_percept(self):
        # Simula el sensor, devuelve la temperatura actual
        return self.temperature


# Clase Agent
class Agent:
    def act(self, perception):
        # la fun f(estado) -> accion
        if perception > 25:
            return "enfriar"
        elif perception < 18:
            return "calentar"
        else:
            return "esperar"


def main():
    env = Environment()
    agent = Agent()

    for i in range(10):
        print(f"Iteracion: {i + 1}")

        # Percepcion
        current_temp = env.get_percept()
        print(f"Temperatura actual: {current_temp}")

        # Accion
        action = agent.act(current_temp)
        print(f"Accion del agente: {action}")

        # Actualizacion del entorno
        env.update(action)
        new_temp = env.get_percept()
        print(f"Nueva temperatura: {new_temp}")
        print("=" * 30)


if __name__ == "__main__":
    main()