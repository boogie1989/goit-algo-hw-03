import os
import shutil
import sys


def copy_files_recursively(source_dir, dest_dir):
    for item in os.listdir(source_dir):
        item_path = os.path.join(source_dir, item)
        if os.path.isdir(item_path):
            # Якщо елемент є директорією, викликаємо функцію рекурсивно
            copy_files_recursively(item_path, dest_dir)
        else:
            # Визначаємо піддиректорію для файлу на основі його розширення
            file_ext = item.split('.')[-1]
            if not file_ext:
                file_ext = 'without_extension'
            ext_dir = os.path.join(dest_dir, file_ext)
            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir)
            dest_file_path = os.path.join(ext_dir, item)
            try:
                shutil.copy2(item_path, dest_file_path)
                print(f"Файл {item_path} скопійовано до {dest_file_path}")
            except Exception as e:
                print(f"Помилка при копіюванні файлу {item_path}: {e}")


def main():
    # Парсинг аргументів командного рядка
    if len(sys.argv) < 2:
        print(
            "Використання: python script.py <шлях до вихідної директорії> [шлях до директорії призначення]")
        sys.exit(1)

    source_dir = sys.argv[1]
    if len(sys.argv) == 3:
        dest_dir = sys.argv[2]
    else:
        dest_dir = 'dist'

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    try:
        copy_files_recursively(source_dir, dest_dir)
    except Exception as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    main()
