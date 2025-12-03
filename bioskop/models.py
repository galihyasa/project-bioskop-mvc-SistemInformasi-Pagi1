from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import List


# ==================== FILM ====================

@dataclass
class Film:
    id: int
    judul: str
    durasi: int   # menit
    rating: str


# ==================== KURSI ====================

class Kursi(ABC):
    def __init__(self, nomor: str) -> None:
        self._nomor = nomor
        self._terisi = False   # encapsulation

    @property
    def nomor(self) -> str:
        return self._nomor

    @property
    def terisi(self) -> bool:
        return self._terisi

    def set_terisi(self, status: bool) -> None:
        self._terisi = bool(status)

    @abstractmethod
    def harga(self) -> float:
        """Polymorphism: harga berbeda sesuai tipe kursi"""
        ...


class Reguler(Kursi):
    def harga(self) -> float:
        return 35000


class VIP(Kursi):
    def harga(self) -> float:
        return 60000


# ==================== STUDIO ====================

@dataclass
class Studio:
    id: int
    nama: str
    kursi: List[Kursi]   # list of Kursi


# ==================== TIKET ====================

@dataclass
class Tiket:
    id: int
    film_id: int
    studio_id: int
    kursi_nomor: str
    harga: float