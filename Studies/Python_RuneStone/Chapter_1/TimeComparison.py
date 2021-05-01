import time

d = {'john': 1, 'tim': 2}

start_time = time.time()
d['john']
end_time = time.time()

print("Time to access dict[0]:", end_time-start_time)

c = ['john', 'tim']
start_time = time.time()
c[0]
end_time = time.time()

print("Time to access list[0]:", end_time-start_time)