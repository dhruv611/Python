import time as t
import random as r

def main():
    target = r.randint(2,10)
    x = input('Press enter to start the game.')
    y = t.time()
    z = input('Press enter after {} secs.'.format(target))
    w = t.time() - y
    if w == target:
        print('Perfect Timing! because you pressed enter after {} secs.'.format(w))
    elif w < target:
        print('Too Fast! because you pressed enter after {} secs.'.format(w))
    else:
        print('Too Slow! because you pressed enter after {} secs.'.format(w))

if __name__ == "__main__" : main()
