import os
import time
import tracemalloc
import threading
import psutil


def _measure_peak_cpu(stop_event, peak_holder, interval=0.01):
    process = psutil.Process(os.getpid())
    process.cpu_percent(interval=None)

    while not stop_event.is_set():
        cpu = process.cpu_percent(interval=interval)
        if cpu > peak_holder["peak_cpu_percent"]:
            peak_holder["peak_cpu_percent"] = cpu


def benchmark(func, *args, **kwargs):
    stop_event = threading.Event()
    peak_holder = {"peak_cpu_percent": 0.0}

    cpu_thread = threading.Thread(
        target=_measure_peak_cpu,
        args=(stop_event, peak_holder),
        daemon=True
    )

    tracemalloc.start()
    cpu_thread.start()

    t0 = time.perf_counter()
    result = func(*args, **kwargs)
    t1 = time.perf_counter()

    stop_event.set()
    cpu_thread.join()

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    runtime_ms = (t1 - t0) * 1000
    if isinstance(peak, tuple):
        peak = peak[1]  # Tuple'ın ikinci elemanı genellikle 'peak' değeridir.

    peak_memory_mb = peak / 1024 / 1024

    return {
        "result": result,
        "runtime_ms": runtime_ms,
        "peak_memory_mb": peak_memory_mb,
        "peak_cpu_percent": peak_holder["peak_cpu_percent"],
    }