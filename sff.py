top_male_names = []
male_name_counts = {}
for i in legislators:
    i[1] = name
    if i[3] is 'M':
        if i[7] > 1940:
            if name in male_name_counts:
                male_name_counts[name] += 1
            else:
                male_name_counts[name] = 1

highest_male_count = None
for i,n in male_name_counts.items():
    if highest_male_count is None or n > hold:
        highest_male_count = n
        
for x,r in male_name_counts.items():
    if r == highest_male_count:
        top_male_names.append(x)
        
print(legislators)


