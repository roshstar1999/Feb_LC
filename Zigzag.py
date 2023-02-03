class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans=[[0]*(numRows)]*numRows
        if len(s)<=numRows:
            return s
        
        j,k=0,0
        while k<len(s):
            i=0

            while i<numRows and k<len(s)  :
                ans[i][j]=s[k]
                k+=1
                i+=1
            if i==numRows:
                i-=1
                while i>=0 and k<len(s)  :
                    ans[i][j]=s[k]
                    k+=1
                    i-=1
                    j+=1
        fin=""
        for i in range(0,len(ans)):
            for j in range(0,len(ans[0])):
                if ans[i][j]!=0:
                    fin+=ans[i][j]
        return fin
