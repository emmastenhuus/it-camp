
class Tst:
    y = 0

    def __init__(self, x) -> None:
        self.x = x

    @classmethod
    def i(cls, z):
        cls.y = z

    def __str__(self) -> str:
        return str(self.x) + " / " + str(Tst.y)

t1 = Tst(11)
t2 = Tst(13)
Tst.i(8)

print(t1)
print(t2)

Tst.i(3)

print(t1)
print(t2)

