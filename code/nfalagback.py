from graphviz import Digraph
stack = []
def top(stack):
    if len(stack):
        return stack[len(stack)-1]
    return 0
dfa = Digraph()
s = ""
flag = 0
last_node = 0
count = 0
n = 0
nostar = 0
i1 = 0
next = 1
forloop = 0
st = ""
whole_star = 0
lag1 = 0
lag = input("enter the language (eg: aa a* b*): ").split()
check = input("enter the input to check (eg: aaabb): ")
lag_size = len(lag)
phi = ""
for i in lag:
    for j in i:
        if j != '*':
            phi = phi + j

for i in check[::-1]:
    stack.append(i)
print(len(lag))
for i in lag:
    i1 = i1 + 1
    for j in i:
        if j == '*':
            count = 1
    if count == 1:
        last_node = last_node + len(i)-1
    else:
        last_node = last_node + len(i)
last_node = last_node + 1

for i in lag:
    for j in i:
        if j == '*':
            whole_star = whole_star + 1


if whole_star == len(lag):
    whole_star = 1
else:
    whole_star = 0
i1 = 0
for i in lag:
    forloop = forloop + 1
    count1 = 0
    i1 = i1 + 1
    if n!=0:
        n=n-1
    count = 0
    for j in i:
        if j == '*':
            count = 1
    if len(lag) == 1 and count == 1:
        #q0 final state and loops to it self
        if len(i) == 2:
            dfa.attr('node', shape = 'doublecircle')
            dfa.node('q0')
            for x in lag[0]:
                if x != '*':
                    s = x
            dfa.edge('q0','q0',label=(s))
            dfa.render('dfa', view=True)
        else:
            for x in range(len(i)-1):
                    dfa.attr('node',shape = 'circle')
                    dfa.node('q'+str(x))
            dfa.attr('node',shape = 'doublecircle')
            dfa.node('q'+str(x+1))
            for x in range(len(i)-1):
                for y in range(len(i)-1):
                    if x != y:
                        dfa.attr('node',shape='circle')
                dfa.edge('q'+str(x),'q'+str(x+1),label=(i[x]))
            dfa.edge('q'+str(x+1),'q1',label=(i[0]))
            
        
    elif len(lag) == 1:
        for j in range(len(i)):
            if j < len(i):
                dfa.attr('node',shape = 'circle')
                dfa.node('q'+str(j))

        dfa.attr('node',shape = 'doublecircle')
        dfa.node('q'+str(j+1))
        dfa.attr('node',shape = 'circle')

        for j in range(len(i)):
                
            dfa.edge('q'+str(j),'q'+str(j+1),label=(i[j]))
        #q0 to q1, q1 final state
    else:
        lag_size = lag_size-1
        star = 0
        for j in i:
            if j == '*':
                star = 1
        if star == 1:
            lag1 = lag1 + 1
            if whole_star == 0:
                print("not whole_star")
                s = ""
                for j in i:
                    if j != '*':
                        s = s+j
                limit = 0
                for x in s:
                    dfa.attr('node',shape = 'circle')
                    dfa.node('q'+str(n))
                    n = n + 1
                    limit = limit + 1
                    if limit == 1:
                        q = n
                c = n - limit
                if i1 == len(lag):
                    dfa.attr('node',shape = 'doublecircle')
                    dfa.node('q'+str(len(i)-1))
                for x in range(len(s)):
                    if x!=limit:   
                        dfa.edge(str('q'+str(c)),str('q'+str(c+1)),label=(s[x]))
                        c = c+1
                            
                dfa.edge(str('q'+str(n)),str('q'+str(q)),label=s[0])
                n=n+1

            else:
                print("whole_star")
                s = ""
                for j in i:
                    if j != '*':
                        s = s+j
                limit = 0
                for x in s:
                    dfa.attr('node',shape = 'doublecircle')
                    dfa.node('q'+str(n))
                    n = n + 1
                    limit = limit + 1
                    if limit == 1:
                        q = n
                c = n - limit
                if i1 == len(lag):
                    dfa.attr('node',shape = 'doublecircle')
                    dfa.node('q'+str(len(i)-1))
                for x in range(len(s)):
                
                    if x!=limit:
                        
                        dfa.edge(str('q'+str(c)),str('q'+str(c+1)),label=(s[x]))
                        c = c+1

                dfa.edge(str('q'+str(n)),str('q'+str(q)),label=s[0])
                n=n+1


            
            #for x in s:
                #qn to qn+o path x
            #qn+o to qn+1 path s[0]
        else:
            #check if both * and no * is same later
            lag_size=lag_size-1
            lag1 = lag1 +1
            s = ""
            for j in i:
                s = s+j
            
            limit = 0
            last = n
            for x in range(len(s)+1):
                if n<last_node:
                    dfa.attr('node',shape = 'circle')
                    dfa.node('q'+str(n))
                else:
                    dfa.attr('node',shape = 'doublecircle')
                    dfa.node('q'+str(n))
                n = n + 1
            dfa.attr('node',shape = 'doublecircle')
            dfa.node('q'+str(n-1))
            for x in range(len(s)):
                    dfa.edge(str('q'+str(last)),str('q'+str(last+1)),label = (s[x]))
                    last = last + 1


            #for x in s:
                #qn to qn+o path x
            #qn+o final state

    if count != 1:
        for j in i:
            if (len(stack)):
                nostar = nostar + 1
                print("top",top(stack),"j",j)
                if top(stack) == j:
                    stack.pop()
  
                else:
                    print("line 116")
                    print("rejected")
                    print("not *")
                    exit()
            else:
                print("line 121")
                print("rejected")
                exit()

    else:
        st = ""
        for j in i:
            if j != '*':
                st = st+j

        if len(st)==1:
            for x in st:
                while (x==top(stack)):
                    stack.pop()

        else:

            flag = 0
            count1 = 0
            whileloop = 0
            while(top(stack) and flag == 0):
                whileloop = whileloop + 1
                for x in st:
                    if top(stack) == x:
                        pop = stack.pop()
                        count1 = count1 + 1
                        if len(lag)>1:
                            if lag[next][0]==x and whileloop > 1:
                                count1=count1-1
                                stack.append(pop)
                    else:
                        flag = 1
                        break
                if flag == 1:
                    if count1 !=0:
                        if len(st) % count1 != 0:
                            print("line 159")
                            print("rejected")
                            exit()
                    break
        if next+1<len(lag) and forloop > 0:
            next = next + 1


if len(stack):
    print("line 240")
    print("rejected")
else:
    print("line 243")
    print("accepted")

print("n",n)

dfa.render('dfa', view = True)
