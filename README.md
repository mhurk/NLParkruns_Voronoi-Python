![GitHub Created At](https://img.shields.io/github/created-at/mhurk/NLParkruns_Voronoi-Python)
![GitHub repo file or directory count](https://img.shields.io/github/directory-file-count/mhurk/NLParkruns_Voronoi-Python)
![GitHub repo size](https://img.shields.io/github/repo-size/mhurk/NLParkruns_Voronoi-Python)
![GitHub language count](https://img.shields.io/github/languages/count/mhurk/NLParkruns_Voronoi-Python)
![GitHub last commit](https://img.shields.io/github/last-commit/mhurk/NLParkruns_Voronoi-Python)

# Voronoi diagram of parkruns in The Netherlands - Python version
Early 2024 I wrote a voronoi plot, in R, of the parkruns in The Netherlands. On the [parkrun statsgeek facebook group](https://www.facebook.com/groups/1733916136845554) some discussion arose about the correctness of this graph. At that time I could not find the root cause. I expected a projection issue but did not (yet) fix it. This is the updated code (with more parkruns added) and also rewritten in Python.

A voronoi plot or diagram is helpful to visualise the nearest parkrun in The Netherlands.

It uses the parkruns as mentioned on the website of Roderick Hoffman and uses only the ones which are located in The Netherlands.
Country border and the borders of the provices are available via the [GADM](https://gadm.org/download_country.html) project. A version with the used resultion is also copied in the data directory.

The plots look like this for Netherlands with the currently (January 2024) known parkruns : <br>
![NL](/images/parkruns.png)

This is the version without country border because some questions in a prakrunn statistics forum arose whether the lines are correctly positioned:<br>
![plot without border](/images/noborder.png)


