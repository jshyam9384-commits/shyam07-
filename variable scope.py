# 1.local variable
#
# def order():
#     food=input("what food you want?")
#     print("your order is:",food)
#
# order()
#
# 2.enclosing variable
#
# def card():            #outer variable
#     discount=10
#
#     def checkout():   #inner variable(enclosing variable)
#         print("appling your discount",discount)
#
#     checkout()
# card()
#
# simple example
#
# def outer():
#     name="shyam"
#
#     def inner():
#         print(name)
#     inner()
# outer()
#
#
# the variable in the outer function is used in the inner fuction

#3.global variable
#
# user_id="shyam 07"    #global variable
#
# def homepage():
#     print("welcome:",user_id)
#
# def profile():
#     print("welcome to the profile page:",user_id)
# homepage()
# profile

#4.build in
# print(__file__)
