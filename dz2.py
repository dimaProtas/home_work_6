# Д\З № 3 Обьеденил два списка с условием

import itertools
import json

with open('user.txt', 'r', encoding='utf-8') as f1:
    with open('hobby.txt', 'r+', encoding='utf-8') as f2:
        content1 = f1.read()
        content2 = f2.read()
        user = [a for a in content1.split('\n')]
        hobby = [i for i in content2.split('\n')]
        user_hobby = {key: value if len(hobby) < len(user) else exit(1) for key, value in itertools.zip_longest(user, hobby)}
        # user_hobby = dict(zip(user, hobby))
        # if not (user or hobby):
        #     return -1
print(user_hobby)
print(len(user))
print(len(hobby))



# Д\З № 4 Записал в файл
with open('user_hobby.txt', 'w', encoding='utf-8') as f:
    json.dump(user_hobby, f, ensure_ascii=False, indent=1)
with open('user_hobby.txt', 'r', encoding='utf-8') as f:
    result = json.load(f)
    print(result)
