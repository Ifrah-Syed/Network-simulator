import random
s=[]
r=[]
st=[]
ft=[]
print("WELCOME TO ALOHA PROTOCOL IMPLEMENTATION\n")
n=int(input("Enter number of connections you want to form to send data through\n"))
k=[0]*n
print("ENTER SENDER AND CORRESPONDING RECEIVER - enter 1 for client 1, 2 for client 2 and so on..... \n ")
for i in range(n):
    a=int(input("Enter sender\n"))
    s.append(a)
    b=int(input("Enter receiver\n"))
    r.append(b)

for i in range(n):
    start=int(input("Enter start time when frame is sent from node "+str(s[i])+'\n'))
    st.append(start)
t=3
for i in range(n):
    finish=st[i]+t
    ft.append(finish)
st.sort()
ft.sort()
i=0
j=i+1
while(len(st)>1):
    print("Sending frame from node "+str(s[i])+" to "+str(r[i]))
    if ft[i]>st[j]:
        print("Collision Occured")
        nk=k[0]+1
        k[0]=nk
        if k[i]>15:
            print("Frame "+str(i)+"is aborted as tries has exceeded 15")
        ra=random.randint(0,2**k[i]-1)
        del(st[i])
        del(ft[i])
        del(k[i])
        st.append(ra)
        st.sort()
        ke=st.index(ra)
        ft.insert(ke,ra+t)
        k.insert(ke,nk)
        print("Time slots at trial" + str(k[i] + 1))
        print(st)
        print(ft)
        m=s[i]
        n=r[i]
        del(s[i])
        del(r[i])
        s.insert(ke,m)
        r.insert(ke,n)
    else:
        print("No Collision has occured")
        print("Frame delivered from "+str(s[i])+" to "+str(r[i])+" at trial "+str(k[i]+1))
        print("Time slots at trial" + str(k[i] + 1))
        print(st)
        print(ft)
        del(st[i])
        del(ft[i])
        del(s[i])
        del(r[i])
        del(k[i])
if len(st)==1:
    print("Sending frame from node "+str(s[0])+" to "+str(r[0]))
    print("No collision occured")
    print("Frame delivered from "+str(s[0])+" to "+str(r[0])+" at trial "+str(k[0]+1))

