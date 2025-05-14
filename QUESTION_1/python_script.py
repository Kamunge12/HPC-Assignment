#!/usr/bin/env python3.8
# calculate the sum of the first ten million intergers
import time
start_time = time.time()
n = 10000000
sum_intergers = n * (n+1) // 2 # interger division to avoid float
end_time=time.time()
print(f"sum of the first ten million intergers:{sum_intergers}")
print(f"execution time:{end_time-start_time:.4f}seconds")


