def first_last6(nums):
    
    return nums[0]==6 or nums[-1]==6



print(first_last6([1, 2, 6]))



def same_first_last(nums):
  return len(nums)>=1 and nums[0]==nums[-1]
print(same_first_last([1, 2, 3]))



def make_pi():
  a=[3,1,4]
  return a
print(make_pi())


def common_end(a, b):
  return a[0]==b[-1] or a[-1]==b[-1]
print(common_end([1, 2, 3], [1, 3]))




def sum3(nums):
  return sum(nums)
print(sum3([1, 2, 3]))




def rotate_left3(nums):
    rotated = nums[1:] + nums[:1]
    return rotated



print(rotate_left3([1, 2, 3]) )




def reverse3(nums):
  return nums[::-1]
print(reverse3([1, 2, 3]))




def max_end3(nums):
  max_num=max(nums[0],nums[-1])
  nums[0]=max_num
  nums[1]=max_num
  nums[2]=max_num
  return nums
print(max_end3([1, 2, 3])) 



def middle_way(a, b):
  d=[a[1],b[1]]
  return d
print(middle_way([1, 2, 3], [4, 5, 6]))




def make_ends(nums):
  res=[nums[0],nums[-1]]
  return res
print(make_ends([1, 2, 3]) )



def has23(nums):
   return nums[0] == 2 or nums[1] == 2 or nums[0] == 3 or nums[1] == 3

print(has23([2, 5]))


