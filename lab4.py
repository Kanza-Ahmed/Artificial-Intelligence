#stack implementation
stack = []
# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
print('Initial stack')
print(stack)
# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
print('\nStack after elements are popped:')
print(stack)

#Queue implementation
queue = []
queue.append('a')
queue.append('b')
queue.append('c')
print("Initial queue")
print(queue)
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print("\nQueue after removing elements")
print(queue)

#binary search
#iterative method
def find(start, end, val, list):
    while start <= end:
        mid = (start + end) // 2
        if val == list[mid]:
            return mid
        elif val > list[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

list = [1, 2, 3, 4, 5, 6, 7, 8]
start = 0
end = len(list) - 1
val = int(input("Enter value to find: "))
index = find(start, end, val, list)

if index != -1:
    print(f"Value found at Index: {index}")
else:
    print("Value not found in the list.")

#recursive method
""" def find(start, end, val, list):
    if start > end:
        return -1
    mid = (start + end) // 2
    if val == list[mid]:
        return mid
    elif val > list[mid]:
        return find(mid + 1, end, val, list)
    else:
        return find(start, mid - 1, val, list)

list = [1, 2, 3, 4, 5, 6, 7, 8]
start = 0
end = len(list) - 1
val = int(input("Enter value to find: "))
index = find(start, end, val, list)

if index != -1:
    print(f"Value found at Index: {index}")
else:
    print("Value not found in the list.") """