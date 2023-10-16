first=-1
last=-1
def fisrtAndLast(arr,index,first,last,ele):
    if(index==len(arr)):
      return [first,last]
    if(arr[index]==ele):
        if  first==-1:
            first=index
        else:
            last=index
    return fisrtAndLast(arr,index+1,first,last,ele)
 
data="bacvahdgfvadggahaaaagah"   
print(fisrtAndLast(data,0,-1,-1,'a'))
        
