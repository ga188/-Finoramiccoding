class Solution:
    # @param A : Array of strings
    # @return a list of list of integers
    def anagrams(self, A):
        Arr=list(A)
        for i in range(0, len(A)):
            Arr[i] = A[i]
            ascii = 0
            for j in Arr[i]:
                ascii = ord(j)+ ascii
            Arr[i]= ascii
#print A
        C=[10]
        for i in range(0,len(Arr)):
#   D= A.count(A[i])
            G= Arr[i]
            if G!= 0:
                B=[10]
                for c in range(0, Arr.count(Arr[i])):
                    B.append(Arr.index(G)+1)
                    Arr[Arr.index(G)]= 0
                B.remove(B[0])
                C.append(B)
        print C[1:]
#print C
