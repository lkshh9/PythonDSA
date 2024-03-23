# x = [1,"abcd",2,"efgh",[3,4]]
# print(x)

# y = x[0:6]        
# print(y)             
# z = x                          
# w = y                          
# x[1] = x[1][0:3] + 'd'         
# print(x[1])
# y[2] = 4             
# print(y)          
# # z[1][1:3] = 'yzw'        # strings are immutable 

# z[0] = 0  
# print(z)                     
# w[4][0] = 1000    
# print(w)             
# a = (x[4][1] == 4) 
# print(a)

# x = [423,'b',37,'f']
# u = x[1:]
# y = u
# w = x
# print(w)
# u = u[0:]
# print(u)
# u[1] = 53
# print("y = ", y)
# x[2] = 47
# print(w)

# print(x[2] , y[1], w[2] , u[1] )

# first = "tarantula"
# second = ""
# for i in range(len(first)-1,-1,-1):
#   second = first[i] + second
#   print(second)


def mystery(l):
  l = l[0:5]
  print(l)

list1 = [44,71,12,8,23,17,16]
mystery(list1)  
print(list1)


