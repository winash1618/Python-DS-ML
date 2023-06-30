import time
import math
import shutil

terminal_width = shutil.get_terminal_size().columns - 40

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
        time_duration = round(((end_time - start_time) / (count / len(lst))) - (end_time - start_time), 2)
        minutes, seconds = divmod(time_duration, 60)
        time_duration1 = round(end_time - start_time, 2)
        minutes1, seconds1 = divmod(time_duration1, 60)
        print(f"{int((count/len(lst)) * 100)}%|{''.rjust(math.ceil(terminal_width * (count / len(lst))), progress_bar):{terminal_width}}| {count}/{len(lst)} [{minutes1:02.0f}:{seconds1:02.0f}<{minutes:02.0f}:{seconds:02.0f}, {round(len(lst)/(end_time - start_time) / (count / len(lst)), 2)}it/s]", end="\r")
    print()
