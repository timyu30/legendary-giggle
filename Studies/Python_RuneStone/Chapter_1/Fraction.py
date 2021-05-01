def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n

class Fraction:
    def __init__(self, top, bottom):
        new_gcd = gcd(top,bottom)
        self.num = top/new_gcd
        self.den = bottom/new_gcd
        if ( not top%1==0 or not bottom%1==0):
          raise RuntimeError('you did not use an int')
        
    # def __str__(self):
    #     return "{:d}/{:d}".format(int(self.num), int(self.den))

    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den

        return first_num == second_num

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den \
        + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        cmmn = gcd(new_num, new_den)
        return Fraction(new_num // cmmn, new_den // cmmn)

    def show(self):
        return "{:d}/{:d}".format(int(self.num), int(self.den))

    def get_num(self):
      return int(self.num)

    def get_den(self):
      return int(self.den)

    def __sub__(self, other_fraction):
      new_num = int(self.num*other_fraction.den) - int(self.den*other_fraction.num)
      new_den = int(self.den * other_fraction.den)
      new_gcd = gcd(new_num, new_den)
      return Fraction(int(new_num/new_gcd), int(new_den/new_gcd))

    def __mul__(self, other_fraction):
      return Fraction((self.get_num() * other_fraction.get_num()), (self.get_den() * other_fraction.get_den()))
      
    def __truediv__(self, other_fraction):
      return (self.get_num()/self.get_den())/(other_fraction.get_num()/other_fraction.get_den()) 

    def __gt__(self, other_fraction):
      return (self.num/self.den)>(other_fraction.num/other_fraction.den)

    def __ge__(self, other_fraction):
      return (self.num/self.den)>=(other_fraction.num/other_fraction.den)

    def __radd__(self, other_fraction):
      new_num = self.num * other_fraction.den + self.den * other_fraction.num
      new_den = self.den * other_fraction.den
      cmmn = gcd(new_num, new_den)
      return Fraction(new_num // cmmn, new_den // cmmn)
    
    def __iadd__(self, other_fraction):
      new_num = self.num * other_fraction.den \
      + self.den * other_fraction.num
      new_den = self.den * other_fraction.den
      cmmn = gcd(new_num, new_den)
      return Fraction(new_num // cmmn, new_den // cmmn)

    #def __str__(self):
    #  return f'Fraction num is {self.get_num()} and den is {self.get_den()}'

    def __repr__(self):
      return f'Fraction(top={self.get_num()}, bottom={self.get_den()})'

class frac_2:
  def __init__(self, top, bot):
    self.num = top 
    self.den = bot
      

test_fraction=Fraction(11,-12)
print(test_fraction.get_num())
print(test_fraction.get_den())

test_fraction2=Fraction(55,-44)
print(test_fraction2.show())

f1 = Fraction(1,-2)
f2 = Fraction(1,4)
print(f1-f2)
print(f1*f2)
print(f1/f2)

print(f2>f1)
print(f1>f2)

error_fraction=Fraction(1, -2)

f3 = frac_2(1,3)
print(f1+f3)
f4 = frac_2(1,4)
print(f4+f1)

f1 += Fraction(1,7)
print(f1)