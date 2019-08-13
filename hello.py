print("Hello Python")
x = 23.6
if x == 1:
    # indented four spaces
    print("x is 1.")
else:
    print("x is NOT 1.")

floatv = float(55)
print "my float value is", floatv

intv = float(55.26)
print "my integer value is", intv

round2 = round(55.2352356,2)
print "my rounded value is", round2

amount = 1000
balance = 10
print("my salary is %s but now in my account %s" % (amount, balance))
print("my salary is {} but now in my account {}".format(amount, balance))
concatString = "my salary is {} but now in my account {}".format(amount, balance)
print (concatString)

a,b,c = 6,4,"Three"
print "a is {} and b is {} and c is {}".format(a,b,c)

if isinstance(x,float) :
    print "X is float"

if isinstance(x,float) and x ==23.6 :
    print "X is float and value is 23.6"

if isinstance(x,float) and x ==23.6 :
    print "X is float and value is %f " % x 