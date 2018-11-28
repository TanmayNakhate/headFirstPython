todos = open('new.txt','w')

print('Put out the trash.', file=todos)
print('Feed the cat.', file=todos)
print('Prepare tax return.', file=todos)
print('Study Python.', file=todos)

todos.close()

tasks = open('new.txt')

for chore in tasks:
    print(chore)

tasks.close()


with open('new.txt') as tasks:
    for chore in tasks:
        print(chore, end='')