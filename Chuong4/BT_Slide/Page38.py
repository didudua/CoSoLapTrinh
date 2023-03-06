def spam(divideby):
    try:
        result = 42 / divideby  # Chạy code
    except:
        # nếu code lỗi chạy dòng này
        print("Sorry ! You are dividing by zero ")
    else:
        # nếu code không lỗi chạy dòng này
        print("Yeah ! Your answer is :", result)


print(spam(1))
print(spam(0))
