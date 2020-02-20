#for
for name in ['Bill', 'Nicole', 'John']:
  print('Hi {}!'.format(name))

#for zip
letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
for l, n in zip(letters, numbers):
    print('Letter:', l)
    print('Number:', n)

#for enum

for ele in enumerate(letters): 
    print(ele)

for count,ele in enumerate(letters):
    print(count,ele)
