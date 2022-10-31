class Const:
    def __init__(self, c) -> None:
        self.c = c
    def __str__(self) -> str:
        return str(self.c)
    def eval(self, env):
        return self.c

class Var:
    def __init__(self, v) -> None:
        self.v = v
    def __str__(self) -> str:
        return self.v
    def eval(self, env):
        return env[self.v]

class Multi:
    def __init__(self, l, r) -> None:
        self.l = l
        self.r = r
    def __str__(self) -> str:
        return str(self.l) + "*" + str(self.r)
    def eval(self, env):
        return self.l.eval(env) * self.r.eval(env)

class Add:
    def __init__(self, l, r) -> None:
        self.l = l
        self.r = r
    def __str__(self) -> str:
        return "(" + str(self.l) + "+" + str(self.r) + ")"
    def eval(self, env):
        return self.l.eval(env) + self.r.eval(env)

expr = Add(Multi(Const(7), Var("x")), Multi(Add(Var("y"), Const(4)), Var("x")))
print(expr)
print(expr.eval({"x":-2, "y":17}))
