def next_permutation(nums):
    # Tìm vị trí lớn nhất trong dãy số mà số tại vị trí đó vẫn có thể tăng lên được
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1
    
    # Nếu không tìm thấy vị trí như vậy, dãy số đã là hoán vị lớn nhất
    if i == -1:
        nums.reverse()
        return nums
    
    # Tìm số lớn nhất ở phía bên phải của vị trí i
    j = len(nums) - 1
    while j >= 0 and nums[j] <= nums[i]:
        j -= 1
    
    # Hoán đổi số ở vị trí i và j
    nums[i], nums[j] = nums[j], nums[i]
    
    # Đảo ngược các số từ vị trí i+1 đến cuối để tạo ra hoán vị liền sau
    nums[i+1:] = nums[i+1:][::-1]
    
    return nums
# hoán vị liền sau: 
nums = [4,5,1,2,6,3]
print(next_permutation(nums))