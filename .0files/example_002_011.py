import ray


@ray.remote
class HelloWorld:
    def __init__(self):
        self.value = 0

    def greet(self):
        self.value += 1
        return f"Hi user #{self.value}"


hello_world = HelloWorld.remote()

if __name__ == '__main__':
    for i in range(100):
        print(ray.get(hello_world.greet.remote()))
