# Week 1 Node Monitor

A small, production-style Python toolkit for parsing and summarizing cloud node status data (the kind of data typically returned by a cloud provider's API).

## Features
- Detect unique active node IPs
- Flag high-CPU-load nodes above a configurable threshold
- Detect duplicate IPs across nodes
- Calculate average CPU usage of active nodes (returns `None`, not `0`, when there's no data)
- Build a summarized report of node status

## Project Structure