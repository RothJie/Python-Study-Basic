from typing import Union

class ShowPoint:
    def __init__(self, x:Union[int,float,str], y:Union[int,float,str]):
        self.x = round(float(x),2)
        self.y = round(float(y),2)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def get_print_point(self):
        print("Point({},{})".format(self.getX(), self.getY()))


def input_pos():
    pos_li = []
    i = 1
    while i <= 3:
        pos = input("请输入坐标，用‘,'隔开即可:").split(',')
        pos_li.append(ShowPoint(pos[0], pos[1]))
        i += 1
    else:
        return pos_li


def get_zhong_xin(p1:ShowPoint,p2:ShowPoint,p3:ShowPoint):
    x_ = (p1.getX() + p2.getX() + p3.getX())/3
    y_ = (p1.getY() + p2.getY() + p3.getY())/3
    return ShowPoint(x_,y_)

if __name__ == '__main__':
    position_li = input_pos()
    zhong_xin = get_zhong_xin(position_li[0],position_li[1],position_li[2])
    zhong_xin.get_print_point()
