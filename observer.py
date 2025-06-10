# observer.py
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, pesan):
        pass

class Shelter(Observer):
    def __init__(self, nama):
        self.nama = nama
        self.notifikasi_masuk = [] # Untuk menyimpan notifikasi yang diterima

    def update(self, pesan):
        self.notifikasi_masuk.append(pesan)
        print(f"[Notifikasi untuk Shelter {self.nama}] {pesan}")

class Adopter(Observer): # Kelas Adopter sebagai Observer juga
    def __init__(self, nama):
        self.nama = nama
        self.notifikasi_masuk = []

    def update(self, pesan):
        self.notifikasi_masuk.append(pesan)
        print(f"[Notifikasi untuk Adopter {self.nama}] {pesan}")

class Subject: # Kelas Subject untuk mengirim notifikasi
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self, pesan):
        for observer in self._observers:
            observer.update(pesan)