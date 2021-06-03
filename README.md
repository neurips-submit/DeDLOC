# DeDLOC

This is a supplementary code for an anonymous paper submission for NeurIPS'21. The code is divided into several sections, matching the corresponding evaluations in the original paper.

- [`src`](./src) contains the common DeDLOC code that is required by all other sections
- [`albert`](./albert) is the supplementary code for controlled experiments with ALBERT-large on Wikitext103
- [`swav`](./swav) is for training SwAV on ILSVRC data, similarly in similar conditions.
- [`sahajbert`](./sahajbert) contains the code used to conduct public collaborative experiment for Bengali language.
- [`p2p`](./p2p) is a step-by-step tutorial that explains decentralized NAT traversal and circuit relays


### Installation
Before running any experiments, one must install the library from `src` section as such:

- Prepare an environment with python __3.7-3.9__
   - [Anaconda](https://www.anaconda.com/products/individual) is recommended, but not required
- Ensure that your machine has a recent version of Golang (1.15 or higher)
   - To install Go, follow the [instructions](https://golang.org/doc/install) on the official website.
- Install the library: __`cd ./src && python setup.py install`__

For all distributed experiments, the installation procedure must be repeated on every machine that participates in the experiment. We recommend using machines with at least 2 CPU cores, 16GB RAM and, when applicable, a low/mid-tier NVIDIA GPU.

We recommend running [`albert`](./albert) experiments first: other experiments build on top of that starter and may reqire more careful setup (e.g. for public participation). Furthermore, for this experiment, we provide [a script](./albert/AWS%20runner.ipynb) for launching experiments using cloud preemptible GPUs.
