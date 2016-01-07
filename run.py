

def solution(A):
        for i in range(1,len(A)):
                present=0;

                for j in range( 0 , len(A) ):
                        if i == A[j]:
                                A.remove(i)
                                present=present+1
                                break
                if present==0:
                        return i


