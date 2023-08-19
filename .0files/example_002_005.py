import ray


def hi():
    import os
    import socket
    return f"Running on {socket.gethostname()} in pid {os.getpid()}"


@ray.remote
def hi_future():
    import os
    import socket
    return f"Running on {socket.gethostname()} in pid {os.getpid()}"


if __name__ == '__main__':
    print(hi())
    future = hi_future.remote()
    print(ray.get(future))
