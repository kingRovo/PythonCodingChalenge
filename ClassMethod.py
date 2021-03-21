class Mob:
    fp ='priti'
    def __init__(self,mobile,camara):
        self.mob = mobile
        self.cam = camara
    def isFP(self):
        print(self.fp)
    def show(self):
        print('Mobile is : ',self.mob)
        print('Camara is : ',self.cam)
ob =Mob('OnePlus','Sony')
ob.show()
print(Mob.isFP())
print(Mob.fp)
Mob.fp = 'no'
print(Mob.fp)
