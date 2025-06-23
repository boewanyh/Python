"""
字典
"""
# 创建
person = {
    'name': 'wanyh',
    'age': 22,
    'height': 177,
    'weight': 54,
    'addr': '安徽合肥',
    'car': {
        'model': '本田',
        'year': 2021
    }
}
print(person)

person2 = dict(name='wanyh', age=22, height=177, weight=54, addr='安徽合肥')
print(person2)

items = dict(zip('ABCD', '1234'))
print(items) # {'A': '1', 'B': '2', 'C': '3', 'D': '4'}

# 成员运算
print('name' in person)

# 索引运算
print(person['name'])
person['birth'] = '1993-04-05'
print(person)

# 方法
print(person.get('name'))
print(person.get('other', 'lumia')) # 指定默认值
print(person.keys()) # dict_keys(['name', 'age', 'height', ...])
print(person.values()) # dict_values(['wanyh', 22, 177, ...])
print(person.items()) # dict_items([('name', 'wanyh'), ('age', 22), ('height', 177), ...])

print(person.pop('name'))
print(person)
print(person.popitem()) # ('birth', '1993-04-05')
print(person)
del person['age']
person.clear() # 清空

# 遍历
print(len(person))
for key in person:
    print(f'{key}: {person[key]}')

for key, value in person.items():
    print(f'{key}: {value}')

# update |
person1 = {'name': 'wanyh', 'age': 22}
person2 = {'age': 32, 'height': 177}
person1.update(person2)
person1 |= person2
print(person1) # {'name': 'wanyh', 'age': 32, 'height': 177}