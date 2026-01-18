class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: intm'j'b
        :rtype: bool
        """
        graph = {}
        for a,b in edges:
            if a in graph:
                graph[a].append(b)
            else:
                graph[a] =[b]
            if b in graph:
                graph[b].append(a)
            else:
                graph[b] =[a]
        seen = set([source])
        dq= deque([source])
        while dq:
            cur = dq.popleft()
            if cur==destination: return True
            for nxt in graph[cur]:
                if nxt not in seen:
                    seen.add(nxt)
                    dq.append(nxt)
        return False

                
