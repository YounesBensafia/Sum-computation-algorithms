import tracking_usage as tu
p = 100
def compute_sum(N):
    s = 0
    for i in range(1, N + 1):
        s += i
    return s

def compute_sum_recu(N):
    return sum(range(1, N + 1))

a = open("complexity.csv", "w")
a.write("VALUE, ITERATIVE, RECURSIVE\n")
for i in range(1, 5000):
    time = sum([tu.track_time(lambda: compute_sum(i)) for _ in range(p)]) / p
    time_recu = sum([tu.track_time(lambda: compute_sum_recu(i)) for _ in range(p)]) / p
    a.write(f"{i}, {time}, {time_recu}\n")
    