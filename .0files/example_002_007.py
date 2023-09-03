import timeit
import ray
import numpy as np
from tqdm import tqdm

ray.init()


def slow_task(x):
    import time
    time.sleep(0)
    return x


@ray.remote
def remote_task(x):
    return slow_task(x)


things_to_process = range(10)
very_slow_result = map(slow_task, things_to_process)
slowish_result = map(lambda x: remote_task.remote(x), things_to_process)

if __name__ == '__main__':
    slow_times, fast_times = [], []
    for i in tqdm(range(10000)):
        slow_time = timeit.timeit(lambda: list(very_slow_result), number=1)
        fast_time = timeit.timeit(lambda: list(ray.get(list(slowish_result))), number=1)
        slow_times.append(slow_time)
        fast_times.append(fast_time)
    print(f"In sequence {np.mean(slow_times):<6.6f}, in parallel {np.mean(fast_times):>6.6f}")

    ray.shutdown()
