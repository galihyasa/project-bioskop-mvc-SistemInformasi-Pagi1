from typing import List, Optional

from rich.console import Console
from rich.table import Table
from rich import box

from .models import Film, Studio


class CLIView:
    def __init__(self) -> None:
        self.console = Console()

    # ---------- helper ----------
    def garis(self) -> None:
        print("-" * 55)

    def show_message(self, msg: str, style: Optional[str] = None) -> None:
        if style:
            self.console.print(f"[{style}]{msg}[/]")
        else:
            self.console.print(msg)

    # ---------- menu ----------
    def show_menu(self) -> str:
        self.console.print("[bold magenta]SISTEM PEMESANAN TIKET BIOSKOP[/]")
        self.console.print("[cyan]1.[/] Tambah Film")
        self.console.print("[cyan]2.[/] Tambah Studio")
        self.console.print("[cyan]3.[/] Lihat Film")
        self.console.print("[cyan]4.[/] Lihat Studio")
        self.console.print("[cyan]5.[/] Pesan Tiket")
        self.console.print("[cyan]6.[/] Keluar")
        pilihan = input("Pilih menu (1-6): ").strip()
        return pilihan

    # ---------- film ----------
    def tampil_film(self, data: List[Film]) -> None:
        if not data:
            self.console.print("[bold red]✖ Belum ada film.[/]")
            return

        table = Table(
            title="Daftar Film",
            box=box.ROUNDED,
            style="cyan",
        )
        table.add_column("ID", justify="center", style="yellow")
        table.add_column("Judul", style="bold white")
        table.add_column("Durasi (m)", justify="center")
        table.add_column("Rating", justify="center")

        for f in data:
            table.add_row(str(f.id), f.judul, str(f.durasi), f.rating)

        self.console.print(table)

    # ---------- studio ----------
    def tampil_studio(self, data: List[Studio]) -> None:
        if not data:
            self.console.print("[bold red]✖ Belum ada studio.[/]")
            return

        table = Table(
            title="Daftar Studio",
            box=box.ROUNDED,
            style="green",
        )
        table.add_column("ID", justify="center", style="yellow")
        table.add_column("Nama Studio", style="bold white")
        table.add_column("Kursi Tersedia", justify="center")

        for s in data:
            bebas = [k.nomor for k in s.kursi if not k.terisi]
            isi = ", ".join(bebas) if bebas else "PENUH"
            table.add_row(str(s.id), s.nama, isi)

        self.console.print(table)