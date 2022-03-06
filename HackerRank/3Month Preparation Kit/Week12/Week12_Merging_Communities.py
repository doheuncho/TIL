# Enter your code here. Read input from STDIN. Print output to STDOUT
n, q = input().split()
n, q = int(n), int(q)
network = [[i, 1] for i in range(n+1)]

for i in range(q):
    query = input().split()
    
    if query[0] == 'M':
        person1 = int(query[1])
        person2 = int(query[2])
        dummy = person2
        
        while network[person1][0] != person1:
            person1 = network[person1][0]
        while network[person2][0] != person2:
            person2 = network[person2][0]
        if person1 == person2:
            continue
        while dummy != person2:
            rep = network[dummy][0]
            network[dummy][0] = person1
            dummy = rep
        network[person2][0] = person1
        network[person1][1] += network[person2][1]
        
    else:
        person = int(query[1])
        while network[person][0] != person:
            person = network[person][0]
        print(network[person][1])
