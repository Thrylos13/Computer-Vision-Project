# # # # # #
# # # # # #
# # # # # # store = [("shirt",20.00),
# # # # # #          ("pants",25.00),
# # # # # #          ("jacket",50.00),
# # # # # #          ("socks",10.00)]
# # # # # #
# # # # # # to_euros = lambda data: (data[0],round(data[1]*0.93,2))
# # # # # # to_dollars = lambda data: (data[0],round(data[1]/0.93,2))
# # # # # # store_euros = list(map(to_euros,store))
# # # # # # store_new = list(map(to_dollars,store))
# # # # # #
# # # # # # price = lambda data:data[1] >= 23
# # # # # #
# # # # # # store_filtered = list(filter(price, store_new))
# # # # # #
# # # # # # for i in store_filtered:
# # # # # #     print(i)
# # # # #
# # # # # import functools      
# # # # # letters = ["H","E","L","L","O"]
# # # # # word = functools.reduce(lambda x,y:x+y,letters)
# # # # # print(word)
# # # # import functools
# # # # factorial = [5,4,3,2,1]
# # # # number = functools.reduce(lambda x,y:x*y,factorial)
# # # # print(number)
# # #
# # # square = [i*i for i in range(1,11)]
# # # print(square)
# # #list comprehension = [ expression for item in iterable if conditional ]
# # for and if/else statement move the conditional before the for loop right after the expression
# # students = [100,90,70,80,60,40,30,10,0]
# # # passed = list(filter(lambda x:x >= 40,students))
# # passed = [i if i >= 60 else "FAILED" for i in students]
# # print(passed[::-1])
# # #dictionary comprehension = {key: expression for (key,value) in iterable}
# for if/else statement instead of expression right the conditional there
# # cities = {'A':20,"B":35,"C":40,"D":30}
# # cities_in_f = {key:((value * 9/5)+(32)) for (key,value) in cities.items()}
# # print(cities_in_f)
#
# weather = {'A':"sunny","B":"snowy","C":"cold","D":"cloudy"}
# sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}
# print(sunny_weather)
#
# cities = {'A':20,"B":35,"C":40,"D":30}
# desc_cities = {key: ("warm" if value >= 30 else "cold") for (key,value) in cities.items()}
# print(desc_cities)
# import time
# print(time.ctime(0))
# print(time.time())
# print(time.ctime(time.time()))
# time_obj = time.localtime()
# print(time_obj)
# import threading
# import time
# # print(threading.active_count())
# # print(threading.enumerate())
# def eat_breakfast():
#     time.sleep(3)
#     print("You eat breakfast")
# def drink_milk():
#     time.sleep(2)
#     print("You drink milk")
# def get_dressed():
#     time.sleep(6)
#     print("You get dressed")
#
# # eat_breakfast()
# # drink_milk()
# # get_dressed()
#
# x = threading.Thread(target=eat_breakfast)
# x.start()
#
# y = threading.Thread(target=drink_milk)
# y.start()
#
# z = threading.Thread(target=get_dressed)
# z.start()
# import threading
# import time
# def timer():
#     count = 0
#     while True:
#         time.sleep(1)
#         count += 1
#         print("logged in for",count,"seconds")
#
# x = threading.Thread(target=timer,daemon=True)
# x.start()
# answer = input("do you wish to exit?")
# from multiprocessing import Process,cpu_count
# import time
# def counter(num):
#     count = 0
#     while count < num:
#         count += 1
# def main():
#     # a = Process(target=counter, args=(500000000,))
#     # a.start()
#     # a.join()
#     #
#     # b = Process(target=counter, args=(500000000,))
#     # b.start()
#     # b.join()
#     #
#     # print("Finished in ",time.perf_counter(),"seconds")
#     print(cpu_count())
# if __name__ == '__main__':
#     main()