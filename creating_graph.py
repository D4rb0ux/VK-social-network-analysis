import requests
import networkx
import collections
import time

def get_friends_ids(user_id):
    friends_url = 'https://api.vk.com/method/friends.get?v=5.52&access_token=youraccesstoken&user_id={}'
    trottling_request(friends_url)
    json_response = requests.get(friends_url.format(user_id)).json()
    if json_response.get('error'):
        print(json_response.get('error'))
        return list()
    return json_response['response']['items']

def trottling_request(url):
    deq.appendleft(time.time())
    if len(deq) == 3:
        time.sleep(max(1+deq[2]-deq[0], 0))

deq = collections.deque(maxlen=3)
url = 'https://api.vk.com/method/friends.get?v=5.52&access_token=youraccesstoken&user_id={}'
my_id = #yourid
friends = requests.get(url.format(my_id)).json()
friend_ids = friends['response']['items']
graph = {}
for friend_id in friend_ids:
    graph[friend_id] = get_friends_ids(friend_id)

g = networkx.Graph(directed=False)
for i in graph:
    g.add_node(i)
    for j in graph[i]:
        if i != j and i in friend_ids and j in friend_ids:
            g.add_edge(i, j)

networkx.write_gexf(g, "graph.gexf")
