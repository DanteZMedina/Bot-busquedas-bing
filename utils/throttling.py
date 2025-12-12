import time
import random

def human_pause(min_s=0.4, max_s=0.9):
    time.sleep(random.uniform(min_s, max_s))

def between_searches(min_s=4, max_s=6):
    time.sleep(random.uniform(min_s, max_s))
