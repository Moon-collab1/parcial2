class NodoCircular:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class ListaCircular:
    def __init__(self):
        self.head = None

    def insertar_final(self, dato):
        nuevo = NodoCircular(dato)

        if not self.head:
            self.head = nuevo
            nuevo.next = self.head
            return

        actual = self.head
        while actual.next != self.head:
            actual = actual.next

        actual.next = nuevo
        nuevo.next = self.head

    def crear_lista(self, n):
        for i in range(1, n + 1):
            self.insertar_final(i)

    def mostrar(self):
        if not self.head:
            print("Lista vacía")
            return

        resultado = []
        actual = self.head

        while True:
            resultado.append(str(actual.dato))
            actual = actual.next
            if actual == self.head:
                break

        print(" -> ".join(resultado) + " -> (ciclo)")

    def josephus_modificado(self, m):
        if not self.head:
            return None
        n=1
        actual = self.head.next
        while actual != self.head: 
            actual = actual.next
            n = n +1
        j=1
        act = self.head

        while j < n:
            a=1
            j=j+1
            while a < m:
                if act % 5 == 0:
                    act = act.next
                a = a + 1
                act = act.next
                if a == m:
                    act = None
                    break
            

        
    