class Solution(object):
    def longestSpecialPath(self, edges, nums):
        """
        :type edges: List[List[int]]
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        graph = [[] for _ in range(n)]
        for edge in edges:
            a, b, length = edge
            graph[a].append((b, length))
            graph[b].append((a, length))

        prefixSum = []
        lastOccurrence = {nums[0]: [0]}
        answer = [0, 0]

        def dfs(prev, curr, depth, length, cutoff, duplicate):
            prefix = prefixSum[cutoff] if cutoff >= 0 else 0
            sum_ = prefixSum[-1] if prefixSum else 0
            current = [sum_ - prefix, depth - cutoff - 1]

            if current[0] > answer[0] or (current[0] == answer[0] and current[1] < answer[1]):
                answer[0] = current[0]
                answer[1] = current[1]

            for (next_, nextLength) in graph[curr]:
                if next_ == prev:
                    continue

                color = nums[next_]

                old_cutoff = cutoff
                old_duplicate = duplicate

                if color in lastOccurrence and lastOccurrence[color]:
                    last = lastOccurrence[color][-1]
                    if last > duplicate:
                        cutoff = duplicate
                        duplicate = last
                    elif last > cutoff:
                        cutoff = last

                prefixSum.append(length + nextLength)
                if color not in lastOccurrence:
                    lastOccurrence[color] = []
                lastOccurrence[color].append(depth)

                dfs(curr, next_, depth + 1, length + nextLength, cutoff, duplicate)

                prefixSum.pop()
                lastOccurrence[color].pop()

                cutoff = old_cutoff
                duplicate = old_duplicate

        dfs(-1, 0, 1, 0, -1, -1)

        return answer
