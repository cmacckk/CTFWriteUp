str1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
str2 = 'KVQP0LdJKRaV3n9D'     # 因本题生成是从后往前，需要反转
str3 = str1[::-1]
res = ''
for i in range(len(str2)):  
    for j in range(len(str1)):
        if str2[i] == str1[j]:
            res+=str(j) + ' ' + str(j) + ' ' + '0' + ' ' + str(len(str1)-1) + ' '
            break
print(res)