Simple utility for helping you reduce your storage layout costs.
Optimal layout is NP-hard, but "first fit" is an algorithm that works well enough in general.
The goal is simply to quickly identify optimizations and suggest them.

This is just a proof of concept.
Ideally this should be part of solc.

Run:

```
$ solc --storage-layout Example.sol | tail -n +4 | python3 __main__.py
```
