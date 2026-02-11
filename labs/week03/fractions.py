
def gcd(a,b):
    if b > a: 
        a,b = b,a
    while b > 0: 
        remainder = a % b 
        a = b 
        b = remainder
    return a

def gcd_rec(a,b):     
    if b == 0: 
        return a
    return gcd_rec(b, a % b)

def gcd(a,b):
    if b > a: 
        a,b = b,a
    return gcd_rec(a,b)

def lcm(a,b):
    return a * b // gcd(a,b)

class Fraction: 

    def __init__(self, numer, denom):
        self.numerator = numer
        self.denominator = denom 
    
    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __mul__(self, other):
        new_numer = self.numerator * other.numerator
        new_denom = self.denominator * other.denominator
        return Fraction(new_numer, new_denom).simplify()

    def __add__(self, other):
        my_lcm = lcm(self.denominator, other.denominator)
        new_self_numer = self.numerator * my_lcm // self.denominator
        new_other_numer = other.numerator * my_lcm // other.denominator
        return Fraction(new_self_numer + new_other_numer, my_lcm)

    def simplify(self): 
        my_gcd = gcd(self.numerator, self.denominator)
        new_numerator = self.numerator // my_gcd
        new_denominator = self.denominator // my_gcd
        #self.denominator = new_denominator
        #self.numerator = new_numerator
        return Fraction(new_numerator, new_denominator)

    def __lt__(self, other):
        my_lcm = lcm(self.denominator, other.denominator)
        new_self_numer = self.numerator * my_lcm // self.denominator
        new_other_numer = other.numerator * my_lcm // other.denominator
        #if new_self_numer < new_other_numer: 
        #    return True
        #return False 
        return new_self_numer < new_other_numer
    
    def __eq__(self, other):
        my_lcm = lcm(self.denominator, other.denominator)
        new_self_numer = self.numerator * my_lcm // self.denominator
        new_other_numer = other.numerator * my_lcm // other.denominator 
        return new_self_numer == new_other_numer

    def __le__(self, other):
        return self < other or self == other

if __name__ == "__main__":
    f1 = Fraction(1,4)
    f2 = Fraction(1,3)   
    f3 = Fraction(2,5)
    f4 = Fraction(7,10)

    li = [f1,f2,f3,f4]
    li.sort()
    print(li)
    #f3 = f1 + f2 # f1.__add__(f2)
    #rint(f3)


    
  
