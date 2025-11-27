class Solution:
    def containVirus(self, isInfected):
        m, n = len(isInfected), len(isInfected[0])
        
        def neighbors(r, c):
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n:
                    yield nr, nc
        
        total_walls = 0
        
        while True:
            visited = [[False]*n for _ in range(m)]
            regions = []            
            frontiers = []          
            walls_needed = []       
            
            
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and not visited[i][j]:
                        stack = [(i, j)]
                        visited[i][j] = True
                        
                        region = []
                        frontier = set()
                        walls = 0
                        
                        while stack:
                            r, c = stack.pop()
                            region.append((r,c))
                            
                            for nr, nc in neighbors(r, c):
                                if isInfected[nr][nc] == 0:
                                    frontier.add((nr,nc))
                                    walls += 1
                                elif isInfected[nr][nc] == 1 and not visited[nr][nc]:
                                    visited[nr][nc] = True
                                    stack.append((nr,nc))
                        
                        regions.append(region)
                        frontiers.append(frontier)
                        walls_needed.append(walls)
            
            if not regions:
                break
            
            idx = max(range(len(frontiers)), key=lambda i: len(frontiers[i]))
            
            total_walls += walls_needed[idx]
            
            for r, c in regions[idx]:
                isInfected[r][c] = 2
            
            for i, region in enumerate(regions):
                if i == idx:
                    continue
                for r, c in frontiers[i]:
                    isInfected[r][c] = 1
            
            can_spread = False
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1:
                        can_spread = True
                        break
                if can_spread:
                    break
            
            if not can_spread:
                break
        
        return total_walls
