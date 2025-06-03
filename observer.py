from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, pesan):
        pass

class Shelter(Observer):
    def __init__(self, nama):
        self.nama = nama

    def update(self, pesan):
        print(f"[Notifikasi untuk {self.nama}] {pesan}")
