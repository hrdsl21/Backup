import shutil
import os
import pyfiglet
import zipfile


baner_text = pyfiglet.figlet_format("Program do kopiowania")
print(baner_text)


a = input("\nPodaj folder zródłowy: ")
b = input("\nPodaj folder docelowy: ")


def kopia_zapasowa(src_folder, dest_folder):
    try:
        # Sprawdzenie, czy folder docelowy istnieje, jeśli nie, to go utworzy
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)

        zip_filename = os.path.join(dest_folder, 'kopia.zip')

        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(src_folder):
                for file in files:
                    src_path = os.path.join(root, file)
                    rel_path = os.path.relpath(src_path, src_folder)
                    zipf.write(src_path, rel_path)

        print("Utworzono kopię zapasową folderu")
    except shutil.Error as e:
        print(f"Błąd kopiowania: {e}")
    except OSError as e:
        print(f"Błąd systemu operacyjnego: {e}")


src_folder = a
dest_folder = b

kopia_zapasowa(src_folder, dest_folder)
