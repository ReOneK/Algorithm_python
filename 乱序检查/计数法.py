def count_string(s1,s2):
     c1=[0]*26
     c2=[0]*26


     for i in range(len(s1)):
          pos=ord(s1[i])-ord('a')
          c1[pos]+=1

     for i in range(len(s2)):
          pos=ord(s1[i])-ord('a')
          c2[pos]+=1

     match=True
     j=0

     while j<26 and match:
          if c1[j]==c2[j]:
               j+=1
          else:
               match=False

     return  match
