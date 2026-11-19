---
title: "Interlude 8: code proof"
fontsize: 10pt
geometry:
  - paperwidth=6in
  - paperheight=9in
  - margin=0.7in
header-includes:
  - \DefineVerbatimEnvironment{Highlighting}{Verbatim}{commandchars=\\\{\},fontsize=\footnotesize}
---

Black-and-white conversion specimen. The language tag is metadata, not a printed heading. Indentation carries meaning independently of syntax color.

### Example 1

```python
import torch

w = torch.tensor(0.5, requires_grad=True)   # a weight to learn
b = torch.tensor(0.0, requires_grad=True)   # a bias to learn
x, target = torch.tensor(2.0), torch.tensor(3.0)

for step in range(50):
    y = w * x + b               # forward: record operations
    loss = (y - target) ** 2    # how wrong, squared
    loss.backward()             # backward: replay the record
    with torch.no_grad():       # update without recording
        w -= 0.05 * w.grad
        b -= 0.05 * b.grad
        w.grad.zero_()
        b.grad.zero_()
```

### Example 2

```python
optimizer = torch.optim.AdamW(model.parameters(), lr=3e-4)
for x, target in loader:              # Interlude 4's data loader
    loss = loss_fn(model(x), target)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
```

### Example 3

```python
from transformers import pipeline
classify = pipeline("sentiment-analysis")
classify("Miracles do happen. We won... and Sam is batting 1.000.")
```
