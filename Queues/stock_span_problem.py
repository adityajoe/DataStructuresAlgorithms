# The stock span problem is a financial problem where we have a series of daily price quotes for a stock and we need to calculate the span of stock price for all days.
# You are given an array arr[] representing daily stock prices, the stock span for the i-th day is the number of consecutive days up to day i (including day i itself) 
# for which the price of the stock is less than or equal to the price on day i. Return the span of stock prices for each day in the given sequence.


class Solution:
    def calculateSpan(self, arr):
        # code here
        span = [1]
        stack = [arr[0]]
        for i in range(1, len(arr)):
            # print(stack)
            # print(span)
            if arr[i] < stack[-1]:
                stack.append(arr[i])
                span.append(1)
            else:
                curr_span = 1
                index = i-1
                while len(stack) > 0 and arr[i] >= stack[-1]:
                    curr_span += span[index]
                    index -= span[index]
                    stack.pop()
                stack.append(arr[i])
                span.append(curr_span)
        return span
                    
                    
        
        
        
