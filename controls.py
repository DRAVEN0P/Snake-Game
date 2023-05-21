
def collision(obj,target):
    if int(obj.distance(target)) < 15:
        return True

def wall(obj):
    if obj.xcor()>=290 or obj.ycor()>=290 or obj.xcor()<=-290 or obj.ycor()<=-290:
        return True