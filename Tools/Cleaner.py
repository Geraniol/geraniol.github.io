import os
import shutil
import sys


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


def cleaner(path=".") -> None:

    for cp, dns, fns in os.walk(path, topdown=False):

        for dn in dns:
            if _match_dir(dn):
                dp = os.path.join(cp, dn)
                try:
                    shutil.rmtree(dp)
                    print('Removed dir:', dp)
                except:
                    print('Failed to remove dir:', dp)

        for fn in fns:
            if _match_file(fn):
                fp = os.path.join(cp, fn)
                try:
                    os.remove(fp)
                    print('Removed file:', fp)
                except:
                    print('Failed to remove file:', fp)


def clean_empty_files(path=".") -> None:

    for cp, dns, fns in os.walk(path, topdown=False):

        for fn in fns:
            fp = os.path.join(cp, fn)
            if not os.path.getsize(fp):
                try:
                    os.remove(fp)
                    print('Removed empty file:', fp)
                except:
                    print('Failed to remove empty file:', fp)


def clean_empty_dirs(path=".") -> None:

    flag = True
    while flag:
        flag = False
        for cp, dns, fns in os.walk(path, topdown=False):
            if not dns and not fns:
                try:
                    os.rmdir(cp)
                    print('Removed empty dir:', cp)
                    flag = True
                except:
                    print('Failed to remove empty dir:', cp)


if __name__ == "__main__":

    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "."

    cleaner(path)
    # clean_empty_files(path)
    # clean_empty_dirs(path)
