# Spatial Omics, Worked Through

Tutorials for people who have the data and are about to trust it

**Who lands here.** Wet-lab scientists with a first Xenium or Visium run, computational biologists arriving from scRNA-seq, and students who need a working analysis rather than a survey.

**What every lesson promises.** Every lesson answers one decision you actually face, runs on data small enough to download now, and ends by showing you the wrong answer it can produce without ever throwing an error.

**Where the boundary sits.** The site covers the experimental decisions that determine what your data can support — allocation and blocking, what each bench step leaves behind in the matrix, what a targeted panel can and cannot see. It does not cover bench execution: buffers, incubation times and instrument settings belong to the vendor protocol and change between chemistry versions faster than a tutorial can honestly track. Also out of scope: platform selection advice, and benchmarking methods against each other.

## What a reader can do afterward

- **Name the regime** — State what a platform physically measures and at what resolution, and name the claims its data cannot support.
- **Verify alignment** — Confirm that points, images and tables share a coordinate system before believing any tissue map.
- **Interrogate segmentation** — Inspect masks over the image and recognise the signatures of over- and under-segmentation in downstream results.
- **Choose a valid null** — Apply a test or permutation null that respects spatial autocorrelation, instead of one that assumes independent samples.
- **Spot a silent failure** — Recognise output that is plausible, non-crashing and wrong, and know which figure would expose it.
- **Run it again** — Reproduce an analysis from a pinned environment, with runtime and peak memory known in advance.

## Data strategy

The data does not fit. That constraint was decided first and everything else follows from it.

| Tier | Size | Where it lives | What it teaches |
| --- | --- | --- | --- |
| Committed toy | under 10 MB | in the repository | Mechanics: the object model, the API, the plot call |
| Fetched public | 0.1 to 10 GB | fetch script pinned to an accession, cached locally | The real analysis on real tissue, at real scale |
| Simulated | tiny | generator script in the repository | Ground truth — the only tier where the right answer is known |

Primary data is never committed. Fetch scripts are pinned to an accession and record a
checksum; licence and provenance live in `data/SOURCES.md`. No patient data, and nothing
re-identifiable from tissue morphology.

## Resources

`resources.qmd` catalogues public learning material, tool ecosystems and benchmarks, with
an explicit inclusion rule and a checked-on date per entry. Entries listed without a link
are ones we know by name but have not opened — recorded so the search is not repeated, and
deliberately unlinked until verified.

## Reader paths

Nobody starts at lesson one.

- **I am planning an experiment** (About to generate data; nothing has been cut yet): L01 → L02 → L03 → L05 → L08
- **I just got my first run back** (Wet-lab scientist with data and no prior single-cell analysis): L02 → L04 → L05 → L06 → L07 → L09 → L16
- **I do single-cell analysis and want to learn spatial** (Computational biologist fluent in scanpy or Seurat): L05 → L06 → L02 → L07 → L09 → L10 → L11 → L12 → L13 → L14 → L15 → L17
- **I am reviewing someone else's spatial paper** (Referee or reader checking a published claim): L02 → L04 → L07 → L08 → L12 → L13 → L14
- **I am building a method** (Developer who needs the object model and the scale limits): L06 → L11 → L12 → L15 → L17
- **I have one afternoon** (Anyone about to trust a result and short of time): L06 → L07 → L12

## Building

Python dependencies are managed with [uv](https://docs.astral.sh/uv/). `uv.lock` is
committed and pins exact versions and hashes across platforms — it is the reason this
tutorial will still run next year.

```bash
uv sync --all-groups                    # creates .venv from the lock file
QUARTO_PYTHON=.venv/bin/python quarto preview
```

To add a dependency, `uv add <package>` and commit the changed lock file. To refresh
everything deliberately, `uv lock --upgrade`, then re-run the `reexecute` workflow before
trusting the cache.

`quarto render` publishes from cached output. CI never re-runs the heavy analysis; the
`reexecute` workflow does that on demand and must be run manually before any release.

### Things uv does not manage

- **R**, used by the Rosetta panel in each lesson. Handled separately with `renv`; see
  `rosetta/README.md`.
- **Non-Python binaries.** Any segmentation tool that ships as a standalone program is
  installed outside the lock file, and the lesson that uses it says so.

## Contributing

Every lesson fills all seven slots. See `CONTRIBUTING.md` — a missing slot is a defect,
not a style choice.
