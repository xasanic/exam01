son = int(input("Ballni kiritng ; "))

if 90 <= son <= 100:
    print("A, Alo")
elif 80 <= son <= 89:
    print("B, Yaxshi") 
elif 70 <= son <= 79:
    print("c, Qoniqarli") 
elif 60 <= son <= 69:
    print("D, Qoniqarsiz") 
elif 0 <= son <= 59:
    print("F, Yomon")
else:
    print("Ball 0-100 oralig\'ida bo\'lishi kerak!")