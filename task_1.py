import os
import shutil
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor


def copy_file(src: Path, dist: Path):
    """Копирует файл в папку dist/<расширение>/"""
    ext = src.suffix.lower().lstrip(".")
    if not ext:
        ext = "no_ext"

    target_dir = dist / ext
    target_dir.mkdir(parents=True, exist_ok=True)

    shutil.copy2(src, target_dir / src.name)


def scan_folder(folder: Path, dist: Path, executor):
    """Обходит папку и отправляет файлы на копирование"""
    for item in folder.iterdir():
        if item.is_file():
            executor.submit(copy_file, item, dist)
        elif item.is_dir():
            scan_folder(item, dist, executor)  # обычная рекурсия


def main():
    import sys

    if len(sys.argv) < 2:
        print("Использование: python sorter.py <source> [dist]")
        return

    source = Path(sys.argv[1])
    dist = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("dist")

    dist.mkdir(exist_ok=True)

    # Пул потоков только для копирования файлов
    with ThreadPoolExecutor(max_workers=8) as executor:
        scan_folder(source, dist, executor)

    print("Готово!")


if __name__ == "__main__":
    main()
