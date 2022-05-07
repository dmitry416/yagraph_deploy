from collections import deque
import numpy as np


# пример графа
example_graph = {0: [-1, 11, -1, -1, 3, 1],
                 1: [11, -1, 8, -1, -1, 2],
                 2: [-1, 8, -1, 5, -1, 3],
                 3: [-1, -1, 5, -1, -1, 4],
                 4: [3, -1, -1, -1, -1, 10],
                 5: [1, 2, 3, 4, 10, -1]}

example_graph = {0: [-1, 1, -1, 1],
                 1: [1, -1, 1, -1],
                 2: [-1, 1, -1, 1],
                 3: [1, -1, 1, -1]}


# проверка запроса на валидность
def parse_request(req: dict):
    global algs
    if len(req.keys()) == 2:
        try:
            del_graph, alg = req['graph'], req['alg'].split(',')
            graph = {}
            for i in del_graph.keys():
                graph[int(i)] = del_graph[i]
            try:
                if len(alg) > 1:
                    return algs[alg[0]](graph, int(alg[1]))
                return algs[alg[0]](graph)
            except:
                return {'message': 'incorrect graph'}
        except KeyError:
            return {'message': 'incorrect args'}
    else:
        return {'message': 'incorrect number of args'}


def to_matrix(graph: dict, t=-1):
    return np.array([[j if j != -1 else t for j in i[1]] for i in list(sorted(graph.items(), key=lambda x: x[0]))])


# алгоритм поиска в ширину
def bfs(graph, _type='dict'):
    if _type == 'dict':
        graph = to_matrix(graph)
    n = len(graph)
    visited = [False] * n
    visited[0] = True
    queue = deque([0])
    while queue:
        vertex = queue.pop()
        for i in range(n):
            v = graph[i][vertex]
            if i != vertex and v != -1 and not visited[i]:
                queue.append(i)
                visited[i] = True
    return all(visited)


# алгоритм Дейктсры
def dij(graph, vert):
    graph = to_matrix(graph, t=float('inf'))
    n = len(graph)
    valid = [True] * n
    weight = [1000000] * n
    weight[vert] = 0
    for i in range(n):
        min_weight = 1000001
        ID_min_weight = -1
        for j in range(n):
            if valid[j] and weight[j] < min_weight:
                min_weight = weight[j]
                ID_min_weight = j
        for z in range(n):
            if weight[ID_min_weight] + graph[ID_min_weight][z] < weight[z]:
                weight[z] = weight[ID_min_weight] + graph[ID_min_weight][z]
        valid[ID_min_weight] = False
    return weight


def min_tree(graph: dict):
    graph = to_matrix(graph)
    n = len(graph)
    n_pairs = 0
    pairs = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            el = graph[i][j]
            if el > -1:
                pairs.append((i, j, el))
                n_pairs += 1

    pairs = list(sorted(pairs, key=lambda x: x[2]))[::-1]
    ans_pairs = set(pairs)
    idx = -1
    while n_pairs != n - 1:
        idx += 1
        v, u, _ = pairs[idx]
        local_graph = graph.copy()
        local_graph[v][u] = -1
        local_graph[u][v] = -1
        if bfs(graph, _type='matrix'):
            n_pairs -= 1
            graph = local_graph
            ans_pairs.remove(pairs[idx])

    ans_pairs = list(ans_pairs)
    s = int(sum([i[2] for i in ans_pairs]))
    ans_pairs = [i[:2] for i in ans_pairs]
    return [ans_pairs, s]


def is_eul(graph):
    graph = to_matrix(graph)
    odd = []
    n = len(graph)
    for i in range(n):
        d = 0
        for j in range(n):
            if graph[i][j] != -1:
                d += 1
        if d % 2 == 1:
            odd.append(i)

    if len(odd) > 1:
        return False
    elif len(odd) == 1:
        return odd[0]
    else:
        return 0


# алгоритм Эйлерова цикла
def get_eul(graph):
    v = is_eul(graph)
    graph = to_matrix(graph).copy().tolist()
    ans = []
    n = len(graph)
    if v is not False:
        queue = deque([v])
        while queue:
            v = queue.pop()
            d = n - graph[v].count(-1)
            if d == 0:
                ans.append(v)
            else:
                queue.append(v)
                for i in range(n):
                    if graph[v][i] != -1:
                        graph[v][i] = -1
                        graph[i][v] = -1
                        queue.append(i)
                        break
        return ans
    else:
        return False


# алгоритм проверки графа на дерево
def is_tree(graph: dict):
    n_graph = {}
    for i in graph.keys():
        n_graph[str(i)] = [str(j) for j in range(len(graph[i])) if graph[i][j] != -1]
    graph = n_graph
    import random
    verts = sorted(graph.keys())
    edges = set(''.join(sorted([i, j])) for i in graph.keys() for j in graph[i])
    visited = []
    if len(edges) != len(verts) - 1:
        return False

    def local_dfs(graph, vert: str, visited):
        visited.append(vert)
        for i in graph[vert]:
            if i not in visited:
                local_dfs(graph, i, visited)

    local_dfs(graph, random.choice(verts), visited)
    if len(visited) != len(verts):
        return False
    return True


algs = {'bfs': bfs,
        'dij': dij,
        'is_eul': get_eul,
        'is_tree': is_tree,
        'min_tree': min_tree}

# проверка работоспособности алгоритмов
# print(get_eul(example_graph))
# print(min_tree(example_graph))
# print(bfs(example_graph))
# graph3 = {'graph': {0: [-1, 11, -1, -1, 3, 1],
#                     1: [11, -1, 8, -1, -1, 2],
#                     2: [-1, 8, -1, 5, -1, 3],
#                     3: [-1, -1, 5, -1, -1, 4],
#                     5: [1, 2, 3, 4, 10, -1]},
#           'alg': 'min_tree'}
# print(min_tree(graph3['graph']))
# ex = {0: [-1, 0, 0],
#       1: [0, -1, -1],
#       2: [0, -1, -1]
#       }
# print(is_tree(ex))
