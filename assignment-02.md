# CMPS 2200 Assignment 2

**Name:**______Charles Zhang___________________

In this assignment we'll work on applying the methods we've learned to analyze recurrences, and also see their behavior
in practice. As with previous
assignments, some of of your answers will go in `main.py` and `test_main.py`. You
should feel free to edit this file with your answers; for handwritten
work please scan your work and submit a PDF titled `assignment-02.pdf`
and push to your github repository.


1. Derive asymptotic upper bounds of work for each recurrence below.
  * $W(n)=2W(n/3)+1$
.  
.  $\Theta(n^{log_3 2})$
.  
.  
.  
  * $W(n)=5W(n/4)+n$
.  
.  $\Theta(n^{log_4 5})$
.  
.  
.  
  * $W(n)=7W(n/7)+n$
.  
.  $\Theta(n*log n)$
.  
.  
.  
  * $W(n)=9W(n/3)+n^2$
.  
.  $\Theta(n^2)$
.  
.  
.  
  * $W(n)=8W(n/2)+n^3$
.  
.  $\Theta(n^3)$
.  
.  
.  
  * $W(n)=49W(n/25)+n^{3/2}\log n$
.  
.  $O(n^{3/2}\log n)$
.  
.  
.  
  * $W(n)=W(n-1)+2$
.  
    $O(n)$
.  
.  
.  
  * $W(n)= W(n-1)+n^c$, with $c\geq 1$
.  
.  $O(n^c)$
.  
.  
.  
  * $W(n)=W(\sqrt{n})+1$

$O(log n)$


2. Suppose that for a given task you are choosing between the following three algorithms:

  * Algorithm $\mathcal{A}$ solves problems by dividing them into
      five subproblems of half the size, recursively solving each
      subproblem, and then combining the solutions in linear time.
    
  * Algorithm $\mathcal{B}$ solves problems of size $n$ by
      recursively solving two subproblems of size $n-1$ and then
      combining the solutions in constant time.
    
  * Algorithm $\mathcal{C}$ solves problems of size $n$ by dividing
      them into nine subproblems of size $n/3$, recursively solving
      each subproblem, and then combining the solutions in $O(n^2)$
      time.

    What are the asymptotic running times of each of these algorithms?
    Which algorithm would you choose?

    For algorithm A, $T(n) = 5T(n/2)+O(n)$, which yields running time of $O(n^{log_2 5})$

    For Algorithm B, $T(n) = 2T(n-1)+O(1)$, yields $O(2^n)$

    For Algorithm C, $T(n) = 9T(n/3)+O(n^2)$, yields $O(n^2 log n)$

    I will choose algorithm C as it has the shortest running time.


3. Now that you have some practice solving recurrences, let's work on
  implementing some algorithms. In lecture we discussed a divide and
  conquer algorithm for integer multiplication. This algorithm takes
  as input two $n$-bit strings $x = \langle x_L, x_R\rangle$ and
  $y=\langle y_L, y_R\rangle$ and computes the product $xy$ by using
  the fact that $xy = 2^{n/2}x_Ly_L + 2^{n/2}(x_Ly_R+x_Ry_L) +
  x_Ry_R.$ Use the
  stub functions in `main.py` to implement Karatsaba-Ofman algorithm algorithm for integer
  multiplication: a divide and conquer algorithm that runs in
  subquadratic time. Then test the empirical running times across a
  variety of inputs in `test_main.py` to test whether your code scales in the manner
  described by the asymptotic runtime. Please refer to Recitation 3 for some basic implementations, and Eqs (7) and (8) in the slides https://github.com/allan-tulane/cmps2200-slides/blob/main/module-02-recurrences/recurrences-integer-multiplication.ipynb
 
 


