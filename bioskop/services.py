from typing import Dict, List, Type

from .models import Film, Studio, Kursi, Reguler, VIP, Tiket


class BioskopService:
    def __init__(self) -> None:
        self._film: Dict[int, Film] = {}
        self._studio: Dict[int, Studio] = {}
        self._tiket: Dict[int, Tiket] = {}

        self._id_film = 0
        self._id_studio = 0
        self._id_tiket = 0

    # ---------- Film ----------
    def tambah_film(self, judul: str, durasi: int, rating: str) -> Film:
        if not judul.strip():
            raise ValueError("Judul film tidak boleh kosong.")
        if durasi <= 0:
            raise ValueError("Durasi harus > 0.")

        self._id_film += 1
        f = Film(
            id=self._id_film,
            judul=judul.strip(),
            durasi=int(durasi),
            rating=rating.strip(),
        )
        self._film[f.id] = f
        return f

    def daftar_film(self) -> List[Film]:
        return list(self._film.values())

    # ---------- Studio ----------
    def tambah_studio(self, nama: str, jumlah_kursi: int, tipe_kursi: str) -> Studio:
        if jumlah_kursi <= 0:
            raise ValueError("Jumlah kursi harus > 0.")

        tipe_map: Dict[str, Type[Kursi]] = {
            "reguler": Reguler,
            "vip": VIP,
        }
        cls = tipe_map.get(tipe_kursi.lower())
        if cls is None:
            raise ValueError("Tipe kursi salah. Gunakan 'reguler' atau 'vip'.")

        # buat kursi 1..N
        kursi = [cls(str(i + 1)) for i in range(jumlah_kursi)]

        self._id_studio += 1
        s = Studio(
            id=self._id_studio,
            nama=nama.strip(),
            kursi=kursi,
        )
        self._studio[s.id] = s
        return s

    def daftar_studio(self) -> List[Studio]:
        return list(self._studio.values())

    # ---------- Tiket ----------
    def pesan_tiket(self, id_film: int, id_studio: int, nomor_kursi: str) -> Tiket:
        if id_film not in self._film:
            raise ValueError("Film tidak ditemukan.")
        if id_studio not in self._studio:
            raise ValueError("Studio tidak ditemukan.")

        studio = self._studio[id_studio]
        kursi = next((k for k in studio.kursi if k.nomor == nomor_kursi), None)
        if kursi is None:
            raise ValueError("Nomor kursi tidak valid.")
        if kursi.terisi:
            raise ValueError("Kursi sudah terisi.")

        kursi.set_terisi(True)
        harga = kursi.harga()

        self._id_tiket += 1
        t = Tiket(
            id=self._id_tiket,
            film_id=id_film,
            studio_id=id_studio,
            kursi_nomor=nomor_kursi,
            harga=harga,
        )
        self._tiket[t.id] = t
        return t

    def daftar_tiket(self) -> List[Tiket]:
        return list(self._tiket.values())