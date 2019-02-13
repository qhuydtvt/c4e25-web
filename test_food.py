import mlab
from food import Food

mlab.connect()

# 1. Create 
# 1.1 create a food data
f = Food(title="banh sai", link="<<Link sai>>")
# 1.2 save it
# f.save()

# 2. Read
# 2.1 Get cursor
f_objects = Food.objects() # Lazy loading # Same as list
# 2.2 Process cursor
# f_first = f_objects[0] # Actual data transfering
# print(f_first.title)
# print(f_first.link)

#print(len(f_objects))
# print(f_objects.count())

# for f in f_objects:
#   print(f.title)
#   print(f.link)
#   print("------------------")

# f = f_objects[3]
# # f.update(set__title="Banh rat rat ngon", set__link="Link ngon")
# # f.reload()
# # print(f.title)
# f.delete()

f = f_objects.with_id("5c4d7da21d4f0ce4e58ff4b1") # 1
if f != None:
  f.delete()
  print("OK")
else:
  print("Not found")