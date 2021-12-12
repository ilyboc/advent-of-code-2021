inp = '''start-A
start-b
A-c
A-b
b-d
A-end
b-end'''
inp = list(map(lambda x: x.split('-'),list(inp.split("\n"))))
paths = []
small_caves = set()
for i in inp:
    if i[0].islower(): small_caves.add(i[0])
    if i[1].islower(): small_caves.add(i[1])
small_caves.remove('start')
small_caves.remove('end')
for s in small_caves:
    stack = [['start']]
    while len(stack) > 0:
        current = stack.pop()
        if current[-1] == 'end':
            paths.append(",".join(current))
        else:
            for i in inp:
                if i[0] == current[-1]:
                    if not i[1].islower() or \
                        (i[1] == s and current.count(s) == 1) or \
                        (i[1] not in current):
                        stack.append(current + [i[1]])
                if i[1] == current[-1]:
                    if not i[0].islower() or \
                        (i[0] == s and current.count(s) == 1) or \
                        (i[0] not in current):
                        stack.append(current + [i[0]])

print(len(set(paths)))
        
