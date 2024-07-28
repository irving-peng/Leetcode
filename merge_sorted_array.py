ratings = [1,3,2,2,1]
# 1 + 2 + 2  + 1 + 1


min_val = min(ratings)
min_index = ratings.index(min_val)
total_candy = 1

current_candy = 1
current_val = ratings[min_index]

for i in range(min_index- 1, -1, -1):
    print("cur candy: "+  str(current_candy) +  " total: " +  str(total_candy))

    
    if ratings[i] == current_val:
        # same
        total_candy += 1
        current_candy= 1
        print(ratings[j])
        a = ratings[i]
        print("cur candy: "+  str(current_candy) +  " total: " +   str(total_candy) + " cur_val : " + str(a))
        current_val = a
        continue

        
    if ratings[i] < current_val:
        # lower, give current -1
        total_candy += 1 
        current_candy =1
        print(ratings[j])
        a = ratings[i]
        print("cur candy: "+  str(current_candy) +  " total: " +  str(total_candy) + " cur_val : " + str(a))
        current_val = a
        continue

    if ratings[i] > current_val:
        # larger, give +1
        total_candy += current_candy + 1
        current_candy += 1
        print(ratings[j])
        a = ratings[i]
        print("cur candy: "+  str(current_candy) +  " total: " + str(total_candy) + " cur_val : " + str(a))
        current_val = a
        continue
    
    
    
current_candy = 1
current_val = ratings[min_index]
for j in range(min_index + 1, len(ratings)):
    
    
    if ratings[j] == current_val:
        # same
        total_candy += 1
        current_candy= 1
        print(ratings[j])
        a = ratings[j]
        print("cur candy: "+  str(current_candy) +  " total: " +   str(total_candy) + " cur_val : " + str(a))
        current_val = a
        continue
    if ratings[j] < current_val:
        # lower, give current -1
        total_candy += 1 
        current_candy =1
        print(ratings[j])
        a = ratings[j]
        print("cur candy: "+  str(current_candy) +  " total: " +  str(total_candy) + " cur_val : " + str(a))
        current_val = a
        continue
    if ratings[j] > current_val:
        # larger, give +1
        total_candy += current_candy + 1
        current_candy += 1
        print(ratings[j])
        a = ratings[j]
        print("cur candy: "+  str(current_candy) +  " total: " + str(total_candy) + " cur_val : " + str(a))
        current_val = a
        continue
    

print(total_candy)   