#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
def get_positive_integer():
  while True:
    try:
      n = int(input("Enter the number of Fibonacci terms you want (positive integer): "))
      if n > 0:
        return n
      else:
        print("Please enter a positive integer greater than zero.")
    except ValueError:
      print("Invalid input. Please enter a valid integer.")

def generate_fibonacci(n):
  sequence = []
  a, b = 0, 1
  for _ in range(n):
    sequence.append(a)
    a, b = b, a + b
  return sequence

def print_fibanacci(sequence):
  print("Fibanacci sequence:", ", ".join(str(num) for num in sequence))

def main():
  terms = get_positive_integer()
  fib_sequence = generate_fibonacci(terms)
  print_fibanacci(fib_sequence)

if __name__ == "__main__":
  main()
