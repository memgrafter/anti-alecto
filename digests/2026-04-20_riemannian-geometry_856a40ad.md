---
url: https://en.wikipedia.org/wiki/Riemannian_geometry
title: Riemannian geometry
scraped_at: '2026-04-20T01:21:22Z'
word_count: 1759
raw_file: raw/2026-04-20_riemannian-geometry_856a40ad.txt
tldr: Riemannian geometry is the study of smooth manifolds equipped with a smoothly varying inner product on tangent spaces, and this page surveys its intrinsic viewpoint, its foundational role in modern geometry/relativity, and a grab bag of classical theorems linking curvature to topology.
key_quote: the essential ingredient here was this quadratic form on tangent vectors, and that it could be generalized.
durability: high
content_type: mixed
density: high
originality: synthesis
reference_style: refer-back
scrape_quality: good
people:
- Bernhard Riemann
- Einstein
- Jeff Cheeger
- D. Ebin
- G. Perelman
- Marcel Berger
- Sylvestre Gallot
- Dominique Hulin
- Jacques Lafontaine
- Jürgen Jost
- Peter Petersen
- Lizhen Ji
- Athanase Papadopoulos
- Sumio Yamada
- Simon Brendle
- Richard M. Schoen
tools: []
libraries: []
companies: []
tags:
- differential-geometry
- riemannian-geometry
- curvature
- topology
- general-relativity
---

### TL;DR
Riemannian geometry is the study of smooth manifolds equipped with a smoothly varying inner product on tangent spaces, and this page surveys its intrinsic viewpoint, its foundational role in modern geometry/relativity, and a grab bag of classical theorems linking curvature to topology.

### Key Quote
"the essential ingredient here was this quadratic form on tangent vectors, and that it could be generalized."

### Summary
- **What it is**
  - Riemannian geometry studies **Riemannian manifolds**: smooth manifolds with a **Riemannian metric**.
  - A Riemannian metric is an **inner product on each tangent space** that varies smoothly from point to point.
  - This gives local notions of:
    - angle
    - curve length
    - surface area
    - volume
  - Global quantities are then obtained by integrating these local measurements.

- **Core idea / historical framing**
  - The field originates with **Bernhard Riemann** and his inaugural lecture *Über die Hypothesen, welche der Geometrie zu Grunde liegen*.
  - The emphasis is **intrinsic geometry**: what matters is not how a surface sits in ambient space, but how distances are measured on the manifold itself.
  - The page uses examples like:
    - a **cylinder vs. a flat sheet of paper**: intrinsic distances can be unchanged by bending
    - the **helicoid and catenoid**: different embeddings, same intrinsic geometry after cutting along a generator

- **Generalization and scope**
  - Riemannian geometry generalizes the differential geometry of surfaces in \(\mathbb{R}^3\) to higher-dimensional manifolds.
  - A modern result cited here: **every smooth manifold admits a Riemannian metric**.
  - The metric can be described in local coordinate patches, with transformation rules governed by the chain rule.

- **Relation to other geometries / physics**
  - If the positive-definite condition is relaxed, one gets **pseudo-Riemannian manifolds**.
  - These are the main geometric objects in **general relativity**.
  - Replacing the quadratic form by a more general non-quadratic function leads to **Finsler geometry**.
  - The text also notes analogies with **crystal defects**, where dislocations and disclinations correspond to torsion and curvature.

- **Introductory related topics**
  - The page points readers to:
    - Metric tensor
    - Riemannian manifold
    - Levi-Civita connection
    - Curvature
    - Riemann curvature tensor
    - List of differential geometry topics
    - Glossary of Riemannian and metric geometry

- **Classical theorems highlighted**
  - The page gives an intentionally incomplete list of major theorems for readers who already know the basics.
  - **General theorems**
    - **Gauss–Bonnet theorem**: integral of Gauss curvature on a compact 2D manifold equals \(2\pi \chi(M)\); generalized to even dimensions.
    - **Nash embedding theorems**: every Riemannian manifold can be isometrically embedded in some Euclidean space \(\mathbb{R}^n\).

  - **Geometry in large**: local curvature assumptions imply global/topological conclusions.

  - **Pinched sectional curvature**
    - **Sphere theorem**: simply connected compact \(n\)-manifold with sectional curvature pinched between \(1/4\) and \(1\) is diffeomorphic to a sphere.
    - **Cheeger finiteness theorem**: with bounds on curvature, diameter, and volume, only finitely many diffeomorphism types occur.
    - **Gromov’s almost flat manifolds**: sufficiently small sectional curvature and bounded diameter imply a finite cover diffeomorphic to a nil manifold.

  - **Sectional curvature bounded below**
    - **Cheeger–Gromoll soul theorem**: complete noncompact nonnegatively curved manifold is diffeomorphic to the normal bundle of a compact totally geodesic soul.
    - In particular, strictly positive curvature everywhere implies diffeomorphic to \(\mathbb{R}^n\).
    - **Perelman’s 1994 result**: positive curvature at just one point already implies \(\mathbb{R}^n\) under the Soul Conjecture setting.
    - **Gromov’s Betti number theorem**: positive sectional curvature bounds the sum of Betti numbers.
    - **Grove–Petersen finiteness theorem**: bounds on curvature, diameter, and volume imply finitely many homotopy types.

  - **Sectional curvature bounded above**
    - **Cartan–Hadamard theorem**: complete simply connected nonpositively curved manifold is diffeomorphic to \(\mathbb{R}^n\); geodesics between any two points are unique.
    - Negative sectional curvature yields **ergodic geodesic flow** on compact manifolds.
    - Strictly negative upper curvature bound implies the space is **CAT(k)** and its fundamental group is **Gromov hyperbolic**, with consequences like finite presentation and restricted subgroup structure.

  - **Ricci curvature bounded below**
    - **Myers theorem**: positive Ricci curvature implies finite fundamental group.
    - **Bochner’s formula** consequence: nonnegative Ricci curvature bounds the first Betti number by \(n\); equality characterizes flat tori.
    - **Splitting theorem**: a complete manifold with nonnegative Ricci curvature containing a line splits as \(\mathbb{R} \times N\).
    - **Bishop–Gromov inequality**: volume growth of balls is bounded above by Euclidean volume under positive Ricci curvature.
    - **Gromov compactness theorem**: positive Ricci curvature plus diameter bound gives precompactness in Gromov–Hausdorff metric.

  - **Negative Ricci curvature**
    - Isometry group of a compact manifold with negative Ricci curvature is discrete.
    - Every smooth manifold of dimension at least 3 admits a metric with negative Ricci curvature; the text notes this fails for surfaces.

  - **Positive scalar curvature**
    - The \(n\)-torus does not admit a metric with positive scalar curvature.
    - If injectivity radius is at least \(\pi\), average scalar curvature is at most \(n(n-1)\).

- **References / further reading**
  - The page lists standard books by:
    - Berger
    - Cheeger & Ebin
    - Gallot, Hulin, Lafontaine
    - Jost
    - Petersen
    - Ji, Papadopoulos, Yamada (edited volume)
  - Also cites a paper by **Brendle and Schoen** on weakly \(1/4\)-pinched curvature.

### Assessment
This is a high-durability, reference-style encyclopedia entry with mixed content: mainly factual and conceptual overview, plus a catalog of major theorems. It is dense with named results, curvature conditions, and consequences, making it useful for recall and quick lookup rather than deep study of proofs. The content is largely a synthesis of established material rather than primary research, though it includes one modern theorem statement (every smooth manifold admits a Riemannian metric) and cites classical literature. Scrape quality looks good overall: the main text, theorem list, references, and external links are present, though the “Notes” section is empty and the page omits images and any theorem proofs or full context.
