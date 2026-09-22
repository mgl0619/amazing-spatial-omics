"""Print the installed version of every package the lessons import.

The site states versions on the page, not only in a lock file, because a reader
cannot open your lock file. appendix/environment.qmd calls this.
"""

from importlib.metadata import PackageNotFoundError, version

PACKAGES = [
    "anndata", "scanpy", "squidpy", "spatialdata", "spatialdata-io",
    "spatialdata-plot", "zarr", "dask", "pyarrow", "numpy", "pandas",
    "matplotlib", "colorspacious",
]


def table() -> str:
    rows = ["| Package | Version |", "| --- | --- |"]
    for name in PACKAGES:
        try:
            v = version(name)
        except PackageNotFoundError:
            v = "not installed"
        rows.append(f"| `{name}` | {v} |")
    return "\n".join(rows)


if __name__ == "__main__":
    import sys
    print(f"Python {sys.version.split()[0]}\n")
    print(table())
