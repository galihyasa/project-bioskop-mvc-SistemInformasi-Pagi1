from .services import BioskopService
from .view import CLIView


class BioskopController:
    def __init__(self, service: BioskopService, view: CLIView) -> None:
        self.service = service
        self.view = view

    def run(self) -> None:
        while True:
            pilihan = self.view.show_menu()

            if pilihan == "1":
                self.tambah_film()
            elif pilihan == "2":
                self.tambah_studio()
            elif pilihan == "3":
                self.lihat_film()
            elif pilihan == "4":
                self.lihat_studio()
            elif pilihan == "5":
                self.pesan_tiket()
            elif pilihan == "6":
                print("Sampai jumpa! 👋")
                break
            else:
                print("Pilihan tidak valid.")

    # ---------- handler tiap menu ----------

    def tambah_film(self) -> None:
        try:
            judul = input("Judul film        : ")
            durasi = int(input("Durasi (menit)    : "))
            rating = input("Rating (SU/13+/D) : ")
            f = self.service.tambah_film(judul, durasi, rating)
            print(f"✅ Film ditambahkan. ID={f.id}")
        except Exception as e:
            print("❌", e)

    def tambah_studio(self) -> None:
        try:
            nama = input("Nama studio                : ")
            jumlah = int(input("Jumlah kursi              : "))
            tipe = input("Tipe kursi (reguler/vip)  : ")
            s = self.service.tambah_studio(nama, jumlah, tipe)
            print(f"✅ Studio ditambahkan. ID={s.id}")
        except Exception as e:
            print("❌", e)

    def lihat_film(self) -> None:
        data = self.service.daftar_film()
        self.view.tampil_film(data)

    def lihat_studio(self) -> None:
        data = self.service.daftar_studio()
        self.view.tampil_studio(data)

    def pesan_tiket(self) -> None:
        try:
            self.lihat_film()
            id_f = int(input("Pilih ID film    : "))
            self.lihat_studio()
            id_s = int(input("Pilih ID studio  : "))
            nomor = input("Pilih nomor kursi: ").strip()

            t = self.service.pesan_tiket(id_f, id_s, nomor)
            print(
                f"✅ TiketID={t.id} | Kursi {t.kursi_nomor} | "
                f"Harga Rp{int(t.harga):,}".replace(",", ".")
            )
        except Exception as e:
            print("❌", e)