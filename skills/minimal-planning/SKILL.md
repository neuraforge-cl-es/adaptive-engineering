---
name: minimal-planning
description: Produce a right-sized implementation plan with acceptance criteria, complexity budget, verification, and rollback proportional to the selected mode.
---
# Minimal Planning

Plan only enough to reduce execution risk.

## FAST
Usually no formal plan. If needed, use at most three execution bullets.

## STANDARD
Create a short plan containing:
1. acceptance criteria
2. files/components expected to change
3. implementation sequence (normally 3-7 steps)
4. targeted tests/verification
5. complexity budget

## DEEP
Add only the rigor the risk requires:
1. requirements and invariants
2. failure modes
3. considered approaches and selected trade-off
4. staged implementation
5. data/compatibility/rollback considerations
6. test and operational verification strategy
7. explicit complexity budget

## Rule

A plan must make implementation easier. If a plan repeats the request without resolving uncertainty, shorten it or investigate instead.
