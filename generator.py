from functools import reduce
from math import sqrt, log10
from IPython.display import clear_output
import json


def sum_divisors(n, t=False):
    if n in [0, 1]:
        return 0
    step = 2 if n % 2 else 1
    if t:
        return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))
    return sum(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))) - n


def sum_divisors_sequence(num, t=False):
    n = num
    sequence = [n]
    while sum_divisors(n) not in sequence:
        digits = int(log10(n)) + 1
        if digits >= 13:
            sequence.append('break')
            break
        sequence.append(sum_divisors(n))
        if t:
            print(sum_divisors(n), end=', ')
        n = sum_divisors(n)
#     sequence.append(sum_divisors(n))
    
    return sequence


def generate():
  loop_start = [0]
  loop_tracker = {}
  
  for i in range(1000000):
      if i % 100 == 0: print(i)
  #     clear_output(wait=True)
      sequence = sum_divisors_sequence(i)
      if sequence[-1] not in [0, 'break']:
          if sum_divisors(sequence[-1]) not in loop_start:
              start = sum_divisors(sequence[-1])
              end = sequence[-1]
              length = len(sequence[sequence.index(start):])

              if f'Loop Length {length}' not in loop_tracker.keys():
                  loop_tracker[f'Loop Length {length}'] = [0, []]

              if length == 2:
                  if [end, start] not in loop_tracker[f'Loop Length {length}'][-1]:
                      loop_tracker[f'Loop Length {length}'][-1].append([start, end])
              else:
                  loop_tracker[f'Loop Length {length}'][-1].append(start)

              loop_tracker[f'Loop Length {length}'][0] += 1
              loop_start.append(start)

              clear_output(wait=True)
              print(loop_start[-1])
              print(json.dumps(loop_tracker, indent=4, sort_keys=True))


generate()
