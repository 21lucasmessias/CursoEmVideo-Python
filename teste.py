# a, b = 0, 1
# for i in range(0, 10):
#     print(a)
#     a, b = b, a + b
#

#
# def fib(num):
#     a, b = 0, 1
#     for i in range(0, num):
#         yield f'{i + 1:<2}: {a:<2}'
#         c = a
#         a = b
#         b = b + c
#
#
# for item in fib(10):
#     print(f'{item}')

# from random import randint
#
#
# class Employee:
#     employeers_list = list()
#
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age
#         self.employeers_list.append(self)
#
#     def __repr__(self):
#         return self.full_name
#
#     @property
#     def full_name(self):
#         return f'{self.first} {self.last}'
#
#     @property
#     def email(self):
#         return f'{self.first}.{self.last}@mail.com'
#
#
# class Enginner(Employee):
#     enginner_list = list()
#
#     def __init__(self, first, last, age, lan):
#         super().__init__(first, last, age)
#         self.lan = lan
#         self.enginner_list.append(self)
#
#
# emp_1 = Enginner('Lucas', 'Messias', 21, 'C')
# emp_2 = Enginner('Diogo', 'Messias', 26, 'Python')
# emp_3 = Employee('Tibursio', 'Jose', 50)
# emps = list()
# for i in range(5):
#     emps.append(i)
#     n_first = f'emp_'
#     n_last = str(i)
#     emps[i] = Enginner(n_first, n_last, randint(18, 50), 'Python')


