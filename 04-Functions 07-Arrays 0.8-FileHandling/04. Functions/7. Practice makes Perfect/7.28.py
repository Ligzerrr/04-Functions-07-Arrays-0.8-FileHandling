###
# Program that returns the most rolled number

def f(dice):
    max_streak = 1
    current_streak = 1
    most_rolled = dice[0]
    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:
            current_streak += 1
        else:
            if current_streak > max_streak:
                max_streak = current_streak
                most_rolled = dice[i - 1]
            current_streak = 1
    
    if current_streak > max_streak:
        most_rolled = dice[-1]
        max_streak = current_streak 
    return int(most_rolled)

dice_rolls = input('Enter dice rolls: ')
print(f'{f(dice_rolls)}')