class Solution:
   def largestRectangleArea(self, heights: List[int]) -> int:
      n = len(heights)
      st = []
      leftsmall = [0] * n
      rightsmall = [0] * n

      for i in range(n):
         while st and heights[st[-1]] >= heights[i]:
            st.pop()
         leftsmall[i] = 0 if not st else st[-1] + 1
         st.append(i)

      st.clear()
      for i in range(n - 1, -1, -1):
         while st and heights[st[-1]] >= heights[i]:
            st.pop()
         rightsmall[i] = n - 1 if not st else st[-1] - 1
         st.append(i)

      maxA = 0
      for i in range(n):
         maxA = max(maxA, heights[i] * (rightsmall[i] - leftsmall[i] + 1))
      return maxA
