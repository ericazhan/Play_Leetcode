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

   
    def reverse(self, x: int) -> int:
        xx=str(x)
        tot=len(xx)
        s=""
        for i in range(tot):
            s=s+xx[(tot-1)-i]
            ss=int(s.split("-")[0])
        if x<0:
            ss=-1*ss
            if ss<=-2**31:return 0
        elif ss>2**31: return 0
        return ss
    
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            new_x=int(str(x)[::-1])
            if new_x==x:
                return True
            else:
                return False
