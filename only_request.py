import requests


graph0 = {'graph': {0: [-1, 1, -1, 1],
                    1: [1, -1, 1, -1],
                    2: [-1, 1, -1, 1],
                    3: [1, -1, 1, -1]},
          'alg': 'dij, 1'}


graph1 = {'graph': {0: [-1, 1, -1, 1],
                    1: [1, -1, 1, -1],
                    2: [-1, 1, -1, 1],
                    3: [1, -1, 1, -1]},
          'alg': 'is_eul'}


graph2 = {'graph': {0: [-1, 1, -1, 1],
                    1: [1, -1, 1, -1],
                    2: [-1, 1, -1, 1],
                    3: [1, -1, 1, -1]},
          'alg': 'bfs'}

graph3 = {'graph': {0: [-1, 1, -1, 1],
                    1: [1, -1, 1, -1],
                    2: [-1, 1, -1, 1],
                    3: [1, -1, 1, -1]},
          'alg': 'min_tree'}

graph4 = {'graph': {0: [-1, 1, -1, 1],
                    1: [1, -1, 1, -1],
                    2: [-1, 1, -1, 1],
                    3: [1, -1, 1, -1]},
          'alg': 'is_tree',
          'extra argument': None}

graph5 = {'something': True,
          'else': False}

graph6 = {'graph': {0: [-1, 1, -1, 1],
                    1: [1, -1, 1, -1],
                    2: [-1, 1, -1, 1],
                    3: 123},
          'alg': 'is_tree'}

graph7 = {'graph': {0: [-1, 1, 1],
                    1: [1, -1, -1],
                    2: [-1, -1, -1],
                    },
          'alg': 'is_tree'}

print(requests.get('http://127.0.0.1:5000/api/', json=graph0).json())
print(requests.get('http://127.0.0.1:5000/api/', json=graph1).json())
print(requests.get('http://127.0.0.1:5000/api/', json=graph2).json())
print(requests.get('http://127.0.0.1:5000/api/', json=graph3).json())
print(requests.get('http://127.0.0.1:5000/api/', json=graph4).json())
print(requests.get('http://127.0.0.1:5000/api/', json=graph5).json())
print(requests.get('http://127.0.0.1:5000/api/', json=graph6).json())
print(requests.get('http://127.0.0.1:5000/api/', json=graph7).json())
