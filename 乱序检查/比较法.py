def sorted_string(s1,s2):
     list_s1=list(s1)
     list_s2=list(s2)

     list_s1.sort()
     list_s2.sort()

     pos1=0
     mtch=True
     while pos1<len(s1):
          if list_s1[pos1]==list_s2:
               pos1+=1
          else:
              mtch=False

     return mtch
