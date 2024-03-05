#脚本很菜,各位师傅见谅XwX
from typing import final
import string

def realHex(num):
    if num <16:
        return "%0"+hex(num)[2:] 
    else:
        return '%'+hex(num)[2:]
pattern=input("请输入正则过滤式,没有则直接回车跳过\n")
#正则表达式修饰符re.I大小写不敏感,re.M多行匹配,影响^和$,re.S使得.匹配包括换行在内的所有字符,re.U根据Unicode字符集解析字符,影响\w,\W,\b,\B
#建议回车跳过,这个功能很逊
if pattern != "":
    import re
    blacklist=["`","'",'"',"\\"]
    for i in range(32,255):
        if  re.search(pattern,chr(i),re.I):
            blacklist.append(chr(i))
else:
    #blacklist列表中的字符在生成的拼接字符串中不会被使用,除了部分是被过滤掉的字符，其余的如',"等字符考虑可能会导致闭合等问题暂列入
    #如果有其他的要求可以对blacklist列表进行删改
    #!注意对于|和&来说拼凑字符是相当困难的,并且可用范围实际上是31-255,这就导致了要这样用必须引号包裹,否则大概率GG
    #比如{,},;,|,&,$等诸多符号不带引号会导致无法使用
    blacklist=[]
    for word in string.ascii_letters+string.digits:
        blacklist.append(word)
    blacklist+=[" ","^","~","|","'",'"',"\\"]
#print(blacklist)
#不同于取反,一个目标字符串使用异或的方式可以获大量的可用拼接字符串,这里只取了1种组合的拼接字符串
#如果需要获得更多拼接字符串查看该函数中的result列表

def yiHuo(string):
    global operationEffient
    global blacklist
    operationEffient=False
    result=[]
    finalstr='""^""'
    rawstr=string
    for i in range(0,len(rawstr)):
        result.extend([[]])
    for k in range(0,len(rawstr)):
        #这里更换范围
        for i in range(1,255):
           if(chr(i) not in blacklist):
               #这里更换范围
                for j in range(1,255):
                    if(chr(j) not in blacklist):
                        if(i^j==ord(rawstr[k]) and [hex(j).replace('0x',"%"),hex(i).replace('0x',"%")] not in result[k]):
                            result[k].extend([[realHex(i),realHex(j)]])
    #在这里往下的函数部分,result列表均是可用的(已填充了获得的拼接字符串)
    for i in range(0,len(result)):
        if(len(result[i])==0):
            return("该字符在现有黑名单和字符范围下无法拼接出->%s"%(rawstr[i]))
    for i in range(0,len(rawstr)):
        finalstr=finalstr[:finalstr.find("^",0)-1]+result[i][0][0]+'"'+finalstr[finalstr.find("^",0):]
        finalstr=finalstr[:finalstr.rfind("'",0)]+result[i][0][1]+finalstr[finalstr.rfind('"',0):]   
    return finalstr
def quFan(string):
    global operationEffient
    global blacklist
    operationEffient=False
    result=[]
    finalstr='~""'
    rawstr=string
    for i in range(0,len(rawstr)):
        result.extend([[]])
    for k in range(0,len(rawstr)):
        #这里更换范围
        for i in range(1,255):
           if(chr(i) not in blacklist and chr(int(bin(~i & 0xFF)[2:],2))==rawstr[k]):
               result[k].extend([realHex(i)])
    #print(result)
    for i in range(0,len(result)):
        if(len(result[i])==0):
            return("该字符在现有黑名单和字符范围下无法拼接出->%s"%(rawstr[i]))
    for i in range(0,len(rawstr)):
        finalstr=finalstr[:finalstr.rfind('"',0)]+result[i][0]+finalstr[finalstr.rfind('"',0):]
    return finalstr
def rce_and(string):
    global operationEffient
    global blacklist
    operationEffient=False
    rawstring=string
    result=[]
    finalstr=""
    for i in range(0,len(rawstring)):
        result.extend([[]])
    for l in range(0,len(rawstring)):
        for i in range(1,255):
            for j in range(1,255):
                if (chr(j) in blacklist) or (chr(i) in blacklist):
                    continue
                if chr(i&j)==rawstring[l]:
                    #注意&在URL特殊含义,故需要URL编码
                    result[l].append("\""+realHex(i)+"\"%26\""+realHex(j)+"\"")
                    continue
    for i in range(0,len(result)):
        if(len(result[i])==0):
            print("该字符在现有黑名单和字符范围下无法拼接出->%s"%(rawstring[i]))
            return
    for i in range(0,len(result)):
        if i == 0:
            finalstr+="({})".format(result[i][0])
        else:
            finalstr+=".({})".format(result[i][0])      
    return finalstr
def rce_or(string):
    global operationEffient
    global blacklist
    operationEffient=False
    rawstring=string
    result=[]
    finalstr=""
    for i in range(0,len(rawstring)):
        result.extend([[]])
    for l in range(0,len(rawstring)):
        for i in range(1,255):
            for j in range(1,255):
                if (chr(j) in blacklist) or (chr(i) in blacklist):
                    continue
                if chr(i|j)==rawstring[l]:
                    result[l].append("\""+realHex(i)+"\"|\""+realHex(j)+"\"")
                    continue
    for i in range(0,len(result)):
        if(len(result[i])==0):
            print("该字符在现有黑名单和字符范围下无法拼接出->%s"%(rawstring[i]))
            return
    for i in range(0,len(result)):
        if i == 0:
            finalstr+="({})".format(result[i][0])
        else:
            finalstr+=".({})".format(result[i][0])      
    return finalstr
while(True):
    operationEffient=True
    target=input("请输入待转换字符\n")
    while(operationEffient):
        operation=input("请选择操作\n0->重新输入\n1->使用异或拼接\n2->使用取反获得\n3->使用二进制和\n4->使用二进制或\n")
        if(operation=="1"):
            result=yiHuo(target)
            pass
        elif(operation=="2"):
            result=quFan(target)
            pass
        elif(operation=='3'):
            result=rce_and(target)
            pass
        elif(operation=='4'):
            result=rce_or(target)
            pass
        elif(operation=="0"):
            break
        else:
            print("选择的操作无效")
            continue
        if result!='':
            print(result)
