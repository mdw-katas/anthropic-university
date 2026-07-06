# CS 440 — Deep Learning and Large Language Models

**Prerequisites:** CS 430
**Language:** Python (PyTorch)

## Course Description

Modern neural networks, from backpropagation to the transformer — the
architecture behind the large language models reshaping the industry (and
this curriculum's own delivery mechanism). Emphasis on building working
models at small scale to understand the real ones: train a small
transformer, then study how the frontier systems extend the same recipe.

## Learning Objectives

- Implement backpropagation and a training loop from scratch, then
  translate to PyTorch's autograd idioms.
- Diagnose and stabilize training: initialization, normalization, learning
  rate schedules, the optimizer zoo (SGD to Adam).
- Explain the transformer completely: embeddings, attention, positional
  information, the block structure.
- Train a small language model end to end: tokenization, next-token
  prediction, sampling strategies.
- Explain how LLMs become assistants: pretraining, instruction tuning,
  RLHF (survey) — and their capabilities, costs, and failure modes.

## Topic Outline

1. From CS 430's perceptron to deep networks; why depth works.
2. Backpropagation in detail; automatic differentiation.
3. Training dynamics: initialization, vanishing/exploding gradients,
   batch/layer normalization, residual connections.
4. Optimizers and schedules: SGD, momentum, Adam; regularization (dropout,
   weight decay, augmentation).
5. Convolutional networks (survey): vision as a case study in inductive
   bias.
6. Sequence modeling: RNNs and their limits — motivation for attention.
7. Attention and the transformer architecture, piece by piece.
8. Language modeling: tokenization (BPE), embeddings, next-token
   prediction, sampling (temperature, top-p).
9. Training a small GPT-style model; scaling laws (survey).
10. From LM to assistant: instruction tuning, RLHF/RLAIF (survey),
    system prompts and tool use.
11. Using LLMs as an engineer: prompting, retrieval-augmented generation,
    fine-tuning vs. context, evaluation.
12. Limits and safety: hallucination, bias, alignment questions; reading
    the current literature critically.
