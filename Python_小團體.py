def find_group(alist):
    v=[] 
    g=[] 
    k=[]
    a=0
    for i in range(0, num):
        v.append(0)   
    for j in range(0, num):
        if v[j]==0:
            if j==alist[j]:
                v[j]=1
                k.append({j})
                a+=1
            else:
                group=j
                while v[group]==0:
                    g.append(group)
                    v[group]=1
                    group=alist[group]
                k.append(set(g))
                g.clear()
                a+=1
    return a, k

while True:
    ppl=input("輸入好友個數")  
    try:
        ppl = int(ppl)
        if ppl <= 0:  
            print("請輸入正整數")
            continue
        num = int(ppl)
        break
    except ValueError:
        print("非整數，請再輸入一次")
alist=[]


while ppl>0:              
    friend=input("依次輸入每個人最好的朋友編號(輸入完請按Enter)")
    try:
        friend=int(friend)
        if friend < 0:  
            print("請輸入正整數")
            continue
        if friend >= num:
            print("此編號不存在")
            continue
        if friend in alist:
            print("以輸入過此編號")
            continue
        alist.append(friend)
        ppl -= 1    
    except ValueError:
        print("非整數，請再輸入一次")

a, k = find_group(alist)
print("共有{0}組\n{1}".format(a, k))