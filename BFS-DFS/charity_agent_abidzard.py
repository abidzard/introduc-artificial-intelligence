from queue import Queue
import queue

grafKota = {
    "Banda Aceh":["Sabang", "Calang", "Jantho", "Sigli"],
    "Sabang":["Banda Aceh"],
    "Calang":["Meulaboh"],
    "Jantho":["Banda Aceh"],
    "Sigli":["Banda Aceh", "Bireun"],
    "Meulaboh":["Calang", "Bl.Pidie", "Simuelue"],
    "Bireun":["Sigli", "Takengon", "Lhokseumawe"],
    "Bl.Pidie":["Meulaboh", "Tapak Tuan", "Singkil"],
    "Simuelue":["Meulaboh"],
    "Takengon":["Bireun", "Bl.Krejen", "Kutacane"],
    "Lhokseumawe":["Bireun", "Langsa", "Perlak"],
    "Tapak Tuan":["Bl.Pidie"],
    "Singkil":["Bl.Pidie"],
    "Bl.Krejen":["Takengon"],
    "Kutacane":["Takengon"],
    "Langsa":["Lhokseumawe"],
    "Perlak":["Lhokseumawe"]
}

# code breadth first metode
dikunjungi = {}
tingkat = {}    # jarak tree
parent = {}
bfs = []
queue = Queue()

for node in grafKota.keys():
    dikunjungi[node] = False
    parent[node] = None
    tingkat[node] = -1 #inf

titik = "Banda Aceh"    # titik awal
dikunjungi[titik] = True
tingkat[titik] = 0
queue.put(titik)

while not queue.empty():
    u = queue.get()
    bfs.append(u)

    for v in grafKota[u]:
        if not dikunjungi[v]:
            dikunjungi[v] = True
            parent[v] = u
            tingkat[v] = tingkat[u]+1
            queue.put(v)

# jarak terdekat
v = "Bl.Pidie"
path = []
while v is not None:
    path.append(v)
    v = parent[v]
path.reverse()

# cetak hasil
print("Metode Pencarian Breadth First Search :")
print(bfs)
print("Jarak terdekat Banda Aceh -> Bl.Pidie : " + str(path))
print("Posisi Bl.Pidie : " + str(tingkat["Bl.Pidie"]))