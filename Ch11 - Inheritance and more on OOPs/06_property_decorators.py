class Employee:

    def name(self):
        return self.ename
    
e = Employee()
e.ename = "Harry"

print(e.name())

#Same can be done as:

class Employee:

    @property
    def name(self):
        return self.ename
    
e = Employee()

e.ename = "Harry"
print(e.name)

# See how instead of e.name(), we just printed e.name with @property.
# e.name() -> looks like function
# e.name   -> looks like a simple attribute.

# Basically, @property lets you use a function like a variable.