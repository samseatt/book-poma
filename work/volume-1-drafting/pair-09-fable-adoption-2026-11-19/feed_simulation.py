"""Reproducible illustrative model for Interlude 9; not fitted to a platform.
Python standard library only. Seed, priors, update ordering and all parameters
are explicit. Habit is an ASSUMPTION; its emergence is not an empirical finding.
"""
import random, json, csv, statistics
from pathlib import Path
BASE=[.20-i*.01 for i in range(8)]
RUNS=400; STEPS=5000; SEED=20261119
DECAY=.0005; REINFORCEMENT=.01; CEILING=.6

def experiment(epsilon, habit, seed=SEED, runs=RUNS):
    winners=[]; finalshares=[]; starts=[]; finishes=[]
    curves=[[0.0,0.0] for _ in range(101)]
    for run in range(runs):
        rng=random.Random(seed+run)
        probabilities=BASE.copy(); successes=[1]*8; trials=[5]*8
        history=[]; snapshots=[probabilities.copy()]
        for t in range(STEPS):
            estimates=[a/b for a,b in zip(successes,trials)]
            best=max(estimates); ties=[j for j,x in enumerate(estimates) if x==best]
            # Draw even when epsilon=0 so the same initial random stream is used.
            explore=rng.random()<epsilon
            topic=rng.randrange(8) if explore else rng.choice(ties)
            click=rng.random()<probabilities[topic]
            successes[topic]+=int(click);trials[topic]+=1;history.append(topic)
            if habit:
                if click:probabilities[topic]+=REINFORCEMENT*(CEILING-probabilities[topic])
                probabilities=[p+DECAY*(b-p) for p,b in zip(probabilities,BASE)]
            if (t+1)%50==0:snapshots.append(probabilities.copy())
        counts=[history[-1000:].count(j) for j in range(8)]
        winner=max(range(8),key=lambda j:counts[j]);winners.append(winner)
        finalshares.append(counts[winner]/1000)
        starts.append(BASE[winner]);finishes.append(probabilities[winner])
        for t,ps in enumerate(snapshots):
            curves[t][0]+=ps[winner]/runs
            curves[t][1]+=(sum(ps)-ps[winner])/7/runs
    return dict(epsilon=epsilon,habit=habit,runs=runs,seed=seed,
                selects_original_favorite=sum(x==0 for x in winners)/runs,
                median_final_topic_share=statistics.median(finalshares),
                original_favorite_se=(sum(x==0 for x in winners)/runs*(1-sum(x==0 for x in winners)/runs)/runs)**.5,
                winner_initial_probability=statistics.mean(starts),
                winner_final_probability=statistics.mean(finishes),
                winner_counts=[winners.count(j) for j in range(8)],
                curve=curves)

if __name__=='__main__':
    out=Path(__file__).parent
    results=[experiment(e,h) for h in [False,True] for e in [0,.1]]
    report={'parameters':{'base':BASE,'runs':RUNS,'steps':STEPS,'seed':SEED,'decay':DECAY,'reinforcement':REINFORCEMENT,'ceiling':CEILING,'initial_successes':1,'initial_trials':5,'winner_definition':'Most shown topic in final 1000 rounds; ties resolved by lowest index. Curves average retrospectively selected winners across runs.'},'results':results}
    (out/'feed-results.json').write_text(json.dumps(report,indent=2)+'\n')
    with (out/'feed-curves.csv').open('w') as f:
        w=csv.writer(f,lineterminator='\n');w.writerow(['round','selected_topic','other_seven'])
        for t,(a,b) in enumerate(results[2]['curve']):w.writerow([50*t,a,b])
    for r in results:print({k:v for k,v in r.items() if k!='curve'})
