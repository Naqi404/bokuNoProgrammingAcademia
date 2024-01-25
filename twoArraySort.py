def sorted(arr1, arr2):
    i = 0
    j = 0
    ans = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i+=1
        elif arr2[j] < arr1[i]:
            ans.append(arr2[j])
            j+=1
        else:
            ans.append(arr1[i])
            ans.append(arr2[j])
            i += 1
            j += 1
    
    while i < len(arr1):
        ans.append(arr1[i])
        i+=1
    
    while j < len(arr2):
        ans.append(arr2[j])
        j+=1
    
    print(ans)


sorted([1,5,6,8,65,76,123,124,453,653,2343],[2,3,7,9,12,122,323,434,543,653,2343])
