while True:
    shown_hit_rate = int(input("what is the shown hit rate %?"))
    
    # Instead of nested loops, calculate directly
    # For each value of a (0-99), count how many values of b satisfy shown_hit_rate > (a + b) / 2
    count = 0
    for a in range(100):
        # shown_hit_rate > (a + b) / 2
        # 2*shown_hit_rate > a + b
        # b < 2*shown_hit_rate - a
        valid_b_count = min(100, max(0, int(2 * shown_hit_rate - a)))
        count += valid_b_count
    
    true_hit = count / 100  # Divide by 100 for the percentage
    print(true_hit)

'''
For reference:
https://serenesforest.net/general/true-hit/
'''