class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# kelas DoublyLinkedList yang merepresentasikan double linked list itu sendiri. 
class DoublyLinkedList:
    def __init__(self):
        # satu atribut yaitu head yang akan digunakan untuk menunjukkan simpul pertama dalam linked list.
        self.head = None

    # fungsi append(data) untuk menambahkan elemen baru di akhir linked list.
    def append(self, data):
        new_node = Node(data)
        # Jika linked list kosong, simpul baru akan jadi simpul pertama (head).
        if self.head is None:
            self.head = new_node
        # Jika tidak, cari simpul terakhir pakai while, kemudian tambah simpul baru sebagai simpul selanjutnya (next) dari simpul terakhir.
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    # fungsi prepend(data) untuk menambahkan elemen baru di awal linked list.
    def prepend(self, data):
        new_node = Node(data)
        # Jika linked list kosong, simpul baru akan jadi simpul pertama (head).
        if self.head is None:
            self.head = new_node
        # Jika tidak, simpul baru akan ditambahkan di awal dengan mengatur referensi next dari simpul baru ke simpul pertama saat ini, dan mengatur referensi prev dari simpul pertama saat ini ke simpul baru.
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # fungsi print_list() untuk mencetak isi linked list. 
    def print_list(self):
        # mulai dari simpul pertama (head) dan cetak nilai data dari setiap simpul dengan while. 
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Membuat objek DoublyLinkedList  (dllist = instance dari kelas DoublyLinkedList)
dllist = DoublyLinkedList()

# Menambahkan elemen ke linked list
dllist.append(1)
dllist.append(2)
dllist.append(3)

# Menambahkan elemen di awal linked list
dllist.prepend(4)
dllist.prepend(5)

# Menampilkan linked list
dllist.print_list()



