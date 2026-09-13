"""Keep Pages code blocks and the downloadable lesson package in sync."""
import argparse
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "beispiele/snake"
ARCHIVE = ROOT / "docs/assets/downloads/snake-unterricht.zip"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    outdated = []
    for page in (ROOT / "docs/ki-snake").glob("*.md"):
        text = page.read_text(encoding="utf-8")

        def block(match):
            name = match.group(1)
            code = (SOURCE / name).read_text(encoding="utf-8").rstrip()
            return "<!-- CODE:" + name + " -->\n```python\n" + code + "\n```\n<!-- END CODE -->"

        updated = re.sub(r"<!-- CODE:([\w.]+) -->.*?<!-- END CODE -->", block, text, flags=re.S)
        if updated != text:
            outdated.append(str(page.relative_to(ROOT)))
            if not args.check:
                page.write_text(updated, encoding="utf-8")

    files = sorted(p for p in SOURCE.iterdir() if p.is_file() and p.suffix in {".py", ".md", ".txt"})
    expected = {"snake/" + p.name: p.read_bytes() for p in files}
    actual = {}
    if ARCHIVE.exists():
        with zipfile.ZipFile(ARCHIVE) as archive:
            actual = {name: archive.read(name) for name in archive.namelist()}
    if actual != expected:
        outdated.append(str(ARCHIVE.relative_to(ROOT)))
        if not args.check:
            ARCHIVE.parent.mkdir(parents=True, exist_ok=True)
            with zipfile.ZipFile(ARCHIVE, "w", zipfile.ZIP_DEFLATED) as archive:
                for name, data in expected.items():
                    archive.writestr(name, data)
    if args.check and outdated:
        raise SystemExit("Out of sync: " + ", ".join(outdated))
    print("Snake pages and download are in sync." if args.check else "Snake pages and download updated.")


if __name__ == "__main__":
    main()
