S = raw_input()
vowels = 'AEIOU'
kevin_score = 0
stu_score = 0
for i in range(len(S)):
    if S[i] in vowels:
        kevin_score += (len(S)-i)
    else:
        stu_score += (len(S)-i)

if kevin_score > stu_score:
    print "Kevin", kevin_score
elif kevin_score < stu_score:
    print "Stuart", stu_score
else:
    print "Draw"
