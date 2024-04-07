def shortest_common_superstring(strings):
    # Find the maximum overlap between two strings
    def overlap(str1, str2, min_length=1):
        start = 0
        while True:
            start = str1.find(str2[:min_length], start)
            if start == -1:
                return 0
            if str2.startswith(str1[start:]):
                return len(str1) - start
            start += 1

    # Merge the two strings with maximum overlap
    def merge(str1, str2, overlap_len):
        return str1 + str2[overlap_len:]

    # Find the shortest common superstring
    n = len(strings)
    while n > 1:
        max_overlap = 0
        pair = (0, 1)
        i = 0
        while i < n:
            j = i + 1
            while j < n:
                olen = overlap(strings[i], strings[j])
                if olen > max_overlap:
                    max_overlap = olen
                    pair = (i, j)
                j += 1
            i += 1
        i, j = pair
        strings[i] = merge(strings[i], strings[j], max_overlap)
        strings.pop(j)
        n -= 1

    return strings[0]

# Take user input for the string set
num_strings = int(input("Enter the number of strings in the set: "))
strings = []
i = 0
while i < num_strings:
    string = input(f"Enter string {i+1}: ")
    strings.append(string)
    i += 1

# Find the shortest common superstring
shortest_superstring = shortest_common_superstring(strings)
print(f"The shortest common superstring is: {shortest_superstring}")
