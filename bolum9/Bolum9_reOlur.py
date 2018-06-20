import re
ad="Bulent Cobanoglu, yazar"
m = re.match("(\w+) (\w+)", ad )
print (m.group()) #Bulent Cobanoglu
print (m.groups()) #('Bulent', 'Cobanoglu')
print (m.group(2)) #Cobanoglu
