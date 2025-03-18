# Use asctime function to read internal clock and convert to human readable format.

import time

current_time = time.localtime()

converted_time = time.asctime(current_time)

print(converted_time)