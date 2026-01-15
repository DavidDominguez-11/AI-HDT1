import random

# Clase Environment
class Environment:
    def __init__(self):
        # Temperatura inicial random entre 15 y 30 grados
        self.temperature = random.randint(15, 30)


# Clase Agent
class Agent:
    def act(self, perception):
        # la fun f(estado) -> accion
        pass


def main():
    env = Environment()
    agent = Agent()

    print(env.temperature)

if __name__ == "__main__":
    main()
