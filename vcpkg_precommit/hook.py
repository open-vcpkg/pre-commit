import argparse
import os
import platform
import subprocess
import tempfile
from pathlib import Path
from typing import Optional, Sequence
from urllib.request import urlretrieve


def get_vcpkg_binary() -> Path:
    """Download and return path to vcpkg binary for current platform."""
    system = platform.system().lower()
    machine = platform.machine().lower()

    binary_map = {
        ("windows", "amd64"): ("vcpkg.exe", "vcpkg-windows-x64.exe"),
        ("linux", "x86_64"): ("vcpkg", "vcpkg-glibc"),
        ("darwin", "arm64"): ("vcpkg", "vcpkg-macos"),
        ("darwin", "x86_64"): ("vcpkg", "vcpkg-macos"),
    }

    if (system, machine) not in binary_map:
        raise Exception(f"Unsupported platform: {system} {machine}")

    binary_name, url_suffix = binary_map[(system, machine)]
    url = f"https://github.com/microsoft/vcpkg-tool/releases/latest/download/{url_suffix}"

    vcpkg_dir = Path.home() / ".vcpkg"
    vcpkg_dir.mkdir(exist_ok=True)

    vcpkg_path = vcpkg_dir / binary_name

    if not vcpkg_path.exists():
        print(f"Downloading vcpkg from {url}...")
        urlretrieve(url, vcpkg_path)
        vcpkg_path.chmod(0o755)

    return vcpkg_path


def format_manifest_vcpkg_json(filename: str, vcpkg_binary: Path) -> bool:
    """Format a single vcpkg.json file."""
    os.environ["VCPKG_ROOT"] = tempfile.TemporaryDirectory()
    result = subprocess.run(
        [str(vcpkg_binary), "format-manifest", "--x-wait-for-lock", filename],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(f"Error formatting {filename}:")
        print(result.stderr)
        return False

    return True


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to check")
    args = parser.parse_args(argv)

    try:
        vcpkg_binary = get_vcpkg_binary()

        retval = 0
        for filename in args.filenames:
            print(f"Formatting {filename}...")
            if not format_manifest_vcpkg_json(filename, vcpkg_binary):
                retval = 1

        return retval

    except Exception as e:
        print(f"Error: {str(e)}")
        return 1


if __name__ == "__main__":
    exit(main())
