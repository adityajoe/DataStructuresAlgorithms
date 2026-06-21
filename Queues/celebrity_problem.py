# A celebrity is a person who is known to all but does not know anyone at a party. A party is being organized by some people. A square matrix mat[][] of size n*n is used to represent people at the party such that if an element of row i and column j is set to 1 it means ith person knows jth person. You need to return the index of the celebrity in the party, if the celebrity does not exist, return -1.

class Solution:
    def celebrity(self, mat):
        # code here
        for i in range(len(mat)):
            col_sum = 0
            row = mat[i]
            # print(row)
            if sum(row) > 1:
                continue
            else:
                # print("Yes")
                for j in range(len(mat)):
                    col_sum += mat[j][i]
                if col_sum == len(mat):
                    return i
        return -1
                
    
    # def celebrity(self, mat):
    #     stack = list(range(0,len(mat)))
    #     # print(stack)
    #     while stack:
    #         if len(stack) <= 1:
    #             break
    #         person1 = stack.pop()
    #         person2 = stack.pop()
    #         if mat[person1][person2] == 1:
    #             if mat[person2][person1] == 0:
    #                 stack.append(person2)
    #         else:
    #             if mat[person2][person1] == 1:
    #                 stack.append(person1)
    #     # print(stack)
    #     if len(stack) == 0:
    #         return -1
    #     if sum(mat[stack[-1]]) == 1:
    #         col_sum = 0
    #         for j in range(len(mat)):
    #                 col_sum += mat[j][stack[-1]]
    #         if col_sum == len(mat):
    #             return stack[-1]
    #     return -1        
