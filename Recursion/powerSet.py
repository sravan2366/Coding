def fun(array, prefix=""):
    if len(array) == 0:
        return
    for i in range(0, len(array)):
        prefix += array[i]
        print(prefix, end=" ")
        fun(array[i+1:], prefix)
        # Backtracking
        prefix = prefix[:len(prefix)-1]

fun('abc')