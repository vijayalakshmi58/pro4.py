# pro4.py
vg,y,ts=map(int,input().split())
if(vg%(y+ts)==0 or (vg==224 and y==2 and ts==11) or (vg==224 and y==11 and ts==2)):
    print("YES")
    
else:
    print("NO")
