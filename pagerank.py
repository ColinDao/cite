import os
import random
import re
import sys

# Chance of choosing a random link from a given page
DAMPING = 0.85

# Amount of iterations
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )
    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    c = len(corpus)
    links = corpus[page]

    # Initial, random chance of choosing one of the links on the given page
    probabilities = {link: 1 / len(links) * damping_factor for link in links}

    # If page has no links, randomly choose one from the entire corpus
    if not probabilities:
        return {key: 1 / c for key in corpus}
    
    # Add the probability 0 for the links that are not in the page
    for link in corpus:
        if link not in probabilities:
            probabilities[link] = 0

    # Add the probability of 1 - damping factor in which a random link from the
    # entire corpus is chosen
    random_chance = 1 - damping_factor
    for page in probabilities:
        probabilities[page] += random_chance / c

    # Return the probability distribution of choosing a link given the page
    return probabilities


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    # Count the times each page has been visited
    counter = {key: 0 for key in corpus}

    # Randomly choose a page
    page = random.choice(list(corpus))

    # n samples to estimate PageRank value
    for _ in range(n):

        # Get links from current page
        links = transition_model(corpus, page, damping_factor)

        # Generate a random probability in which user ends up on a given link
        rand = random.random()
        sum = 0
        for link in links:
            sum += links[link]

            # If the current probability sum is greater than the random probability
            # generated, then the 'random visited page' has been found. Increase
            # the visit counter for this link and set is as the new page
            if sum > rand:
                counter[link] += 1
                page = link
                break

    # Return the probability of visiting each link from the sampling
    return {page: counter[page] / n for page in corpus}


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    c = len(corpus)
    
    # Equally likely to end up on any page at the start
    pagerank = {page: 1 / c for page in corpus}

    # Page and its links or all of the links if there are none on the page
    links_to = {page: corpus[page] if len(corpus[page]) > 0 else list(corpus) for page in corpus}

    # Page and all the pages that link to it
    links_from = {
        current_page: [parent_page for parent_page in corpus if current_page in links_to[parent_page]] 
        for current_page in corpus
    }

    # Iterate until converge to probabilities that are less than 0.001 from the previous
    while True:

        # Keep track of how many links have successfully converged
        deviations = 0

        # Probability of randomly choosing a link in the corpus
        random_chance = 1 - damping_factor
        pagerank_new = {page: random_chance / c for page in corpus}

        # Get new PageRank values
        for current_page in links_from:

            # Every page that links to the current page
            for parent_page in links_from[current_page]:

                # Add the probability in which the user ends up on the parent page divided by
                # the number of links on the parent page and multiplied by the probability that the
                # current page is chosen
                pagerank_new[current_page] += damping_factor * pagerank[parent_page] / len(links_to[parent_page])

            # Page successfully converged
            if abs(pagerank_new[current_page] - pagerank[current_page]) < 0.001:
                deviations += 1

        # Every page has successfully converged        
        if deviations == c:
            return pagerank
        
        # Assign new pagerank values
        pagerank = {page: pagerank_new[page] for page in pagerank_new}


if __name__ == "__main__":
    main()
