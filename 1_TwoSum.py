class Solution:

    def twoSum(self,nums,target):
        """
        ex1
        """
        result=[]
        for i in range(len(nums)):
            #print("i=",i)
            #print(nums[i])
            diff=target-nums[i]
            #print("diff=",diff)
            for m in range(len(nums)):
                if m==i:
                    continue
                else:
                    if nums[m]==diff:
                        result.append(i)
                        result.append(m)
                    
                    else:
                        continue
            if result: # not a blank list; if blank, the value is 'False'
                break
        #print(result)
        return(result)
