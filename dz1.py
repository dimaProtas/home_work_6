# Д\З № 1 Список кортежей адрес, тип, ресурс

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    addr_sum = []
    listt_nginx = []
    for line in f:

        r_addr = line.split(' - - ')[0]
        rtr = line.split('"')[1]
        r_type = rtr.split()[0]
        r_resourc = rtr.split()[1]
        # listt_nginx.append(r_addr)
        # listt_nginx.append(r_type)
        # listt_nginx.append(r_resourc)

        listt_nginx.append((r_addr, r_type, r_resourc))
        addr_sum.append(r_addr)
print(listt_nginx)



# Д\З № 2 IP спамера и количество запросов
from collections import Counter
spam_addr = Counter(addr_sum)
print(spam_addr.most_common()[0])







        # remote_addr = f.readline().split(' - - ')[0]
        # request_type_resourc = f.readline().split('"')[1]
        # request_type = request_type_resourc.split()[0]
        # request_resourc = request_type_resourc.split()[1]
        # print(f'{remote_addr}, {request_type}, {request_resourc}')
        # print(request_type)
        # print(request_resourc)

    # line = f.readline()
    # print(line.strip(), f.tell(), sep='[]')
    # f.seek(17)
    # print(f.readline().strip())
    # f.seek(43)
    # print(f.readline().strip())

