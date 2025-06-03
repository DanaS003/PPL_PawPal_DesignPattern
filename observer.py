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

class Mediator(ABC): # Kelas baru untuk Mediator
    @abstractmethod
    def notify(self, sender, event):
        pass

class AdoptionMediator(Mediator): # Implementasi Mediator
    def __init__(self, shelter):
        self._shelter = shelter

    def notify(self, sender, event):
        if event == "adopsi_diajukan":
            self._shelter.update(f"Permintaan adopsi baru diajukan dari {sender.user} untuk {sender.hewan.nama}")