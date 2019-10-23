import math

def atan2(y, x):
    phi = math.atan2(y, x)
    if phi < 0: phi += 2 * math.pi
    return phi

class Skidpad:
    def __init__(self, R, a, b):
        self.R_ = R
        self.a_ = a
        self.b_ = b

        self.s_00_ = 0

        # Skidpad entry
        self.s_01_ = self.s_00_ + a

        # Two clockwise rotations
        self.s_02_ = self.s_01_ + math.pi * R
        self.s_03_ = self.s_02_ + math.pi * R
        self.s_04_ = self.s_03_ + math.pi * R
        self.s_05_ = self.s_04_ + math.pi * R

        # Two counterclockwise rotations
        self.s_06_ = self.s_05_ + math.pi * R
        self.s_07_ = self.s_06_ + math.pi * R
        self.s_08_ = self.s_07_ + math.pi * R
        self.s_09_ = self.s_08_ + math.pi * R

        # Skidpad exit
        self.s_10_ = self.s_09_ + b

    def x(self, s):
        if s < self.s_01_: return 0

        if s < self.s_05_:
            delta_s = s - self.s_01_
            return self.R_ * (1 - math.cos(delta_s / self.R_))

        if s < self.s_09_:
            delta_s = s - self.s_05_
            return self.R_ * (math.cos(delta_s / self.R_) - 1)

        return 0

    def y(self, s):

        if s < self.s_00_: return -self.a_
        if s < self.s_01_: return s - self.a_

        if s < self.s_09_:
            delta_s = s - self.s_01_
            return self.R_ * math.sin(delta_s / self.R_)

        if s < self.s_10_: return s - self.s_09_

        return self.b_

    def find_s(self, prev_s, x, y):
        if prev_s < self.s_01_:
            s = self.a_ + y

        elif prev_s < self.s_02_:
            s = self.s_01_ + atan2(+y, self.R_ - x) * self.R_
        elif prev_s < self.s_03_:
            s = self.s_02_ + atan2(-y, x - self.R_) * self.R_
        elif prev_s < self.s_04_:
            s = self.s_03_ + atan2(+y, self.R_ - x) * self.R_
        elif prev_s < self.s_05_:
            s = self.s_04_ + atan2(-y, x - self.R_) * self.R_

        elif prev_s < self.s_06_:
            s = self.s_05_ + atan2(+y, self.R_ + x) * self.R_
        elif prev_s < self.s_07_:
            s = self.s_06_ + atan2(-y, -x - self.R_) * self.R_
        elif prev_s < self.s_08_:
            s = self.s_07_ + atan2(+y, self.R_ + x) * self.R_
        elif prev_s < self.s_09_:
            s = self.s_08_ + atan2(-y, -x - self.R_) * self.R_

        else: return self.s_09_ + y

        if s - prev_s < 1e-9:
            return s
        else:
            return self.find_s(s, x, y)

    def find_d(self, s, x, y):
        if s < self.s_01_:
            return y

        elif s < self.s_05_:
            dx = x - self.R_
            dy = y

            r = math.sqrt(dx**2 + dy**2)

            return r - self.R_

        elif s < self.s_09_:
            dx = x + self.R_
            dy = y

            r = math.sqrt(dx**2 + dy**2)

            return self.R_ - r 

        else: return y
