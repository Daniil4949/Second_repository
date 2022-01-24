graph={}
graph['you']=['alice','bob','claire']
graph['bob']=['anuj','peggy']
graph['claire']=['thom','jonny']
graph['alice']=['peggy']
graph['anuj']=[]
graph['peggy']=[]
graph['thom']=[]
graph['jonny']=[]
def person_is_seller(name):
    return name[-1]=='m'
from collections import deque
search_queue=deque()
search_queue+=graph['you']
while search_queue:
    person=search_queue.popleft()
    if person_is_seller(person):
        print(person,'is a mango seller!')
    else:
        search_queue+=graph[person]




