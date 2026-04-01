def isHappy(n):
    all=[]
    while True:
        sum=0
        for i in str(n):
            sum= sum+int(i)**2
        if sum==1:
            return True
        else:
            if sum in all:
                return False
            all.append(sum)
            n=sum
if __name__ == "__main__": 
    sample0_output = isHappy(19) 
    sample1_output = isHappy(2) 

    with open("/app/bind_mount/output.txt", "w") as f: 
        f.write(f"19: {sample0_output}\n") 
        f.write(f"2: {sample1_output}\n") 
    print("Results saved to /app/bind_mount/output.txt") 
