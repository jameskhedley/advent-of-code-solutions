x = 'x'
y = 'y'

a_cost = 3
b_cost = 1

def read_data(fn):
    machines = []
    h0 = open(fn)
    for raw in h0.readlines():
        line = raw.strip()
        if line.startswith('Button A: '):
            machine = {'button_a': {}, 'button_b': {}, 'prize': {}}
            buttons = line.split('Button A: ')[1].split(',')
            machine['button_a'][x] = int(buttons[0].strip('X'))
            machine['button_a'][y] = int(buttons[1].strip().strip('Y'))
        elif line.startswith('Button B: '):
            buttons = line.split('Button B: ')[1].split(',')
            machine['button_b'][x] = int(buttons[0].strip('X'))
            machine['button_b'][y] = int(buttons[1].strip().strip('Y'))
        elif line.startswith('Prize: X'):
            prizes = line.split('Prize: ')[1].split(',')
            machine['prize'][x] = int(prizes[0].strip('X='))
            machine['prize'][y] = int(prizes[1].strip().strip('Y='))
            machines.append(machine)
        else:
            pass
    return machines

machines = read_data('day13_ex.txt') # pt1 480 # pt2 
#machines = read_data('day13_ex2.txt') 
#machines = read_data('day13_data.txt') 

'''
button_a = {'x':94, 'y':34}
button_b = {'x':22, 'y':67}
prize = {'x':8400, 'y':5400}
'''

def calc(machines):
    total = 0
    for machine in machines:
        prize = machine['prize']
        button_a = machine['button_a']
        button_b = machine['button_b']
        presses_a = (prize[x]*button_b[y] - prize[y]*button_b['x']) / (button_a[x]*button_b[y] - button_a[y]*button_b[x])
        presses_b = (button_a[x]*prize[y] - button_a[y]*prize[x]) / (button_a[x]*button_b[y] - button_a[y]*button_b[x])
        print(presses_a)
        print(presses_b)
        if presses_a == int(presses_a) and presses_b == int(presses_b):
            total += (presses_a*a_cost)
            total += (presses_b*b_cost)

    return total

print('pt 1: %d' % calc(machines))
for machine in machines:
    machine['prize'][x] = machine['prize'][x] + 10000000000000
    machine['prize'][y] = machine['prize'][y] + 10000000000000
print('pt 2: %d' % calc(machines))
