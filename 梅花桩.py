'''
华为2021年9月8日笔试题：梅花桩

题目描述

有一个 M*N 的梅花桩阵，每个桩都有允许跳跃的最大步数，用户从0,0的位置开始跳跃，允许向右和向下两个方向跳跃，求最少要跳跃多少次能到达M-1，N-1的位置。无法到达目的地时返回-1。
M<=100，N<=100，每个桩上允许跳跃的最大步数均为小于10的正整数，0表示不允许跳跃到该位置
输入描述
1、第1行为M和N，用"，"号隔开; 
2、第2行为M*N的梅花桩(格式参考样例)，数组位置为允许跳跃的最大步数，0表示该位置为空不能跳跃到该位置。

Input：
3,3
3 2 2 0 1 0 1 1 1

Output：
2
'''


from queue import Queue
class Solution:
    # 梅花桩:判断是否能到右下角点,深度优先搜索
    def dfs01(self,row,column,m,n):
        # 超出边界就返回
        if row>=m-1 or column >= n-1:
            if row == m-1 and column == n-1:
                # 到达右下角的点，返回
                return True
            elif row > m-1 or column > n-1:
                # 其他情况超出边界
                return False
        # print('now in row:{0},col:{1}'.format(row,column))
        # for i in {go_right,go_down}:
        for i in [0,1]:
            for step in range(1,steps[row*n+column]+1):
                # print('go:{1},step:{0}'.format(step,i))
                if i==0:#表示向右走
                    column = column+step
                    # print('coming to row:{0},col:{1}'.format(row,column))
                    if self.dfs01(row,column,m,n):
                        # 如果找到一条通往右下角点的路径，直接一次性返回，不用再回溯至上一个状态
                        return True
                    column = column-step
                    # print('leaving to row:{0},col:{1}'.format(row,column))
                elif i==1:#表示向下走
                    row = row+step
                    # print('coming to row:{0},col:{1}'.format(row,column))
                    if self.dfs01(row,column,m,n):
                        # 如果找到一条通往右下角点的路径，直接一次性返回，不用再回溯至上一个状态
                        return True
                    row = row-step
                    # print('leaving to row:{0},col:{1}'.format(row,column))
        return False
        
        
        
        
    # 梅花桩:判断是否能到达右下角点,以及返回最小跳跃次数,深度优先搜索
    def dfs02(self,row,column,m,n,count):
        global res
        # 超出边界就返回
        if row>=m-1 or column >= n-1:
            if row == m-1 and column == n-1:
                # 到达右下角的点，先返回,记录此时的路程长度
                res = min(res,count)
            elif row > m-1 or column > n-1:
                # 其他情况超出边界
                return
        # print('now in row:{0},col:{1}'.format(row,column))
        # for i in {go_right,go_down}:
        for i in [0,1]:
            for step in range(1,steps[row*n+column]+1):
                # print('go:{1},step:{0}'.format(step,i))
                if i==0:#表示向右走
                    column = column+step
                    count+=1
                    # print('coming to row:{0},col:{1}'.format(row,column))
                    self.dfs02(row,column,m,n,count)
                    # 现在如果找到一条通往右下角点的路径，不一次性返回，而是回溯至上一个状态
                    column = column-step
                    count-=1
                    # print('leaving to row:{0},col:{1}'.format(row,column))
                elif i==1:#表示向下走
                    row = row+step
                    count+=1
                    # print('coming to row:{0},col:{1}'.format(row,column))
                    self.dfs02(row,column,m,n,count)
                    # 现在如果找到一条通往右下角点的路径，不一次性返回，而是回溯至上一个状态
                    row = row-step
                    count-=1
                    # print('leaving to row:{0},col:{1}'.format(row,column))
        return
        
        
        
        
        
        
    # 梅花桩:用广度优先搜索方法判断是否能到右下角点
    def bfs01(self,steps,m,n):
        que = Queue()
        visted = [0]*(m*n+10)
        # 放入第一个点
        que.put((0,0))
        visted[0] = 1
        while que:
            # 取出队列中的第一个点,并将其周围相邻的点放入队列中
            # 注意,这里相邻的点就是它所能跳跃到的所有点
            row,column = que.get()
            for step in range(1,steps[row*n+column]+1):
                # # 右边相邻点
                # if row <= m-1 and column +step <=n-1 and visted[row*n+column+step] == 0:
                #     if row==m-1 and column +step==n-1:
                #         return True
                #     print('add (row:{0},col:{1}'.format(row,column+step))
                #     que.put((row,column +step))
                #     visted[row*n+(column+step)] = 1
                # # 下边相邻点
                # if row +step <= m-1 and column <=n-1 and visted[(row+step)*n+column] == 0:
                #     if row+step==m-1 and column==n-1:
                #         return True
                #     print('add (row:{0},col:{1}'.format(row+step,column))
                #     que.put((row+step,column))
                #     visted[(row+step)*n+column] = 1
                # 右边相邻点
                for move in [[0,step],[step,0]]:
                    r1 = row + move[0]
                    c1 = column + move[1]
                    if r1 <= m-1 and c1 <=n-1 and visted[r1*n+c1] == 0:
                        if r1==m-1 and c1==n-1:
                            return True
                        # print('add (row:{0},col:{1}'.format(r1,c1))
                        que.put((r1,c1))
                        visted[r1*n+c1] = 1
        return False


    # 梅花桩:用广度优先搜索方法判断是否能到右下角点且最短路程为多少
    def bfs02(self,steps,m,n,count):
        # 特判
        if m==1 and n==1:
            return count
        que = Queue()
        visted = [0]*(m*n+10)
        # 放入第一个点
        que.put((0,0))
        visted[0] = 1
        while que:
            # 取出队列中的第一层的点,并将其周围相邻的点放入队列中
            # 注意,这里相邻的点就是它所能跳跃到的所有点
            temp = que.qsize()
            for _ in range(temp):
            #在每一层遍历开始前，先记录队列中的结点数量temp（也就是这一层的结点数量），然后一口气将这一层结点全部扩散
                row,column = que.get()
                for step in range(1,steps[row*n+column]+1):
                    for move in [[0,step],[step,0]]:
                        r1 = row + move[0]
                        c1 = column + move[1]
                        if r1 <= m-1 and c1 <=n-1 and visted[r1*n+c1] == 0:
                            if r1==m-1 and c1==n-1:
                                return count
                            # print('add (row:{0},col:{1}'.format(r1,c1))
                            que.put((r1,c1))
                            visted[r1*n+c1] = 1
            count+=1
        return count


if __name__ == '__main__':
    #test
    m,n = 3,3 
    steps = [3,2,2,0,1,0,1,1,1]
    solution = Solution()
    print(solution.dfs01(0,0,m,n))
    res = float('inf')
    solution.dfs02(0,0,m,n,0)
    if res != float('inf'):
        print(res)  
    print(solution.bfs01(steps,3,3))
    print(solution.bfs02(steps,m,n,1))
