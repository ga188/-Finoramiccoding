class Solution:    
    # @param A : list of integers
    # @param B : integer
    # @return classan integer
    def threeSumClosest(self, A, B):
        lis = []
        for i in range(0, len(A)):
            for j in range(i+1,len(A)):
                for k in range( j+1, len(A)):
                    lis.append(A[i]+ A[j]+ A[k])
        return Nearest[lis, B][[1]]    
            
                    
        
                    
                    
                
                
    
