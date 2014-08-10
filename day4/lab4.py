def GCD(num1, num2):
  if num1 == num2:
    return num1
  nums = [num1, num2]
  greater = max(nums)
  smaller = min(nums)
  if (smaller == 0) or (greater % smaller == 0):
    return smaller
  remainder = greater % smaller
  remainder_list = [remainder]
  while remainder != 0:
  	num1 = smaller
  	num2 = remainder
  	remainder = num1 % num2
  	remainder_list.append(remainder) 
  	GCD(num1, num2)
  return remainder_list[len(remainder_list)-2]
      
print GCD(4, 2)
print GCD(1071, 462)
print GCD(1071, 1029)
print GCD(78696, 19332)

def prime(num):
  nums  = range(2,num+1)
  nums2 = nums[::2]
  nums3 = nums[1::3]
  nums5 = nums[3::5]
  nums7 = nums[5::7]
  nums11= nums[9::11]
  prime_list = list(set(nums)- set(nums2[1:]) - set(nums3[1:])
   - set(nums5[1:]) - set(nums7[1:]) - set(nums11[1:]))
  return prime_list
  
print prime(121)  

def hanoi(n, source, helper, target):
  if n>0:
    hanoi(n-1, source, target, helper)
    if source:
      target.append(source.pop())
    hanoi(n-1, helper, source, target)

source=[3,2,1]
helper=[]
target=[]
hanoi(len(source), source, helper, target)

print source, helper, target

  