import os
import shutil


def _match_file(filename) -> bool:

    pattern_names = (
        ".DS_Store",
        "Thumbs.db",
        "desktop.ini",
    )

    pattern_starts = (
        "._",
    )

    pattern_ends = (
    )

    return (filename in pattern_names) or (filename.startswith(tuple(pattern_starts))) or (filename.endswith(tuple(pattern_ends)))


def _match_dir(dirname) -> bool:

    pattern_names = (
        ".Spotlight-V100",
        ".TemporaryItems",
        ".Trashes",
        ".fseventsd",
        "System Volume Information",
        "__MACOSX",
    )

    pattern_starts = (
    )

    pattern_ends = (
    )

    return (dirname in pattern_names) or (dirname.startswith(tuple(pattern_starts))) or (dirname.endswith(tuple(pattern_ends)))


def cleaner() -> None:

    for cp, dns, fns in os.walk(".", topdown=False):

        for dn in dns:
            if _match_dir(dn):
                dp = os.path.join(cp, dn)
                print('Removed dir:', dp)
                shutil.rmtree(dp)

        for fn in fns:
            if _match_file(fn):
                fp = os.path.join(cp, fn)
                print('Removed file:', fp)
                os.remove(fp)


def clean_empty_files() -> None:

    for cp, dns, fns in os.walk(".", topdown=False):

        for fn in fns:
            fp = os.path.join(cp, fn)
            if not os.path.getsize(fp):
                print('Removed empty file:', fp)
                os.remove(fp)


def clean_empty_dirs() -> None:

    flag = True
    while flag:
        flag = False
        for cp, dns, fns in os.walk(".", topdown=False):
            if not dns and not fns:
                print('Removed empty dir:', cp)
                os.rmdir(cp)
                flag = True


if __name__ == "__main__":
    cleaner()
    # clean_empty_files()
    # clean_empty_dirs()
