# a=lambda x: x * 3
# print(a(5))

# b=(lambda x:x+4 )(2)
# print(b)

#iteration of lambda function
# list1=[1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda x:x %2==0,list1)))

#
# list2=[2,3,4]
# print(list(map(lambda x:x**2,list2)))
# list1=[]
# a=int(input("enter a number : "))
# list1.append(a)
# print(list(map(lambda x:x**2,list1)))
#
# def outer():
#     def inner():
#         a=100
#         return a
#     return inner
# # print(outer())
# new=outer()
# print(new())


def hi():
    x = 100
    def hello():
        nonlocal x
        x=120
        print("inside ",x)
    hello()
    print("outside", x)
hi()

