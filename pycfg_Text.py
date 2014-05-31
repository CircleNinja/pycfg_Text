import pycfg_HL2 as HL2

class Letter:
    def __init__(self, cfg, name=None, size=10):
        self.cfg = cfg
        self.size = size
        self.letterNO = 0

        if(name != None):
            self.name = name
        else:
            self.name = cfg.name
        return

    def A(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y, pos.z, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size / 2, pos.z + self.size, 1, target)
        self.makePoint(pos.x, pos.y + self.size, pos.z, 2, target)

        target = self.makePoint(pos.x, pos.y + self.size / 4, pos.z + self.size / 2, 3, None)
        self.makePoint(pos.x, pos.y + (self.size - self.size / 4), pos.z + self.size / 2, 4, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def B(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size, 1, target)
        target = self.makePoint(pos.x, pos.y + (self.size / 2), pos.z + self.size, 2, target)
        target = self.makePoint(pos.x, pos.y + self.size / 2 + self.size/4, pos.z + (self.size - (self.size / 5)), 3, target)
        target = self.makePoint(pos.x, pos.y + self.size / 2 + self.size/4, pos.z + (self.size - (self.size / 3)), 4, target)

        target = self.makePoint(pos.x, pos.y + (self.size / 2), pos.z + self.size / 2, 5, target)
        self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size / 2, 6, target)

        target = self.makePoint(pos.x, pos.y + self.size / 2 + self.size/4, pos.z + self.size / 3, 7, target)
        target = self.makePoint(pos.x, pos.y + self.size / 2 + self.size/4, pos.z + self.size / 5, 8, target)
        target = self.makePoint(pos.x, pos.y + (self.size / 2), pos.z, 9, target)
        self.makePoint(pos.x, pos.y + self.size/4, pos.z, 10, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def C(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size / 2 + self.size/4, pos.z, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z, 1, target)
        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size, 2, target)
        self.makePoint(pos.x, pos.y + self.size / 2 + self.size/4, pos.z + self.size, 3, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def D(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size, 1, target)
        target = self.makePoint(pos.x, pos.y + (self.size / 2), pos.z + self.size, 2, target)
        target = self.makePoint(pos.x, pos.y + self.size / 2 + self.size/4, pos.z + (self.size - (self.size / 5)), 3, target)
        target = self.makePoint(pos.x, pos.y + self.size / 2 + self.size/4, pos.z + self.size / 5, 4, target)
        target = self.makePoint(pos.x, pos.y + (self.size / 2), pos.z, 5, target)
        self.makePoint(pos.x, pos.y + self.size/4, pos.z, 6, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def E(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size / 2 + self.size/4, pos.z, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z, 1, target)
        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size, 2, target)
        self.makePoint(pos.x, pos.y + self.size / 2  + self.size/4, pos.z + self.size, 3, target)

        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size/2, 4, None)
        self.makePoint(pos.x, pos.y + self.size/2 + self.size/4, pos.z + self.size/2, 5, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def F(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size, 1, target)
        self.makePoint(pos.x, pos.y + self.size / 2  + self.size/4, pos.z + self.size, 2, target)

        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size/2, 3, None)
        self.makePoint(pos.x, pos.y + self.size/2 + self.size/4, pos.z + self.size/2, 4, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def G(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z + self.size, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size, 1, target)
        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z, 2, target)
        target = self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z, 3, target)
        self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z + self.size/2, 4, target)

        target = self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z + self.size/2, 5, None)
        target = self.makePoint(pos.x, pos.y + self.size/2, pos.z + self.size/2, 6, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def H(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z, 0, None)
        self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size, 1, target)

        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size/2, 3, None)
        self.makePoint(pos.x, pos.y + self.size/2 + self.size/4, pos.z + self.size/2, 4, target)

        target = self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z, 5, None)
        self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z + self.size, 6, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def I(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size, 0, None)
        self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z + self.size, 1, target)

        target = self.makePoint(pos.x, pos.y + self.size/2, pos.z + self.size, 3, None)
        self.makePoint(pos.x, pos.y + self.size/2, pos.z, 4, target)

        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z, 5, None)
        self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z, 6, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def J(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size, 0, None)
        self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z + self.size, 1, target)

        target = self.makePoint(pos.x, pos.y + self.size/2, pos.z + self.size, 3, None)
        self.makePoint(pos.x, pos.y + self.size/2, pos.z, 4, target)

        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z, 5, None)
        self.makePoint(pos.x, pos.y + self.size/2, pos.z, 6, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def K(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size, 0, None)
        self.makePoint(pos.x, pos.y + self.size/4, pos.z, 1, target)

        target = self.makePoint(pos.x, pos.y + self.size- self.size/4, pos.z + self.size, 2, None)
        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size/2, 3, target)
        self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z, 4, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def L(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z, 1, target)
        self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z, 2, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def M(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/8, pos.z, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size/8, pos.z + self.size, 1, target)
        target = self.makePoint(pos.x, pos.y + self.size/2, pos.z + self.size/2, 2, target)
        target = self.makePoint(pos.x, pos.y + self.size - self.size/8, pos.z + self.size, 3, target)
        self.makePoint(pos.x, pos.y + self.size - self.size/8, pos.z, 4, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def N(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size, 1, target)
        target = self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z, 2, target)
        self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z + self.size, 3, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def O(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/4 + self.size/12, pos.z, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size/12, pos.z + self.size/4, 1, target)
        target = self.makePoint(pos.x, pos.y + self.size/12, pos.z + self.size - (self.size/4 + self.size/12), 2, target)
        target = self.makePoint(pos.x, pos.y + self.size/4 + self.size/12, pos.z + self.size - self.size/12, 3, target)
        target = self.makePoint(pos.x, pos.y + self.size - (self.size/4 + self.size/12), pos.z + self.size - self.size/12, 4, target)
        target = self.makePoint(pos.x, pos.y + self.size - self.size/12, pos.z + self.size - (self.size/4 + self.size/12), 5, target)
        target = self.makePoint(pos.x, pos.y + self.size - self.size/12, pos.z + self.size/4, 6, target)
        target = self.makePoint(pos.x, pos.y + self.size - (self.size/4 + self.size/12), pos.z, 7, target)
        self.makePoint(pos.x, pos.y + self.size/4 + self.size/12, pos.z, 8, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def P(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size, 1, target)
        target = self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z + self.size, 2, target)
        target = self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z + self.size/2, 3, target)
        self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size/2, 4, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def Q(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/4 + self.size/12, pos.z, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size/12, pos.z + self.size/4, 1, target)
        target = self.makePoint(pos.x, pos.y + self.size/12, pos.z + self.size - (self.size/4 + self.size/12), 2, target)
        target = self.makePoint(pos.x, pos.y + self.size/4 + self.size/12, pos.z + self.size - self.size/12, 3, target)
        target = self.makePoint(pos.x, pos.y + self.size - (self.size/4 + self.size/12), pos.z + self.size - self.size/12, 4, target)
        target = self.makePoint(pos.x, pos.y + self.size - self.size/12, pos.z + self.size - (self.size/4 + self.size/12), 5, target)
        target = self.makePoint(pos.x, pos.y + self.size - self.size/12, pos.z + self.size/4, 6, target)
        target = self.makePoint(pos.x, pos.y + self.size - (self.size/4 + self.size/12), pos.z, 7, target)
        self.makePoint(pos.x, pos.y + self.size/4 + self.size/12, pos.z, 8, target)

        target = self.makePoint(pos.x, pos.y + self.size, pos.z, 9, None)
        target = self.makePoint(pos.x, pos.y + self.size - self.size/2, pos.z + self.size/3, 10, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def R(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size, 1, target)
        target = self.makePoint(pos.x, pos.y + self.size - self.size/3, pos.z + self.size, 2, target)
        target = self.makePoint(pos.x, pos.y + self.size - self.size/3, pos.z + self.size/2, 3, target)
        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size/2, 4, target)
        self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z, 5, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def S(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z + self.size, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size, 1, target)
        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size - self.size/3, 2, target)
        target = self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z + self.size/3, 3, target)
        target = self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z, 4, target)
        self.makePoint(pos.x, pos.y + self.size/4, pos.z, 5, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def T(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/2, pos.z + self.size, 0, None)
        self.makePoint(pos.x, pos.y + self.size/2, pos.z, 1, target)

        target = self.makePoint(pos.x, pos.y + self.size/8, pos.z + self.size, 2, None)
        self.makePoint(pos.x, pos.y + self.size - self.size/8, pos.z + self.size, 3, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def U(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z, 1, target)
        target = self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z, 2, target)
        self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z + self.size, 3, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def V(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size/2, pos.z, 1, target)
        self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z + self.size, 2, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def W(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/8, pos.z + self.size, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z, 1, target)
        target = self.makePoint(pos.x, pos.y + self.size/2, pos.z + self.size/2, 2, target)
        target = self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z, 3, target)
        self.makePoint(pos.x, pos.y + self.size - self.size/8, pos.z + self.size, 4, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def X(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size, 0, None)
        self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z, 1, target)

        target = self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z + self.size, 2, None)
        self.makePoint(pos.x, pos.y + self.size/4, pos.z, 3, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def Y(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/2, pos.z + self.size/2, 0, None)
        self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size, 1, target)
        self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z + self.size, 2, target)
        self.makePoint(pos.x, pos.y + self.size/4, pos.z, 3, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def Z(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/8, pos.z + self.size, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size - self.size/8, pos.z + self.size, 1, target)
        target = self.makePoint(pos.x, pos.y + self.size/8, pos.z, 2, target)
        self.makePoint(pos.x, pos.y + self.size - self.size/8, pos.z, 3, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def zero(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size, 1, target)
        target = self.makePoint(pos.x, pos.y + self.size / 2  + self.size/4, pos.z + self.size, 2, target)
        target = self.makePoint(pos.x, pos.y + self.size / 2 + self.size/4, pos.z, 3, target)
        self.makePoint(pos.x, pos.y +  self.size/4, pos.z, 4, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def one(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size - self.size/5, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size/2, pos.z + self.size, 1, target)
        self.makePoint(pos.x, pos.y + self.size/2, pos.z, 2, target)

        target = self.makePoint(pos.x, pos.y + self.size/8, pos.z, 3, None)
        self.makePoint(pos.x, pos.y + self.size - self.size/8, pos.z, 4, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def two(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z + self.size, 1, target)
        target = self.makePoint(pos.x, pos.y + self.size - self.size/8, pos.z + self.size - self.size/3, 2, target)
        target = self.makePoint(pos.x, pos.y + self.size/8, pos.z, 3, target)
        self.makePoint(pos.x, pos.y + self.size - self.size/8, pos.z, 4, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def three(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z + self.size, 1, target)
        target = self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z, 2, target)
        self.makePoint(pos.x, pos.y + self.size/4, pos.z, 3, target)

        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size/2, 4, None)
        self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z + self.size/2, 5, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def four(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size/2, 1, target)
        self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z + self.size/2, 2, target)

        target = self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z + self.size, 3, None)
        self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z, 4, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def five(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z + self.size, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size, 1, target)
        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size/2, 2, target)
        target = self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z + self.size/2, 3, target)
        target = self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z, 4, target)
        self.makePoint(pos.x, pos.y + self.size/8, pos.z, 5, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def six(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size, 1, target)
        target = self.makePoint(pos.x, pos.y + self.size / 2  + self.size/4, pos.z + self.size, 2, target)

        target = self.makePoint(pos.x, pos.y + self.size / 2 + self.size/4, pos.z + self.size / 2, 3, None)
        self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size / 2, 4, target)

        target = self.makePoint(pos.x, pos.y + self.size / 2 + self.size/4, pos.z, 5, target)
        self.makePoint(pos.x, pos.y + self.size/4, pos.z, 6, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def seven(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size / 2 + self.size/4, pos.z, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size / 2 + self.size/4, pos.z + self.size, 1, target)
        self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size, 2, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def eight(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size, 1, target)
        target = self.makePoint(pos.x, pos.y + self.size / 2  + self.size/4, pos.z + self.size, 2, target)

        target = self.makePoint(pos.x, pos.y + self.size / 2 + self.size/4, pos.z + self.size / 2, 3, target)
        self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size / 2, 4, target)

        target = self.makePoint(pos.x, pos.y + self.size / 2 + self.size/4, pos.z, 5, target)
        self.makePoint(pos.x, pos.y + self.size/4, pos.z, 6, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def nine(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size / 2 + self.size/4, pos.z, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size / 2 + self.size/4, pos.z + self.size, 1, target)
        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size, 2, target)

        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size / 2, 3, target)
        self.makePoint(pos.x, pos.y + self.size/2 + self.size/4, pos.z + self.size / 2, 4, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def dash(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/4, pos.z + self.size/2, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size - self.size/4, pos.z + self.size/2, 1, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def underline(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/8, pos.z, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size - self.size/8, pos.z, 1, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def arrowLeft(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size - self.size/5, pos.z + self.size, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size/5, pos.z + self.size/2, 1, target)
        self.makePoint(pos.x, pos.y + self.size - self.size/5, pos.z, 2, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def arrowRight(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/5, pos.z + self.size, 0, None)
        target = self.makePoint(pos.x, pos.y + self.size - self.size/5, pos.z + self.size/2, 1, target)
        self.makePoint(pos.x, pos.y + self.size/5, pos.z, 2, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def colon(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + (self.size/2 - self.size/6), pos.z + self.size - self.size/4, 0, None)
        target = self.makePoint(pos.x, pos.y + (self.size/2 - self.size/6), pos.z + self.size - (self.size/2 - self.size/6), 1, target)
        target = self.makePoint(pos.x, pos.y + self.size - (self.size/2 - self.size/6), pos.z + self.size - (self.size/2 - self.size/6), 2, target)
        target = self.makePoint(pos.x, pos.y + self.size - (self.size/2 - self.size/6), pos.z + self.size - self.size/4, 3, target)
        self.makePoint(pos.x, pos.y + (self.size/2 - self.size/6), pos.z + self.size - self.size/4, 4, target)

        target = self.makePoint(pos.x, pos.y + (self.size/2 - self.size/6), pos.z + self.size/4, 5, None)
        target = self.makePoint(pos.x, pos.y + (self.size/2 - self.size/6), pos.z + (self.size/2 - self.size/6), 6, target)
        target = self.makePoint(pos.x, pos.y + self.size - (self.size/2 - self.size/6), pos.z + (self.size/2 - self.size/6), 7, target)
        target = self.makePoint(pos.x, pos.y + self.size - (self.size/2 - self.size/6), pos.z + self.size/4, 8, target)
        self.makePoint(pos.x, pos.y + (self.size/2 - self.size/6), pos.z + self.size/4, 9, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def semiColon(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + (self.size/2 - self.size/6), pos.z + self.size, 0, None)
        target = self.makePoint(pos.x, pos.y + (self.size/2 - self.size/6), pos.z + self.size - self.size/4, 1, target)
        target = self.makePoint(pos.x, pos.y + self.size - (self.size/2 - self.size/6), pos.z + self.size - self.size/4, 2, target)
        target = self.makePoint(pos.x, pos.y + self.size - (self.size/2 - self.size/6), pos.z + self.size, 3, target)
        self.makePoint(pos.x, pos.y + (self.size/2 - self.size/6), pos.z  + self.size, 4, target)

        target = self.makePoint(pos.x, pos.y + self.size/2, pos.z + self.size/3, 5, None)
        self.makePoint(pos.x, pos.y + self.size/2 - self.size/8, pos.z, 6, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def fullStop(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + (self.size/2 - self.size/6), pos.z, 0, None)
        target = self.makePoint(pos.x, pos.y + (self.size/2 - self.size/6), pos.z + self.size/4, 1, target)
        target = self.makePoint(pos.x, pos.y + self.size - (self.size/2 - self.size/6), pos.z + self.size/4, 2, target)
        target = self.makePoint(pos.x, pos.y + self.size - (self.size/2 - self.size/6), pos.z, 3, target)
        self.makePoint(pos.x, pos.y + (self.size/2 - self.size/6), pos.z, 4, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def equals(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/5, pos.z + self.size, 0, None)
        self.makePoint(pos.x, pos.y + self.size - self.size/5, pos.z + self.size, 1, target)

        target = self.makePoint(pos.x, pos.y + self.size/5, pos.z, 2, None)
        self.makePoint(pos.x, pos.y + self.size - self.size/5, pos.z, 3, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def exclamation(self, pos, ang=HL2.Vec(0,0,0)):
        base = HL2.Entity(self.cfg, "info_target", "{0}{1}".format(self.name, self.letterNO))
        base.create()
        base.setKeyvalue("origin", pos.str())

        pos.y -= self.size / 2

        target = self.makePoint(pos.x, pos.y + self.size/2, pos.z + self.size, 0, None)
        self.makePoint(pos.x, pos.y + self.size/2, pos.z + self.size/4 + self.size/6, 1, target)

        target = self.makePoint(pos.x, pos.y + (self.size/2 - self.size/6), pos.z, 2, None)
        target = self.makePoint(pos.x, pos.y + (self.size/2 - self.size/6), pos.z + self.size/4, 3, target)
        target = self.makePoint(pos.x, pos.y + self.size - (self.size/2 - self.size/6), pos.z + self.size/4, 4, target)
        target = self.makePoint(pos.x, pos.y + self.size - (self.size/2 - self.size/6), pos.z, 5, target)
        self.makePoint(pos.x, pos.y + (self.size/2 - self.size/6), pos.z, 6, target)

        self.cfg.rawCmd("ent_fire {0}{1}_* setparent {0}{1}".format(self.name, self.letterNO))
        base.setKeyvalue("angles", ang.str())
        self.letterNO += 1
        return "{0}{1}".format(self.name, self.letterNO-1)

    def makePoint(self, x, y, z, letterSection, target):
        newPointTargetname = "{0}{1}_{2}".format(self.name, self.letterNO, letterSection)

        newPoint = HL2.Entity(self.cfg, "env_alyxemp", newPointTargetname)
        newPoint.create()
        if (target != None):
            newPoint.fireInput("settargetent", target)
        newPoint.setKeyvalue("origin", "{0} {1} {2}".format(x, y, z))

        return newPointTargetname

    def ShowBeam(self, color, letterNO=None):
        if(letterNO == None):
            beamTargetname = "{0}{1}beam".format(self.name, self.letterNO-1)
            lastChar = HL2.Entity(self.cfg, "env_alyxemp", "{0}{1}_*".format(self.name, self.letterNO-1))
        else:
            beamTargetname = "{0}{1}beam".format(self.name, letterNO)
            lastChar = HL2.Entity(self.cfg, "env_alyxemp", "{0}{1}_*".format(self.name, letterNO))
        
        lastChar.addOutput("onuser1","!self","startdischarge")
        lastChar.addOutput("onuser1","!self","startcharge","0","0.001")
        lastChar.addOutput("onuser1","beam","addoutput","targetname {0}".format(beamTargetname),"0.005")
        lastChar.addOutput("onuser1",beamTargetname,"addoutput","classname {0}".format(self.cfg.name),"0.01")
        lastChar.addOutput("onuser1",beamTargetname,"noise","0","0.01")
        lastChar.addOutput("onuser1",beamTargetname,"width","{0}".format(self.size / 10),"0.01")
        lastChar.addOutput("onuser1",beamTargetname,"addoutput","rendercolor {0} {1} {2}".format(color.x, color.y, color.z),"0.01")
        lastChar.addOutput("onuser2","!self","fireuser2","","1000")
        lastChar.addOutput("onuser2","!self","fireuser1")
        lastChar.fireInput("fireuser2");
    
    def Message(self, stringIn, pos=HL2.Vec(0), ang=HL2.Vec(0), rotateOrigin=None):
        addAng = 0
        if(rotateOrigin != None):
            addAng = 0#maths needed here
        
        for c in stringIn:
            if ((c == "A") or (c == "a")):
                self.A(pos, ang)
            elif ((c == "B") or (c == "b")):
                self.B(pos, ang)
            elif ((c == "C") or (c == "c")):
                self.C(pos, ang)
            elif ((c == "D") or (c == "d")):
                self.D(pos, ang)
            elif ((c == "E") or (c == "e")):
                self.E(pos, ang)
            elif ((c == "F") or (c == "f")):
                self.F(pos, ang)
            elif ((c == "G") or (c == "g")):
                self.G(pos, ang)
            elif ((c == "H") or (c == "h")):
                self.H(pos, ang)
            elif ((c == "I") or (c == "i")):
                self.I(pos, ang)
            elif ((c == "J") or (c == "j")):
                self.J(pos, ang)
            elif ((c == "K") or (c == "k")):
                self.K(pos, ang)
            elif ((c == "L") or (c == "l")):
                self.L(pos, ang)
            elif ((c == "M") or (c == "m")):
                self.M(pos, ang)
            elif ((c == "N") or (c == "n")):
                self.N(pos, ang)
            elif ((c == "O") or (c == "o")):
                self.O(pos, ang)
            elif ((c == "P") or (c == "p")):
                self.P(pos, ang)
            elif ((c == "Q") or (c == "q")):
                self.Q(pos, ang)
            elif ((c == "R") or (c == "r")):
                self.R(pos, ang)
            elif ((c == "S") or (c == "s")):
                self.S(pos, ang)
            elif ((c == "T") or (c == "t")):
                self.T(pos, ang)
            elif ((c == "U") or (c == "u")):
                self.U(pos, ang)
            elif ((c == "V") or (c == "v")):
                self.V(pos, ang)
            elif ((c == "W") or (c == "w")):
                self.W(pos, ang)
            elif ((c == "X") or (c == "x")):
                self.X(pos, ang)
            elif ((c == "Y") or (c == "y")):
                self.Y(pos, ang)
            elif ((c == "Z") or (c == "z")):
                self.Z(pos, ang)
            elif (c == "0"):
                self.zero(pos, ang)
            elif (c == "1"):
                self.one(pos, ang)
            elif (c == "2"):
                self.two(pos, ang)
            elif (c == "3"):
                self.three(pos, ang)
            elif (c == "4"):
                self.four(pos, ang)
            elif (c == "5"):
                self.five(pos, ang)
            elif (c == "6"):
                self.six(pos, ang)
            elif (c == "7"):
                self.seven(pos, ang)
            elif (c == "8"):
                self.eight(pos, ang)
            elif (c == "9"):
                self.nine(pos, ang)
            elif (c == "-"):
                self.dash(pos, ang)
            elif (c == "_"):
                self.underline(pos, ang)
            elif (c == "<"):
                self.arrowLeft(pos, ang)
            elif (c == ">"):
                self.arrowRight(pos, ang)
            elif (c == ":"):
                self.colon(pos, ang)
            elif (c == ";"):
                self.semiColon(pos, ang)
            elif (c == "."):
                self.fullStop(pos, ang)
            elif (c == "="):
                self.equals(pos, ang)
            elif (c == "!"):
                self.exclamation(pos, ang)
            
            newpos = HL2.Vec(0)
            newpos.add(pos)
            newpos.y += self.size
            newpos.rotate(pos, 'y', -ang.x)
            newpos.rotate(pos, 'z', -ang.y)
            newpos.rotate(pos, 'x', -ang.z)
            newpos.y += self.size/2 #?ez need to fix this.
            pos = newpos