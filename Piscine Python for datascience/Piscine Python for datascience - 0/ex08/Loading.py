import time
import math
import shutil

terminal_width = shutil.get_terminal_size().columns - 41


def ft_tqdm(lst: range) -> None:
    """
    The function will display the progress of a for loop.
    """
    start_time = time.time()
    count = 0
    progress_bar = '\u2588'
    for elem in lst:
        count += 1
        yield elem
        end_time = time.time()
        count_value = count / len(lst)
        time_value = (end_time - start_time) / count_value
        time_duration = round(time_value - (end_time - start_time), 2)
        minutes, seconds = divmod(time_duration, 60)
        time_duration1 = round(end_time - start_time, 2)
        minutes1, seconds1 = divmod(time_duration1, 60)
        progress_value = math.ceil(terminal_width * (count / len(lst)))
        print(f"{int((count/len(lst)) * 100)}", end='')
        print(f"%|{''.rjust(progress_value, progress_bar):{terminal_width}}", end='')
        print(f"| {count}/{len(lst)} [{minutes1:02.0f}:{seconds1:02.0f}", end='')
        print(f"<{minutes:02.0f}:{seconds:02.0f}, ", end='')
        print(f"{round(len(lst)/(end_time - start_time) / count_value, 2)}", end='')
        print("it/s]", end='\r')
    print()
