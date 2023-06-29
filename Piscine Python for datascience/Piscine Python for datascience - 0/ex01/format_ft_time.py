import time
import datetime

current_time = time.time()
elapsed_time = current_time - 0  # The starting point is January 1, 1970, 00:00:00 (UTC)

print(f"Seconds since January 1, 1970: {elapsed_time} or {elapsed_time:.2e} in scientific notation")

current_date = datetime.datetime.now().strftime("%B %d %Y")
print(current_date)