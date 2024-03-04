"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y



def subquadratic_multiply(x, y):
    ### TODO
  if len(x.binary_vec) < 2 or len(y.binary_vec) < 2:
    return BinaryNumber(x.decimal_val * y.decimal_val)

  # Pad the binary vectors if necessary
  x.binary_vec, y.binary_vec = pad(x.binary_vec, y.binary_vec)

  # Split x and y into halves
  xL, xR = split_number(x.binary_vec)
  yL, yR = split_number(y.binary_vec)

  # Recursive calls for three parts of the Karatsuba algorithm
  A = subquadratic_multiply(xL, yL)  # xL * yL
  B = subquadratic_multiply(xR, yR)  # xR * yR

  # (xL + xR) * (yL + yR)
  xL_plus_xR = BinaryNumber(xL.decimal_val + xR.decimal_val)
  yL_plus_yR = BinaryNumber(yL.decimal_val + yR.decimal_val)
  C = subquadratic_multiply(xL_plus_xR, yL_plus_yR)

  # Middle term calculation
  mid_term = C.decimal_val - A.decimal_val - B.decimal_val

  # Combine the three parts using the Karatsuba algorithm
  result = A.decimal_val * (1 << (len(x.binary_vec))) + mid_term * (1 << (len(x.binary_vec) // 2)) + B.decimal_val

  return BinaryNumber(result).decimal_val



def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    return (time.time() - start)*1000

    
    

