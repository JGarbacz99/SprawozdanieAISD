def merge(l, m, r, A, B):
    i = k = l
    j = m

    while i < m and j <= r:
        if A[i] <= A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
        k += 1

    while i < m:
        B[k] = A[i]
        i += 1
        k += 1

    while j <= r:
        B[k] = A[j]
        j += 1
        k += 1


A = [1, 35, 42, 65, 68, 25, 55, 59, 70, 79]
B = [0] * len(A)

merge(0, 5, 9, A, B)

for b in B:
    print(b)

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


A = [1, 35, 42, 65, 68, 25, 55, 59, 70, 79]
sorted_A = merge_sort(A)
print(sorted_A)
