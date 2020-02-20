#String methods
var = "PrOgRaMiZ"
print(var.lower())
print(var)

print(var.upper())
print(var)
var = var.upper()
print(var)


var = "This will split all words into a list".split()
print(var)

var = ' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string'])
print(var)

var = 'Happy New Year'.find('ew')
print(var)

var = 'Happy New Year'.replace('Happy','Brilliant')
print(var)