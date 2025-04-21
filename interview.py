# interview purpose

        # 1.1 Data Types & Structures
        # 💡 Key Concepts:
        # int, float, str, bool

        # list, tuple, dict, set

# num = 4
# point = 4.5
# name = 'Meet'
# result = True

# ls = ['meet','hello',False,105,5.5,1]
# tup = ('tuple','meet','hello',False,5,5.5,99)
# json = {
#     'FirstName':'meet',
#     'LastName':'ashara',
#     'age':222,
#     'height':6.4,
# }



# print(f'this is an tuple :- {tup}')

# for i in json:
#     print(f'{i} : {json[i]}')
    
# pat = {x:x*2 for x in range(1,11)}

# for x in pat:
#     print(f' {x} => {pat[x]} ')

# aset = {1,2,3,4,4}
# aset1 = {1,2,5,4,6}

# print(aset1 - aset)

# p='hello'
# count=0
# for i in p:
#     print(i)
#     count+=1
# print(count)


# def demo(names):
#     update = set(names)
#     up = tuple(update)
#     for i in up:
#         dis={i:len(i)}
#         print(dis)
        
#         for key, value in dis.items():
#             print(key, value)

    
# demo(['maeet','meet','meet','ashara','good'])

    
# def user_report(name,age,skill,**info):
#     print(f'name : {name}')
#     print(f'age : {age}')
#     print(f'skills : {skill}')
#     for key , value in info.items():
#         print(f'{key}:{value}')
# dis={
#     ' city':' Rajkot',
#     'email': 'meet@gmail.com'
# }
# skill=("python , djnaog, js")
# user_report('meet',20,skill,dis)
    

# 1. Class and Object
# def txt(data):
#     with open('data1.txt','a') as f:
#         f.write(data)

# class Human:
#     def __init__(self,name,age,skill):
#         self.name = name
#         self.age = age
#         self.skill= skill 
#     def gret(name):
#         print(f' Hello my buddy {name}')
    
    
        
# class developer(Human):
#     def skilll(self):
#         print(f'welcome back {self.name} your skill is {','.join(self.skill) } your age is {self.age}')
        
# class student:
#     def __init__(self,mark,name,course):
#         self.mark=mark
#         self.name=name
#         self.course=course
#     def is_pass(self):
#         if self.mark >= 40:
#             return True
#         else:
#             return False

# s1 = student(6,'komal','CSE_AIML')
# s2 = student(76,'komalo','CSE')
# s3 = student(46,'komali','IT')
# results =[s1,s2,s3]
# for i in results:
#     status = 'passed' if i.is_pass else 'fail'
#     txt(f'{i.name} of {i.course} is {status} beacuse it is  scored {i.mark}') 
    
    
# def txt(msg):
#     with open('detials.txt','a') as f:
#         f.write(msg)
        
# for i in range(1,3):
#     name = input('Enter your name ')
#     feedback= input('Enter your Feedback ')
#     txt(f'{name} : {feedback} \n')

# with open('detials.txt','r') as f:
#     content = f.read()
#     print(content)
    



# for num in range(1,28):
#     if (num%num==0 and num%1==0):
#         print(f'{num } is prime number')
#     else:
#         print(f'{num} is not a prime number')




