N = int(input("Enter a number: "))
sum_odd = 0
sum_even = 0
average_even = 0
for i in range(1, N+1):
    if i % 2 == 0:
        total_even = N//2
        sum_even += i
        average_even = sum_even/total_even
    else:
        sum_odd += i
print("Sum of odd numbers 1 to ", N, " is ", sum_odd)
print("Average of even numbers is", average_even)