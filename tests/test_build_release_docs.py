from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "build_release_docs.py"

spec = importlib.util.spec_from_file_location("build_release_docs", SCRIPT_PATH)
if spec is None or spec.loader is None:
    raise ImportError(f"Could not load build script from {SCRIPT_PATH}")

build_release_docs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build_release_docs)

add_page_break_after_contents = build_release_docs.add_page_break_after_contents
clean_auxiliary_files = build_release_docs.clean_auxiliary_files
convert_html_links_to_markdown = build_release_docs.convert_html_links_to_markdown
prepare_markdown = build_release_docs.prepare_markdown


def test_convert_html_links_to_markdown() -> None:
    source = (
        'See <a href="https://example.com">Official Page</a> '
        "for more information."
    )

    result = convert_html_links_to_markdown(source)

    assert result == (
        "See [Official Page](https://example.com) "
        "for more information."
    )


def test_prepare_markdown_removes_readme_toc_and_title(tmp_path: Path) -> None:
    readme = tmp_path / "README.md"
    readme.write_text(
        """# Awesome Financial Crime

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated financial crime resource list.

## Table of Contents

- [Vendor / Commercial Platforms](#vendor--commercial-platforms)
- [Transaction Monitoring](#transaction-monitoring)

## Vendor / Commercial Platforms

Commercial tools are useful for discovery.

## Transaction Monitoring

Streaming and monitoring tools.
""",
        encoding="utf-8",
    )

    result = prepare_markdown(readme, "v1.3.0")

    assert 'title: "Awesome Financial Crime"' in result
    assert 'version: "v1.3.0"' in result
    assert "# Awesome Financial Crime" not in result
    assert "[![Awesome]" not in result
    assert "## Table of Contents" not in result
    assert "[Vendor / Commercial Platforms](#vendor--commercial-platforms)" not in result
    assert "## Vendor / Commercial Platforms" in result
    assert "## Transaction Monitoring" in result
    assert "A curated financial crime resource list." in result


def test_add_page_break_after_contents(tmp_path: Path) -> None:
    tex_path = tmp_path / "document.tex"
    tex_path.write_text(
        "\\begin{document}\n"
        "\\tableofcontents\n"
        "\\section{Vendor / Commercial Platforms}\n",
        encoding="utf-8",
    )

    add_page_break_after_contents(tex_path)

    result = tex_path.read_text(encoding="utf-8")

    assert (
        "\\tableofcontents\n"
        "\\clearpage\n"
        "\\section{Vendor / Commercial Platforms}"
    ) in result


def test_add_page_break_after_contents_raises_when_toc_missing(
    tmp_path: Path,
) -> None:
    tex_path = tmp_path / "document.tex"
    tex_path.write_text(
        "\\begin{document}\n"
        "\\section{Vendor / Commercial Platforms}\n",
        encoding="utf-8",
    )
        
    with pytest.raises(
        RuntimeError,
        match=r"tableofcontents command was found",
    ):
        add_page_break_after_contents(tex_path)


def test_clean_auxiliary_files_keeps_release_artifacts(tmp_path: Path) -> None:
    stem = "Awesome_Financial_Crime_v1.3.0"

    auxiliary_extensions = [".aux", ".log", ".out", ".toc"]
    for extension in auxiliary_extensions:
        (tmp_path / f"{stem}{extension}").write_text(
            "temporary",
            encoding="utf-8",
        )

    tex_path = tmp_path / f"{stem}.tex"
    pdf_path = tmp_path / f"{stem}.pdf"
    tex_path.write_text("tex", encoding="utf-8")
    pdf_path.write_bytes(b"%PDF")

    clean_auxiliary_files(tmp_path, stem)

    for extension in auxiliary_extensions:
        assert not (tmp_path / f"{stem}{extension}").exists()

    assert tex_path.exists()
    assert pdf_path.exists()
