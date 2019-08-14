import random
import time
import memory_profiler

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print('Memory (Before): {}Mb'.format(memory_profiler.memory_usage()))
def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person


t1 = time.clock()
people = people_list(1000)
for p in people:
    print(p)
t2 = time.clock()
#
# t1 = time.clock()
# people = people_generator(1000)
# for p in people:
#     print(p)
# t2 = time.clock()

print('Memory (After) : {}Mb'.format(memory_profiler.memory_usage()))
print('Took {} Seconds'.format(t2-t1))
