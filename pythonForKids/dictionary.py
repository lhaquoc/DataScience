dict = {key: value for key, value in [('name', 'Kteam'), ('member', 88)]}
print(dict)
numbers = range(10)
new_dict = {n: n**2 for n in numbers if n % 2 == 0}
print(new_dict)

my_dict = {k: range(0, 100)[k] for k in range(0, 100)}
print(my_dict)
'''
  use class
'''


class Map_Class:
    def keys(self):
        return [1, 2, 3]

    def __getitem__(self, key):
        return key * 2


map_obj = Map_Class()
dic = dict(map_obj)
print(dic)
