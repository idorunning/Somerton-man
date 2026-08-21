# Finding — Transport route designation test

**Date:** prior session, undated
**Verdict: clean negative. The code lines are not transport route designations, and they do
not match consecutive stop initials on any 1948 Adelaide route in either direction.**

## What was tested

Two related propositions, both alternatives to the place-initial reading:

1. That the letter strings are route codes — that a line such as `MTBIMPANETP` is a
   designation the transport operators themselves used.
2. That the letter strings match the initials of consecutive stops along a single route, read
   in order.

## Result on proposition 1

Rejected on documentary grounds. Adelaide's route designation conventions in 1948 did not use
letter codes of this kind:

- Municipal Tramways Trust trams used **numeral** route numbers, and had done since 1917.
- Buses and trolleybuses were designated by **destination name** only.
- Letter-suffix route codes did not appear in Adelaide until **1962**, fourteen years after
  the relevant period.

There is no 1948 scheme in which these strings could be route designations.

## Result on proposition 2

Rejected on search. No exact consecutive stop-initial match was found for any of the five code
lines on any 1948 Adelaide train, tram, trolleybus, bus or coach route, tested in both
directions of travel.

## Why the negative is useful

It closes off the simplest deterministic reading. If a line had matched a real route's stop
sequence exactly, the case would have been made in a single stroke and no statistical work
would have been needed. That did not happen.

It also tightens what the hypothesis can claim. The itinerary reading now has to be an
itinerary *across* the network — multiple routes, interchanges, mode changes — rather than a
single line ridden end to end. That is a harder thing to demonstrate and a more demanding
version of the claim.

## Limits of this result

The search depended on the completeness of the 1948 route and stop-sequence data available at
the time. A stop list with gaps could hide a match. The negative is as strong as the source
coverage, and the source coverage has not been independently audited.
