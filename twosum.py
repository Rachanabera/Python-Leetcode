nums = list(map(int,input("Enter the Numbers: ").split()))
target = int(input("Enter target variable : "))

def twosum(nums,target):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]

result = twosum(nums,target)
print(f"Indices:{result}")