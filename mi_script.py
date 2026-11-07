# mi_script.py
import platform
import datetime

AUTOR = "Lina Sofia Ballesteros Merchan | Alejandro Rios Muñoz"

def main():
    print(f"Autor: {AUTOR}")
    print(f"Sistema Operativo: {platform.system()} {platform.release()}")
    print(f"Fecha y hora desde Python: {datetime.datetime.now()}")

if __name__ == "__main__":
    main()
