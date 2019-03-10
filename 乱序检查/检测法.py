def check_string(s1,s2):
     list_s2=list(s2)
     pos1=0
     destion1=True
     while pos1<len(s1) and destion1:
          pos2=0
          destion2=False
          while pos2<len(list_s2) and not destion2:
               if s1[pos1]==list_s2[pos2]:
                    destion2=True
                    
               else:
                    pos2+=1


          if destion2==True:
               list_s2[pos2]=None
               pos1+=1
               dection1=True
          else:
               destion1=False

     return  dection1


               
                    
