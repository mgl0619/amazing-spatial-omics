# The R side

`uv` manages Python only. The Rosetta panel in each lesson runs R, so R dependencies are
pinned separately with [renv](https://rstudio.github.io/renv/).

```r
install.packages("renv")
renv::restore()      # from the committed renv.lock
```

`renv.lock` is committed for the same reason `uv.lock` is: a reader who cannot reproduce
the second language has only half a lesson.

## When a lesson has no R equivalent

Say so in the lesson, plainly, rather than dropping the slot. Lesson 12 is the current
example — there is no close R equivalent to the chunked store, and a reader working in R
needs to know that before committing to the approach, not after.

## Packages

Keep this list in step with `renv.lock`.

| Package | Used by |
| --- | --- |
| Seurat | lessons 1, 2, 3, 4, 7, 9, 13 |
| SeuratObject | as above |
| Giotto | lesson 8 |
| spacexr | lesson 5 |
