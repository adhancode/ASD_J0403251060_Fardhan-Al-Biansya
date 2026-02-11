# Node untuk menyimpan data dan pointer ke node berikutnya
class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

# Class LinkedList
class LinkedList:
    def __init__(self):
        self.head = None  # Penunjuk ke node pertama

    # Menambahkan data ke akhir list
    def add(self, value):
        new_node = Node(value)

        if self.head is None:   # Jika list kosong
            self.head = new_node
            return

        current = self.head
        while current.next_node:   # Cari node terakhir
            current = current.next_node

        current.next_node = new_node  # Sambungkan node baru

    # Menampilkan isi linked list
    def show(self):
        if self.head is None:
            return "kosong"

        result = ""
        current = self.head

        while current:
            result += str(current.value) + " -> "
            current = current.next_node

        return result + "null"

    # Menggabungkan dua linked list
    def merge(self, other_list):
        merged_list = LinkedList()

        # Salin elemen list pertama
        current_self = self.head
        while current_self:
            merged_list.add(current_self.value)
            current_self = current_self.next_node

        # Salin elemen list kedua
        current_other = other_list.head
        while current_other:
            merged_list.add(current_other.value)
            current_other = current_other.next_node

        return merged_list

# Membuat dua linked list
list1 = LinkedList()
list2 = LinkedList()

# Input elemen list 1
input_list1 = input("Masukkan elemen untuk linked list 1: ")
if input_list1.strip() != "":
    for item in input_list1.split(","):
        list1.add(int(item.strip()))

# Input elemen list 2
input_list2 = input("Masukkan elemen untuk linked list 2: ")
if input_list2.strip() != "":
    for item in input_list2.split(","):
        list2.add(int(item.strip()))

# Tampilkan hasil
print("\nLinked list 1:", list1.show())
print("Linked list 2:", list2.show())

merged_result = list1.merge(list2)
print("Linked list setelah digabungkan:", merged_result.show())