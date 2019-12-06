with open('Q6.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.split()


class Orbit:

    def __init__(self, tag, root):
        self.tag = tag
        self.root = root
        self.orbiters = []

    def add_orbit(self, child):
        if self.tag == child.root:
            self.orbiters.append(child)
            return True
        else:
            for i in self.orbiters:
                if i.add_orbit(child):
                    return True

        return False

    def count_orbits(self, p):
        ans = 0
        for i in self.orbiters:
            ans = ans + i.count_orbits(p + 1) + p
        return ans

    def path_len(self, dest):
        if dest == self.tag:
            return 0
        else:
            for i in self.orbiters:
                p = i.path_len(dest)
                if p is not None:
                    return p + 1
        return None

    def short_path(self, src, dest):
        ans = 0
        for i in self.orbiters:
            s = i.path_len(src)
            d = i.path_len(dest)
            if s is not None and d is not None:
                return i.short_path(src, dest)
            else:
                ans = ans + (s if s is not None else 0) + (d if d is not None else 0)

        return ans


roots = []

for i in prompt:
    r, c = i.split(')')
    child = None
    for root in roots:
        if c == root.tag:
            roots.remove(root)
            root.root = r
            child = root
            break

    if child is None:
        child = Orbit(c, r)

    pres = False
    for root in roots:
        pres = pres or root.add_orbit(child)

    if not pres:
        root = Orbit(r, None)
        root.add_orbit(child)
        roots.append(root)

root = roots[0]

print(root.short_path('SAN', 'YOU'))
