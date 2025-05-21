while True:


    shown_hit_rate = int(input("what is the shown hit rate %?"))
    count = 0

    for a in range(100):
        for b in range(100):
            if shown_hit_rate > (a + b) / 2:
                count+=1
            
    true_hit = count / 100
    print(true_hit)

'''
For reference:
https://serenesforest.net/general/true-hit/

'''