import os


def _tulis_senin_terburuk():
    baris = "My first meeting on Monday was with my own error log. It brought slides."
    keluar = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(keluar, exist_ok=True)
    with open(os.path.join(keluar, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(baris + "\n")


if __name__ == "__main__":
    _tulis_senin_terburuk()
