class Integral:
    def __init__(self, e, set):
        self.e = e
        self.set = set
        self.length=self.set[1]-self.set[0]
        self.Low=0
        self.Upp=1
    def f(self, x):            # method, function εντός κλάσης
        return x**2        
    def play(self):
        n=1
        while self.Upp - self.Low>self.e:
            self.Low=0
            self.Upp=0
            n += 1
            self.step=(self.length)/n
            for i in range(n):
                t0= self.step*i
                t1= self.step*(i+1)
                self.Low+= self.step * self.f(t0)
                self.Upp+= self.step * self.f(t1)
        return [self.Upp, self.Low, n]