import tracemalloc
import pandas as pd
from crowdsignals_ch3_outliers import main as function_to_test

# function could be moved to utils and loaded in script ifnamemain?

def trace_memory(operation):
    tracemalloc.start()
    operation()
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    tracemalloc.stop()

if __name__ == '__main__':
    trace_memory(function_to_test)