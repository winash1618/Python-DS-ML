"""
You are about to discover the yield operator!
So let's create a function called ft_progress(lst).
The function will display the progress of a for loop.
"""

import time
import math

def ft_progress(lst) -> None:
    """
    The function will display the progress of a for loop.
    """
    start_time = time.time()
    count = 0
    for elem in lst:
        count += 1
        yield elem
        end_time = time.time()
        print(f"ETA: {round((end_time - start_time) / (count / len(lst)), 2)}s",
              f" [{'>'.rjust(math.ceil(20 * (count / len(lst))), '='):21}] ",
              f"{count}/{len(lst)} | elapsed time {round(end_time - start_time, 2)}s", end="\r")
    print()