from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path


HTML_LINK_RE = re.compile(
    r'<a\s+href="([^"]+)"[^>]*>(.*?)</a>',
    flags=re.IGNORECASE | re.DOTALL,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build standalone XeLaTeX and PDF release documents from README.md."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("README.md"),
        help="Source Markdown file. Default: README.md",
    )
    parser.add_argument(
        "--version",
        required=True,
        help="Release version, for example: v1.3.0",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("dist"),
        help="Directory for generated release artifacts. Default: dist",
    )
    return parser.parse_args()


def require_command(command: str) -> None:
    if shutil.which(command) is None:
        raise RuntimeError(
            f"Required command '{command}' was not found on PATH."
        )


def convert_html_links_to_markdown(markdown: str) -> str:
    """Convert README HTML anchors into Markdown links for Pandoc."""

    def replace(match: re.Match[str]) -> str:
        url = match.group(1).strip()
        label = match.group(2).strip()
        return f"[{label}]({url})"

    return HTML_LINK_RE.sub(replace, markdown)


def prepare_markdown(source: Path, version: str) -> str:
    content = source.read_text(encoding="utf-8")
    content = convert_html_links_to_markdown(content)

    # The generated document has its own title page.
    content = re.sub(
        r"^\s*\[!\[Awesome\].*?\n",
        "",
        content,
        count=1,
        flags=re.MULTILINE,
    )

    content = re.sub(
        r"^#\s+Awesome Financial Crime\s*$",
        "",
        content,
        count=1,
        flags=re.MULTILINE,
    )

    # Remove the README's manually maintained Table of Contents.
    # Pandoc/XeLaTeX generates the PDF Contents automatically.
    content = re.sub(
        r"^##\s+Table of Contents\s*\n.*?(?=^##\s+|\Z)",
        "",
        content,
        count=1,
        flags=re.MULTILINE | re.DOTALL,
    )

    metadata = f"""---
title: "Awesome Financial Crime"
subtitle: "Curated Financial Crime Compliance Resources"
author: "SKR-35"
date: "{date.today().isoformat()}"
version: "{version}"
---

"""

    return metadata + content.lstrip()


def build_tex(
    prepared_markdown: Path,
    tex_path: Path,
    version: str,
) -> None:
    command = [
        "pandoc",
        str(prepared_markdown),
        "--from=gfm",
        "--to=latex",
        "--standalone",
        "--toc",
        "--toc-depth=3",
        "--pdf-engine=xelatex",
        "--variable",
        "documentclass=article",
        "--variable",
        "geometry:margin=1in",
        "--variable",
        "fontsize=10pt",
        "--variable",
        "linkcolor=blue",
        "--variable",
        "urlcolor=blue",
        "--variable",
        "colorlinks=true",
        "--metadata",
        f"version={version}",
        "-o",
        str(tex_path),
    ]

    subprocess.run(command, check=True)


def add_page_break_after_contents(tex_path: Path) -> None:
    """Insert a page break immediately after Pandoc's generated Contents."""
    tex = tex_path.read_text(encoding="utf-8")

    marker = r"\tableofcontents"
    replacement = "\\tableofcontents\n\\clearpage"

    if marker not in tex:
        raise RuntimeError(
            "Pandoc generated the TeX file, but no \\tableofcontents command was found."
        )

    tex = tex.replace(marker, replacement, 1)
    tex_path.write_text(tex, encoding="utf-8")


def compile_pdf(tex_path: Path, output_dir: Path) -> Path:
    command = [
        "xelatex",
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-file-line-error",
        f"-output-directory={output_dir}",
        str(tex_path),
    ]

    # Two passes ensure the Contents page and references settle correctly.
    subprocess.run(command, check=True)
    subprocess.run(command, check=True)

    return output_dir / f"{tex_path.stem}.pdf"


def clean_auxiliary_files(output_dir: Path, stem: str) -> None:
    extensions = {
        ".aux",
        ".log",
        ".out",
        ".toc",
    }

    for extension in extensions:
        path = output_dir / f"{stem}{extension}"
        if path.exists():
            path.unlink()


def main() -> int:
    args = parse_args()

    source = args.input.resolve()
    output_dir = args.output_dir.resolve()

    if not source.is_file():
        print(f"Input file not found: {source}", file=sys.stderr)
        return 1

    try:
        require_command("pandoc")
        require_command("xelatex")

        output_dir.mkdir(parents=True, exist_ok=True)

        safe_version = args.version.replace("/", "-")
        stem = f"Awesome_Financial_Crime_{safe_version}"

        tex_path = output_dir / f"{stem}.tex"

        prepared_content = prepare_markdown(source, args.version)

        with tempfile.TemporaryDirectory() as temp_dir:
            prepared_markdown = Path(temp_dir) / "README_release.md"
            prepared_markdown.write_text(
                prepared_content,
                encoding="utf-8",
            )

            build_tex(
                prepared_markdown=prepared_markdown,
                tex_path=tex_path,
                version=args.version,
            )

        # Keep the generated .tex as a release artifact and start the
        # document body on a fresh page after the generated Contents.
        add_page_break_after_contents(tex_path)

        pdf_path = compile_pdf(
            tex_path=tex_path,
            output_dir=output_dir,
        )

        clean_auxiliary_files(
            output_dir=output_dir,
            stem=stem,
        )

    except (RuntimeError, subprocess.CalledProcessError) as exc:
        print(f"Build failed: {exc}", file=sys.stderr)
        return 1

    print("Release documentation built successfully:")
    print(f"  TeX: {tex_path}")
    print(f"  PDF: {pdf_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
