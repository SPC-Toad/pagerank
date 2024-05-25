# PageRank Using Linear Algebra

## Overview

This project implements the PageRank algorithm using linear algebra in Python3. PageRank is a method for ranking web pages based on their link structures, initially developed by Larry Page and Sergey Brin, the founders of Google. This implementation leverages the power of linear algebra to calculate the rank of each page in a network of web pages.

## Files

- `pagerank.py`: The main implementation of the PageRank algorithm using linear algebra.
- `Makefile`: A makefile to manage the build and execution process of the project.
- `hw10prog.py`: An additional script related to the PageRank implementation (likely a homework or supporting script).

## Requirements

- Python 3.6 or higher
- NumPy library

## Installation

To get started with this project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-name/pagerank.git
    cd pagerank
    ```

2. Ensure you have Python 3 and NumPy installed:
    ```bash
    python3 --version
    pip install numpy
    python3 -m pip install networkx
    python3 -m pip install scikit - learn
    ```

## Usage

### Running the PageRank Algorithm

1. Navigate to the project directory.
2. Unzip test files to explore pagerank:
    ```bash
    make unzip
    ```
3. Run the main script using the following command:
    ```bash
    make fullrun
    ```
4. To clean up any generated files:
    ```bash
    make destroy
    ```

## PageRank Algorithm Explanation

The PageRank algorithm assigns a numerical weighting to each element of a hyperlinked set of documents, such as the World Wide Web(WWW.), with the purpose of measuring its relative importance within the set.

### Steps:

1. **Create the Link Matrix**: Represent the link structure of the web pages using a matrix where element (i, j) is 1 if page i links to page j, and 0 otherwise.
2. **Compute the Transition Matrix**: Normalize the link matrix so that each column sums to 1, representing the probability of moving from one page to another.
3. **Iterate to Convergence**: Start with an initial rank vector and repeatedly multiply it by the transition matrix until convergence is reached (the ranks stabilize).

## Conclusion

This project demonstrates a fundamental implementation of the PageRank algorithm using linear algebra techniques. It provides a foundation for understanding how modern search engines rank web pages and the mathematical principles underlying these algorithms.

## Reference / Helpful Resource

https://en.wikipedia.org/wiki/PageRank
