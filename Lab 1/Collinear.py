#fall on one straight line
def pt(x1,y1,x2,y2,x3,y3):
    if x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)==0:
        print("The points are collinear")
    else:
        print("The points are not collinear")
