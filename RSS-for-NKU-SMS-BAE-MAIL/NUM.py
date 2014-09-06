import random
import time

def Code():
    A = (random.random()*1000000)/1
    B = ((int(time.time()))/1000)/1
    
    return ((int(A+B))-int((A+B))%1)