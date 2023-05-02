def calculate_score(dice):
    # initialize counts for each die value (1-6)
    counts = [0, 0, 0, 0, 0, 0]
    # count the number of occurrences of each die value
    for d in dice:
        counts[d-1] += 1
    score = 0
    # check for triplets
    for i in range(6):
        if counts[i] >= 3:
            if i == 0:
                score += 1000
            else:
                score += (i+1) * 100
            counts[i] -= 3
    # add points for remaining 1s and 5s
    score += counts[0] * 100
    score += counts[4] * 50
    
    return calculate_score

dice = [1, 1, 2, 2, 3]
score = calculate_score(dice)
print(score)