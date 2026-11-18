# Figure data

`exchange_simulation.c` produces `exchange-simulation.json` using deterministic xorshift64* streams (17112026 and 17112027). Compile with `cc -O3 exchange_simulation.c -o /tmp/poma-exchange`, then run `/tmp/poma-exchange > /tmp/exchange-simulation.json`. This is an illustration, not fitted empirical data. A participation counts one trader in a two-trader exchange. The fixed-unit model cancels unaffordable transfers; the yard-sale model transfers 10% of the poorer holding. Both conserve money and forbid borrowing.

The SVG preserves the incoming two-panel layout. Panel A uses the first 25 bins of width 20; its unplotted tail above 500 holds 0.8% of traders. Panel B uses the saved top-one-percent series, with x = 600 + 350 × participations/6000 and y = 450 − 620 × share. Code/data make the new curve traceable; no claim is made that it exactly reproduces an undocumented incoming seed.

The other checks, including the six-page PageRank stationary distribution and Gordon formula, are in figure-and-arithmetic-checks.json. Existing incoming assets remain untouched in the Fable directory; their hashes are in provenance.json.
