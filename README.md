# Cite Your Sources

## Project Description

This project implements Google's PageRank algorithm, a cornerstone of web search, which measures the importance 
of pages by analyzing their hyperlink structure. It offers two distinct methods: random sampling and iterative computation 
for estimating PageRank scores. By leveraging both methods, this project provides a comprehensive solution for analyzing and 
ranking web pages within a given corpus by their probability of being visited.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies](#technologies)
- [Credit](#credit)
- [License](#license)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/colindao/cite-your-sources.git
```

2. Navigate to the project directory:

```bash
cd cite-your-sources
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To analyze a corpus' pages, run the following command:

```bash
python pagerank.py [corpus]
```

Adjust the sampling size and damping factor to tinker with how many random iterations you'd like to execute and the likelihood of choosing a link on that page.

## Features


**Random Sampling**: The random sampling method begins by selecting a page randomly from the corpus. Utilizing a transition model and Markov Chain, 
the current page's state transitions to a random link within that page. The visits per page are recorded and accumulate throughout the total sample iterations, 
providing a model of the probability distribution as if a random internet surfer were navigating the web.<br />
<br />
**Iterative Sampling**: In the iterative sampling approach, PageRank values are computed based on previous iterations. 
Initially, each page is assigned an equal probability score—that is choosing one randomly. Then, using a recursive mathematical expression derived from the PageRank algorithm, 
the probability score for each page is updated based on the PageRank values of its parent pages. This process continues iteratively until the 
PageRank values converge to stable values which deviate by less than 0.1%. By refining the PageRank values with each iteration, the iterative sampling method provides an accurate 
estimation of the importance of each page within the corpus.

## Technologies

**Language**: Python <br />
**Libraries**: OS, Random, RE, Sys

## Credit

This project was completed as a part of [CS50's Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/2024/). Go check them out!

## License

MIT License

Copyright (c) 2024 Colin Dao

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
