def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #nums = []
        #targe = 0
        index1 = 0
        index2 = 0
        print("target is", target)

        stop = False
        for x in range(len(nums)):
            index1 = x
            print(x)
            for y in range(x+1, len(nums)):
                if nums[x] + nums[y] == target:
                    print("x and y are", nums[x], nums[y])
                    print(y)
                    index2 = y
                    stop = True
                    break
            if stop:
                break
        ret = [index1,index2]
        return ret  

nums = [2,7,11,15]
target = 9 

solution = twoSum(nums, target)

print(solution)