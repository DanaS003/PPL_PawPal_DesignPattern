# observer.py
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, pesan, target_observer_name=None): # Tambahkan parameter target_observer_name
        pass

class Shelter(Observer):
    def __init__(self, nama):
        self.nama = nama
        self.notifikasi_masuk = []

    def update(self, pesan, target_observer_name=None): # Sesuaikan tanda tangan metode
        if target_observer_name is None or target_observer_name == self.nama: # Filter di sini
            self.notifikasi_masuk.append(pesan)
            print(f"[Notifikasi untuk Shelter {self.nama}] {pesan}")
        # else:
            # print(f"Notifikasi untuk Shelter {self.nama} dilewati (bukan target): {pesan}") # Opsional: untuk debugging

class Adopter(Observer):
    def __init__(self, nama):
        self.nama = nama
        self.notifikasi_masuk = []

    def update(self, pesan, target_observer_name=None): # Sesuaikan tanda tangan metode
        if target_observer_name is None or target_observer_name == self.nama: # Filter di sini
            self.notifikasi_masuk.append(pesan)
            print(f"[Notifikasi untuk Adopter {self.nama}] {pesan}")
        # else:
            # print(f"Notifikasi untuk Adopter {self.nama} dilewati (bukan target): {pesan}") # Opsional: untuk debugging

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self, pesan, target_observer_name=None): # Tambahkan parameter target_observer_name
        for observer in self._observers:
            observer.update(pesan, target_observer_name) # Teruskan parameter