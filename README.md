# Spatial omics: what to read, and who it is for

A filtered list of public material for learning spatial omics data analysis. Not an index —
several of those already exist and are maintained by people closer to the tools. This adds
the two things they omit: **who each resource assumes you are**, and **whether anyone has
opened it**.

Last reviewed **2026-09-01**

## What gets listed

- **It teaches, or it is a primary reference.** Marketing pages do not qualify.
- **Its audience is stateable.** If the level cannot be described, the entry is not actionable.
- **It is reachable** without a login, licence or institutional subscription.
- **It was opened on the date shown**, or it is marked as unopened.

Entries with a link were opened and confirmed on the date shown. Entries in `monospace`
without a link are known by name from index repositories but have **not been opened here** —
recorded so the search is not repeated, and left unlinked until checked.

**Link, never host.** Everything points at the original. Nothing is mirrored or copied.

## Curated lists — start with one of these

| Resource | What it is | Checked |
| --- | --- | --- |
| [crazyhottommy/awesome_spatial_omics](https://github.com/crazyhottommy/awesome_spatial_omics) | Tools **and review papers**. Strongest entry point if you want the literature rather than the software. | 2026-09-01 |
| [p-gueguen/Spatial_transcriptomics_tools](https://github.com/p-gueguen/Spatial_transcriptomics_tools) | Best organised of the three. Tags every entry by language and interface, including GUI tools. | 2026-09-01 |
| [drieslab/awesome-spatial-data-analysis](https://github.com/drieslab/awesome-spatial-data-analysis) | Tools and methods, maintained by the Giotto authors. | 2026-09-01 |
| [SindiLab/Deep-Learning-in-Spatial-Transcriptomics-Analysis](https://github.com/SindiLab/Deep-Learning-in-Spatial-Transcriptomics-Analysis) | ML methods by analysis stage, with language and year. | 2026-09-01 |
| [training-collection](https://github.com/FrederickMappin/training-collection) | Bioinformatics training materials across domains, with a spatial section. | 2026-09-01 |

## Reference texts

| Resource | For whom | Notes | Checked |
| --- | --- | --- | --- |
| `lmweber/OSTA` | R | Orchestrating Spatial Transcriptomics Analysis with Bioconductor. Nearest thing to a standard text; listed in two independent indexes. Not opened here. | unopened |
| `Best practices Bioconductor` | R | Principles for statistical analysis of spatial data. Not opened here. | unopened |

This section is thin. A maintained Python-side best-practices text would belong here.

## Courses and workshop material

Workshop repositories are the most useful free teaching material in this field: written to be
taught from, so they assume less than documentation and explain more than a paper. They are
snapshots — a 2022 workshop teaches a 2022 API.

| Resource | Language | For whom | Checked |
| --- | --- | --- | --- |
| [Introductory Spatial 'Omics Analysis 2024](https://bioinformaticsdotca.github.io/ISO_2024/) | R / Python | Canadian Bioinformatics Workshop. Complete tutorials, slides and exercises, CC-BY 4.0. Most complete single course found. | 2026-09-01 |
| [Giotto Suite Workshop 2024](https://giotto-suite.github.io/giotto_workshop_2024/) | R | Two-day workshop as a book: technologies, preprocessing, clustering, deconvolution, spatial patterns. [Source](https://github.com/drieslab/giotto_workshop_2024). | 2026-09-01 |
| [fhausmann/workshop_spatial](https://github.com/fhausmann/workshop_spatial) | Python | Beginner's course on Visium. Start here with no prior single-cell experience. | 2026-09-01 |
| [theislab/spatial_scog_workshop_2022](https://github.com/theislab/spatial_scog_workshop_2022) | Python | SCOG notebooks with per-session environments, from the group behind much of scverse spatial. Older API. | 2026-09-01 |
| [ashoks773/SpatialTranscriptomicsWorkflow](https://github.com/ashoks773/SpatialTranscriptomicsWorkflow) | Python | End-to-end walkthrough on public HCC data, download through annotation. | 2026-09-01 |
| [ISB Practical Methods 2024](https://github.com/Shuozhen/2024_ISB_workshop_Practical_Methods_in_Spatial-Omics) | Python | Spatial multi-omics including RNA+ATAC; spatial folder generation for custom chips. | 2026-09-01 |
| `mahfouzlab/MGC-BioSB-Spatial-Omics-Analysis-2025` | Python | 2025 workshop materials, most recent found. Not opened here. | unopened |
| `spatial-omics-tutorials` (BIML 2025) | Python / R | Tutorials and best practices from BIML 2025. Not opened here. | unopened |
| `sib-swiss/seq-spatial-transcriptomics-training` | unclear | SIB training, sequencing-based. Not opened here. | unopened |
| `elixir-europe-training/ELIXIR-SCO-spatial-omics` | unclear | ELIXIR Europe training materials. Not opened here. | unopened |
| `DavisLaboratory/GeoMXAnalysisWorkflow` | R | GeoMx-specific workflow; only entry for region-of-interest data. Not opened here. | unopened |

## Tool ecosystems

Choose an ecosystem before choosing a tool. Moving between them mid-project costs more than
either tool saves, and most methods exist in only one.

**Python — scverse.** `squidpy` for spatial statistics and neighbourhood analysis;
`spatialdata` for the object model and coordinate systems; `bento` for subcellular analysis;
`scvi-tools` for the deep-learning family including `DestVI`.

**R.** `Giotto` (also has a Python interface); `Seurat` for spatial objects; `Voyager` on
`SpatialFeatureExperiment` for exploratory spatial data analysis; `spacexr` for RCTD
deconvolution; `nnSVG` for spatially variable genes, notable for being among the
better-calibrated methods; `semla` and `SPATA2` as general toolkits.

**Visualisation.** `Vitessce` for integrated exploration; `rakaia` for in-browser analysis;
`Thor` for cell-level investigation with histology.

**Without code.** `VR-Omics` provides end-to-end processing through a GUI. A substantial part
of the field does not work at a command line, and most tutorials assume otherwise.

Tool URLs live in the curated lists above and are not duplicated here, because duplicating
them guarantees they fall out of date.

## Benchmarks worth reading before choosing a method

| Topic | Finding | DOI |
| --- | --- | --- |
| Imaging platform comparison | FDR differs substantially by platform and by chemistry version within a platform. Xenium lowest FDR in 15 of 22 tissue–cancer combinations. | `10.1038/s41467-025-64990-y` |
| Xenium quality assessment | Detection efficiency 1.2–1.5x Chromium v2. Targeted platforms are not lower quality; denominators differ. | `10.1038/s41592-025-02617-2` |
| Segmentation methods | Cell-type calling accuracy ranged 35–74% across methods on the same simulated tissue. | `10.1038/s42003-024-06480-3` |
| Spatially variable genes | Most methods produce poorly calibrated p-values; select by fixed rank threshold, not significance cutoff. | `10.1186/s13059-025-03731-2` |
| Gene-category enrichment | Over 500-fold inflation of false positives with spatially autocorrelated phenotypes. | `10.1038/s41467-021-22862-1` |
| Experimental design | PoweREST estimates power for Visium; sample size is number of sections, not spots. | `10.1371/journal.pcbi.1013293` |
| FFPE vs fresh frozen | FFPE median RIN 2.5 / DV200 48% against RIN 8.1 / DV200 97%. Do not compare across storage conditions. | `10.1371/journal.pone.0283159` |

Full bibliography with source-quality notes: [`references.bib`](references.bib).

## Contributing an entry

Open an issue with the URL, one sentence on who it is for, and the date you opened it.
Entries without a stated audience are not actionable. Dead links are equally worth reporting —
a resource page that rots is worse than none, because it still looks maintained.

## Also in this repository

`lessons/` holds an unfinished 17-lesson tutorial: six written with verified references,
eleven in draft. Retained for reference; not the focus of this repository.

---

*Eleven entries verified by opening them; six recorded by name and left unlinked pending
review. Benchmark DOIs read from publisher records on 2026-09-01. Nothing is hosted here.*
