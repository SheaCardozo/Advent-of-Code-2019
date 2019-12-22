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

ans = 0

for root in roots:
    ans = ans + root.count_orbits(1)

print(ans)
