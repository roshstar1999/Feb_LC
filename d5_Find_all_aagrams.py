def findAnagrams(self, s: str, p: str) -> List[int]:
        start=0
        ptr=0
        hash={}
        plen=len(p)
        slen=len(s)
        ans=[]
        matched=0
        
        if slen < plen:
            return ans

        for i in p:
            if i not in hash:
                hash[i]=0
            
            hash[i]+=1
    


        for i in range(slen):


            if slen-start < plen:
                return ans
            
           
            if s[i] in hash :

                hash[s[i]]-=1

                if hash[s[i]]==0:
                    matched+=1
            if matched==len(hash):
                ans.append(start)

            if i>=plen-1:
                lc=s[start]
                if lc in hash:
                    if hash[lc]==0:
                        matched-=1
                    hash[lc]+=1
                start+=1
            '''
                

                    

                else:
                    hash[s[start]]+=1
                    start+=1
                ptr+=1
            else:
                start,ptr=i+1,i+1
            
            if ptr-start==plen:
                for i in hash.keys():
                    if hash[i]!=0:
                        break
                    
                
                ans.append(start)
                start+=1
            '''
        return ans
