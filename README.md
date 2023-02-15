Simple utility for helping you reduce your storage layout costs.
Optimal layout is NP-hard, but "first fit" is an algorithm that works well enough in general.
The goal is simply to quickly identify optimizations and suggest them.

This is just a proof of concept.
Ideally this should be part of solc.

Run:

```
$ solc --storage-layout Example.sol | tail -n +4 | python3 __main__.py
```

TODOs:

- [ ] A a deadline/depth kill switch: once we have at least one solution start a clock: every new call decreases the clock, when it hits 0 we return None all over, get the current best result. That means we implement first fit and can then _only do better_.
- [ ] Pack structs, also recursively.
- [ ] Insert packed structs in algo, to improve packing further
- [ ] Preserve original order as much as possible
- [ ] Remove vars >= 32 bytes from problem (optimization) and use them to preserve order
- [ ] Optional strategy: preserve slots, keep vars that share a slot colocated, for more optimal access (assuming the dev collocates for a reason), maybe make it a feature flag
- [ ] Support multiple contracts and don't reorder all variables across contracts
- [ ] Try reordering imports to preserve storage slots (likely devs are missing this/unaware how imports affect slot order)

