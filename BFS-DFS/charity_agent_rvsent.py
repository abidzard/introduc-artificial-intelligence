from collections import defaultdict

map = {
    "B.Aceh": [{
            "Kota": "Sabang",
            "Jarak": 1000
        }, {
            "Kota": "Calang",
            "Jarak": 1000
        }, {
            "Kota": "Jantho",
            "Jarak": 1000
        }, {
            "Kota": "Sigli",
            "Jarak": 1500
        }
    ],
    "Calang": [{
        "Kota": "Meulaboh",
        "Jarak": 800
    }],
    "Meulaboh": [{
        "Kota": "Bl.Pidie",
        "Jarak": 1900
    }, {
        "Kota": "Simuelue",
        "Jarak": 500
    }],
    "Bl.Pidie": [{
        "Kota": "Tapaktuan",
        "Jarak": 1500
    }, {
        "Kota": "Singkil",
        "Jarak": 1800
    }],
    "Sigli": [{
        "Kota": "Bireuen",
        "Jarak": 1500
    }],
    "Bireuen": [{
        "Kota": "Takengon",
        "Jarak": 900
    }, {
        "Kota": "Lhokseumawe",
        "Jarak": 700
    }],
    "Takengon": [{
        "Kota": "Bl.Kejren",
        "Jarak": 800
    }, {
        "Kota": "Kutacane",
        "Jarak": 900
    }],
    "Lhokseumawe": [{
        "Kota": "Langsa",
        "Jarak": 900
    }, {
        "Kota": "Perlak",
        "Jarak": 1000
    }]
}

class Graph:

    def printPath(self, path):

        print("\nRecomended Path:")
        for i in path[:-1]:
            print(i, end=" > ")
        print(path[-1], end=f" ({self.calcLength(path)})\n")
        print()

    def BFS(self, _from, _target):

        self.result = []
        queue = [_from]

        while queue:
            _from = queue.pop(0)

            print(_from , end=f" - {self.calcLength(_from)} KM\n")

            if _from[-1] == _target:
                self.printPath(_from)
                self.result = _from

            if (_from[-1] in map):
                for kota in map[_from[-1]]:
                    new_list = list(_from)
                    new_list.append(kota["Kota"])
                    queue.append(new_list)

        return self.result
        


    def DFSUtil(self, _from, _target):
        
        self.result = []
        print(_from , end=f" - {self.calcLength(_from)} KM\n")

        if _from[-1] == _target:
            self.printPath(_from)
            self.result = _from

        if (_from[-1] in map):
            for neighbour in map[_from[-1]]:
                new_list = list(_from)
                new_list.append(neighbour["Kota"])
                self.DFSUtil(new_list, _target)

    def DFS(self, _from, _target):
        self.DFSUtil(_from, _target)
        return self.result

    def calcLength(self, daftarkota:list):
        length = 0
        for i in range(0, len(daftarkota) - 1):
            if daftarkota[i] in map:
                kota = map[daftarkota[i]]
                for j in kota:
                    if j["Kota"] == daftarkota[i+1]:
                        length += j["Jarak"]

        return length

g = Graph()
print("*** Breadth First Search:")
g.BFS(["B.Aceh"],"Bl.Pidie")

print("\n*** Depth First Search:")
g.DFS(["B.Aceh"],"Bl.Pidie")