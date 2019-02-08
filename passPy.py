# def a(**kwargs):
#     print(kwargs)
#
# def b(*args):
#     print(args)
#
# a(a=1,b=2,c=3)
# b(1,2,3)



class a:
    def __init__(self, name):
        print(name)

class b(a):
    def __init__(self):
        a.__init__(self, 'amit')
    pass
a=[1,2,3,4]
[j,c,d,f] = a
#o = b()
t=(6,7,8,9)
(s1,s2,s3,s4) = t

m={11,12,13}
#{s,d,c}=m

print(d)

cs = {}
cs=t
print(cs)

print(s1)
print(j)

my_list = [[1, 4], (2, 2), {5, 1}]
lists = dict(my_list)
print(lists)  # Prints {5:1,2:2}
