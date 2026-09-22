# Writing a lesson

## Rule zero: the decision comes first

If you cannot write, in one sentence, the decision this lesson helps someone make, the
lesson does not exist yet. Not "understand neighbourhood enrichment" — that is a topic.
"You are about to write that macrophages and tumour cells interact; decide whether that
survives a different radius" is a decision. It has a person in it, and a problem.

If that sentence will not come, the scope is wrong: either you are teaching a technique
nobody has to choose about, or you have bundled three lessons together.

## The seven slots

Every lesson has all seven, in this order.

1. **The decision it serves** — one sentence, concrete, with a person in it.
2. **Concept** — 800 to 1,200 words. One figure that carries an idea, not decoration.
   State what quantity is measured and in what units, early. Name the assumption that
   breaks first.
3. **Runnable notebook** — real code, executed, on data whose truth is known.
4. **Rosetta panel** — the same computation in R. Readers arrive from different tools.
   If there is no equivalent, say so plainly rather than omitting the slot.

   Write it as a plain ```` ```r ```` block, not ```` ```{r} ````. Quarto cannot execute
   Python and R in one document — a file with an executable R chunk becomes a knitr
   document and needs Rscript even under `--no-execute`. The panel is reference code, so
   static is correct. If a panel ever needs to actually run, it belongs in a companion
   `.qmd` rendered by knitr, included as a child document.
5. **Failure mode** — something broken on purpose, plus the diagnostic that catches it.
   This is the slot most often skipped and the one readers remember.
6. **Self-check** — three questions, answers folded. Test judgement, not recall.
7. **Going further** — what to read next, and what this lesson deliberately omitted.

## Sources

**Never write a citation from memory.** Verify each one against PubMed in the session you
write it: title, journal, year, volume, pages, DOI. Record what you actually read — an
annotation from an abstract is not an annotation from the paper, so say which.

Check the licence before planning to reuse a figure. Most literature is all rights
reserved, and "free to read" is permission to read, not to copy. **Link, never host.**
Redraw figures from the equations or the underlying data.

Record negative results. "No public dataset of this tissue on this platform was found"
is a finding, and it stops the next person repeating the search.

## Notebooks

- It must execute. Run it and read the output; an exit code is not a check. Look at
  every figure — a chart that runs is not a chart that reads.
- Prefer simulated data with recorded true parameters, so the reader can measure how far
  their estimate landed from the answer. This is the strongest pedagogical move available
  and the tier most often skipped.
- Assert on the things that matter: recovered values within tolerance, identities that
  must hold, units that must cancel.
- **Sabotage the code each assert guards and confirm the assert fails.** An assert that
  cannot fail is not a test. `all(x > 0 for x in [])` is vacuously true.
- Commit the freeze cache. Frozen output that exists only on your machine looks fine
  locally and breaks every other build.
- State runtime and peak memory in the front matter. "This cell needs 32 GB" is
  information a reader needs before running it.

## Failure modes that work here

Pick one that is plausible and silent — it produces a plausible number, not an error.

- Segmentation error inherited by every downstream cell-level result
- A flipped axis or a mismatched coordinate system
- A spot-level claim written as a cell-level claim
- A test that assumes independent samples applied across spatial neighbours
- Negative and blank probes discarded at load, taking the noise floor with them
- A cell state absent from the reference, assigned confidently to its nearest neighbour
- Integration that removes the anatomy along with the batch

## Plotting

- More than about eight categorical colours is unreadable. Facet, group into lineages,
  or highlight one type against grey.
- Never a rainbow for a continuous quantity. One hue, light to dark.
- Validate palettes for colour-vision deficiency by computing it, not eyeballing it.
- Equal aspect ratio and a scale bar in microns.
- Show the image under the points at least once per lesson. It is the fastest check that
  the coordinates are right.

## Environment

Python dependencies go through `uv add`, never a bare `pip install` into the venv — an
install that is not in `uv.lock` exists only on your machine. Commit the changed lock file
in the same PR as the code that needs it, and run `uv lock --check` before pushing; CI
fails on a stale lock.

R packages go through `renv::snapshot()` into `renv.lock`. Anything that is neither a
Python package nor an R package — a standalone segmentation binary, say — is outside both
locks, so the lesson that uses it must state the version it was run against.

## Before you open the PR

- [ ] The decision sentence exists and names a person with a problem
- [ ] All seven slots present
- [ ] Every citation verified this session, DOI checked, not recalled
- [ ] Notebook executed; output read, every figure looked at
- [ ] Each assert sabotage-tested and confirmed to fail
- [ ] Rosetta panel runs, or its absence is stated plainly
- [ ] Freeze cache committed, not just generated
- [ ] `uv lock --check` passes; lock file committed alongside the change
- [ ] Runtime and peak memory in the front matter
- [ ] Resolution regime stated: spot, bin, or cell
- [ ] Any statistical test accounts for spatial dependence, or says why not
- [ ] Failure mode is silent and plausible, not an obvious error
- [ ] Points overlaid on the image at least once
- [ ] No copyrighted figure reproduced; no patient data
- [ ] Cross-references and counts updated wherever they appear
