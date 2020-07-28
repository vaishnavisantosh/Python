from sys import argv

filename, name, address = argv

print "my name is",name
print "address:",address
print "file on which working on:",argv[0]
print "argv",argv

#upacking ---> same as destructuring in js