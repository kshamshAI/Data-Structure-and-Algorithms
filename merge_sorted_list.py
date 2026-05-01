def mergeTwoLists(list1, list2):
         m = len(list1)
         n = len(list2)
         result = []
         m = len(list1)
         n = len(list2)
         i = 0
         j = 0
         while i<m and j<n:
            if list1[i] <= list2[j]:
               result.append(list1[i])
               i+=1
            else:
               result.append(list2[j])
               j+=1
         if i<m:
            while(i<m):
               result.append(list1[i])
               i+=1
         if j<n:
            while(j<n):
               result.append(list2[j])
               j+=1
         return result