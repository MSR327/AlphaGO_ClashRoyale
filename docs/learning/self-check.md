# Phase 0 self-check

This is not a test. It tells us where to start explaining, so nothing is pitched too
low or too high. For each question, mark one:

- **Y**: I could do or explain this now
- **~**: I've seen it but would need to look it up
- **N**: new to me

Don't look anything up first. Answer in a copy of this file
(`docs/learning/self-check-answers.md`) or just paste your marks into the chat.

## A. Python (needed from Phase 1)

1. Write a function that reads a CSV file and returns a list of dicts.
2. Explain what a class, `__init__` and `self` are, and write a small dataclass.
3. Use type hints, and explain why `list[int]` helps when it isn't enforced.
4. Explain a generator (`yield`) and when you'd use one instead of a list.
5. Explain what a virtual environment is and why projects use one.

*Why it matters here:* capture and recording code is plain Python that runs for
minutes at a time and handles a lot of frames.

## B. NumPy and images (needed from Phase 1)

1. Explain the shape of a colour image as an array, e.g. `(H, W, 3)`.
2. Crop a region out of an image array with slicing.
3. Explain broadcasting: why `image - mean` works when `mean` has shape `(3,)`.
4. Compute the average colour of a region without a Python loop.
5. Explain the difference between `uint8` and `float32` pixel values and why it matters.

*Why it matters here:* every frame from the phone is an array, and reading elixir or
the timer starts with cropping and comparing pixels.

## C. PyTorch and deep learning (needed from Phase 2)

1. Explain what a tensor is and how it differs from a NumPy array.
2. Describe a training loop: forward pass, loss, backward pass, optimizer step.
3. Explain overfitting and what a validation set is for.
4. Explain what a convolutional layer does to an image, in words.
5. Explain what an object detector outputs (boxes, classes, confidence).

*Why it matters here:* Phase 2 trains a detector, and Phases 4 and 5 train policies
with the same loop.

## D. Probability and RL ideas (needed from Phase 3)

1. Explain expected value with a dice example.
2. Explain why a win rate from 20 games is less trustworthy than from 200.
3. Explain the words agent, environment, state, action, reward, policy.
4. Explain the difference between learning from examples (supervised) and learning
   from rewards (reinforcement).
5. Explain the explore-versus-exploit trade-off in one or two sentences.

*Why it matters here:* the gates in Phases 3 to 5 compare win rates, and Phase 3
frames the game as states, actions and rewards.

## What happens next

From your marks, each phase's study list gets adjusted: **N** topics get a short
explanation from scratch before we use them, **~** topics get a refresher, and **Y**
topics are skipped.
