# Fibonacci Series
#
# This is a Fibonacci Series Generator. It will create Fibonacci upto the term specified

Fibonacci <- function(n) {
  a<-0
  b<-1
  count <- 2
  if(n == 1) {
    print(a)
  } else {
    print(a)
    print(b)
    while(count < n) {
      c = a + b
      print(c)
      a = b
      b = c
      count = count +1
    }
  }
}
