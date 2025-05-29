def findLargestMinDistance(arr:list, m:int):
    def canwepaint(maxBoards,arr):
        no_of_boards_painted=arr[0]
        painters=1
        for boards in range(1,len(arr)):
            if(arr[boards]+no_of_boards_painted<=maxBoards):
                no_of_boards_painted+=arr[boards]
            else:
                no_of_boards_painted=arr[boards]
                painters+=1
        return painters
    Min=max(arr)
    Max=sum(arr)
    if(m>len(arr)):
        return -1
    low=max(arr)
    high=sum(arr)
    while(low<=high):
        max=(lowBoards+high)//2
        if(canwepaint(maxBoards,arr)<=m):
            high=maxBoards-1
    else:
            low=maxBoards+1
    return low