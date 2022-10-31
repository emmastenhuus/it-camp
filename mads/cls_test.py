
class Tst:
    def __init__(self, x) -> None:
        self.x = x

    @classmethod
    def i(cls, z):
        Tst.y = z

    def __str__(self) -> str:
        return str(self.x) + " / " + str(Tst.y)

    def __repr__(self) -> str:
        return str()

t1 = Tst(11)
t2 = Tst(13)
t1.i(8)

print(t1)
print(t2)

t2.i(3)

print(t1)
print(t2)

