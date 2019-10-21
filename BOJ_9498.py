score = int(input())

score_dict = {6 : 'D', 7 : 'C', 8 : 'B', 9 : 'A', 10 : 'A'}

score = score // 10

if score in score_dict:
    print(score_dict[score])
else:
    print('F')