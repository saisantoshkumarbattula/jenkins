import time

def timed_print(duration_seconds):
    """Prints a message every second for a specified duration and then the total time."""

    start_time = time.monotonic()  # Use monotonic time for accuracy
    end_time = start_time + duration_seconds

    for i in range(duration_seconds):  # More Pythonic loop
        time.sleep(1)
        elapsed_time = time.monotonic() - start_time
        print(f"Elapsed time = {elapsed_time:.2f} seconds")

    total_time_taken = time.monotonic() - start_time
    print(f"\nTotal time taken: {total_time_taken:.2f} seconds")


if __name__ == "__main__":
    timed_print(30)
