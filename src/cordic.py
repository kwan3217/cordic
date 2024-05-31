"""
Implementation of the CORDIC algorithm

Created: 5/31/24
"""


def fac(n:int):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def sin_taylor1(theta:float,max_n:int=6):
    """
    Calculate the sine of a variable via the Taylor series expansion
    :param theta: Input angle in radians
    :param n: Number of terms, not counting the absent even terms. Default is 6, which uses theta^11/11! as its last term
    :return: sine of the angle

    For sine, the Taylor series is:

    $$\sum_{n=0}^\infty \frac{(-1)^n \theta^{2n+1}}{(2n+1)!}$$

    This uses the series formula exactly as-is, with each term calculated from scratch.
    """
    result=0
    for n in range(max_n):
        numa=(-1)**n
        numb=theta**(2*n+1)
        num=numa*numb
        den=fac(2*n+1)
        term=num/den
        result+=term
    return result


def sin_taylor2(theta:float,n:int=6):
    """
    Calculate the sine of a variable via the Taylor series expansion
    :param theta: Input angle in radians
    :param n: Number of terms, not counting the absent even terms. Default is 6, which uses theta^11/11! as its last term
    :return: sine of the angle

    For sine, the Taylor series is:

    $$\sum_{n=0}^\infty \frac{(-1)^n \theta^{2n+1}}{(2n+1)!}$$

    But, each term can be built on the previous term with a couple of multiplies and divides.
    * Each term is multiplied by -theta^2
    * Each term is divided by the next two integers
    So, we can track an accumulator which will eventually hold the final answer,
    a term, and a next integer counter.
    """
    term=theta
    acc=term
    j=1
    mtheta2=-theta*theta
    for i in range(n-1):
        j+=1
        term/=j
        j+=1
        term/=j
        term*=mtheta2
        acc+=term
    return acc


_rfacs=[1.0/(2*n*(2*n+1)) for n in range(1,6)]
def sin_taylor3(theta:float):
    """
    Calculate the sine of a variable via the Taylor series expansion
    :param theta: Input angle in radians
    :param n: Number of terms, not counting the absent even terms. Default is 6, which uses theta^11/11! as its last term
    :return: sine of the angle

    For sine, the Taylor series is:

    $$\sum_{n=0}^\infty \frac{(-1)^n \theta^{2n+1}}{(2n+1)!}$$

    But, each term can be built on the previous term with a couple of multiplies and divides.
    * Each term is multiplied by -theta^2
    * Each term is divided by the next two integers
    In this one, we pre-calculate a table of reciprocals. Each one is
    the one to multiply the term to get the effect of dividing by the next
    2 integers -- IE _rfac[0]=1/6,rfac[1]=1/(4*5)=1/20,rfac[2]=1/(6*7)=1/420, etc.
    """
    term=theta
    acc=term
    mtheta2=-theta*theta
    for rfac in _rfacs:
        term*=rfac
        term*=mtheta2
        acc+=term
    return acc



def main():
    pass


if __name__ == "__main__":
    main()
