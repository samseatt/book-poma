# Reproducing the illustrative feed

Run `python3 feed_simulation.py` in this directory. Python's standard library is sufficient. The script writes `feed-results.json` and `feed-curves.csv` beside itself; it prints four compact result records. `update_feed_figure.py` redraws only the two curves in an explicitly supplied copy of `feed-loop.svg` from those results.

## What was reproduced

This is an independently specified replacement implementation for the manuscript's unsupported calculation, not recovery of missing Fable code or an author-conducted historical experiment. All parameters are recorded in the script and output. The seed is 20261119 plus the run index; each condition uses 400 runs of 5,000 rounds, eight topics with initial click probabilities .20 through .13, and estimates initialized at one click in five trials. Ties in the recommender's estimate are random. Exploration chooses a topic uniformly with probability .1; the greedy condition has probability zero. Reusing initial seeds does not make this a rigorously paired common-random-number experiment: policies subsequently consume different draws.

In the habit condition only, a click increases its topic's probability by .01 of the remaining distance to .60. Every round all probabilities relax .0005 toward their baselines, after the reinforcement update. The final leading topic is the one shown most in the last 1,000 rounds, with lowest-index tie-breaking. The plot selects that eventual winner retrospectively in each run and averages its whole trajectory; it is not a trajectory of a single fixed topic or person. The dashed line averages the other seven.

| Condition | Leading topic was original favorite | Monte Carlo standard error |
|---|---:|---:|
| Greedy, fixed tastes | 26.5% | 2.21 percentage points |
| 10% exploration, fixed tastes | 53.0% | 2.50 points |
| Greedy, reinforcement assumed | 21.5% | 2.05 points |
| 10% exploration, reinforcement assumed | 22.5% | 2.09 points |

The greedy/habit winner's mean probability rises from .173525 to .565369. These numbers are finite-run outputs for this model, not universal constants. The small difference between the last two rows is not presented as meaningful evidence for one policy over the other.

## What the model can and cannot establish

The fixed-taste control isolates the exploration problem. The reinforcement conditions demonstrate that a recommendation policy can change the target it is learning **if the specified preference dynamics hold**. Reinforcement was inserted, not discovered. More exposure is not automatically more liking; clicks are neither welfare nor a complete measure of preference. Priors, topic spacing, horizon, update rate and decay all matter. This is not a fitted model of a named platform and is not empirical evidence about people.

The chart is about a feedback mechanism, not a claim that the recommender learned the hidden baseline incorrectly under every possible objective. A system maximizing present clicks may be succeeding at that objective while answering a different question from discovering a prior preference. The scientific questions are whether, when and how such dynamics occur, and what should count as a good outcome.

## Checks

The final script was run again after its last correction. The fixed-taste curves stay constant; every simulated probability stays within its initial value and the chosen ceiling; winner counts total 400; all 101 curve samples are finite; and the displayed percentages and endpoints match the report. The SVG's two numerical paths are matched against the report. Re-rendering the SVG is a separate visual check, already completed for this adoption.
