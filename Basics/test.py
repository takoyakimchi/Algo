f = open('test.txt', 'w')

num = 1000
f.write(str(num) + '\n')

for _ in range(num // 2):
    f.write('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz\n')
    f.write('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n')

f.write('\n')
f.close()