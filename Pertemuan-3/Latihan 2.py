class Node:
    def __init__(self, data):
        self.data = data      # Menyimpan data
        self.next = None      # Pointer ke node berikutnya

class CircularLinkedList:
    def __init__(self):
        self.head = None     # Node awal (kosong)

    def append(self, data):
        new_node = Node(data)

        # Jika list kosong
        if self.head is None:
            self.head = new_node
            new_node.next = new_node  # Menunjuk ke diri sendiri (circular)
            return

        # Cari node terakhir
        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head  # Node baru menunjuk ke head

    def is_empty(self):
        return self.head is None  # Cek apakah list kosong

    def search(self, key):
        if self.is_empty():
            return False

        current = self.head
        while True:
            if current.data == key:
                return True
            current = current.next
            if current == self.head:  # Berhenti jika sudah satu putaran
                break

        return False

def main():
    circular_list = CircularLinkedList()

    input_data = input("Masukkan elemen ke dalam Circular Linked List: ").strip()

    if input_data != "":
        data_list = input_data.split(",")
        for item in data_list:
            circular_list.append(int(item.strip()))

    if circular_list.is_empty():
        print("Circular Linked List kosong.")
        return

    search_value = int(input("Masukkan elemen yang ingin dicari: "))

    if circular_list.search(search_value):
        print("Elemen ditemukan.")
    else:
        print("Elemen tidak ditemukan.")

if __name__ == "__main__":
    main()
