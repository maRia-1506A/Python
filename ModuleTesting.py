# import Module
import Module as mod


mod.z()
mod.x()
mod.y()
print(mod.person1["country"])


# specific module call
from Module import person1
print(person1,"\n")


from Module import x
x()
