# Michael's physics packet

What physical limits support—or overturn—the provisional battery and station choice?

**Ready now:** executable baseline, exact segment ledgers, input snapshot and an assistant-prepared derivation/check script. **Not done:** Michael's derivation review, data-based domain assessment and justified uncertainty bounds. No contribution is attributed to him yet.

Run `PYTHONPATH=src python physics/analytical_starter.py`. It compares the dimensionless expression to all six discrete energy ledgers, checks the analytic derivative with central differences, and recovers the ideal stationary point. Its output is included in `results/algebra-checks.json`.

## Model contract
`evaluate_option(vehicle, battery, station, mission, physics, radio, obstacle, power_multiplier=1)` returns a JSON-serializable dictionary. Geometry is local ENU in m, duration s, power bus W, energy Wh, mass kg, link margin dB. The reference power excludes auxiliary loads. Every segment powers avionics and relay continuously, including transit. Inputs are not mutated.

The result contains the gross mass; usable/reserve/planned energy; six-segment ledger; signed energy margin and signed maximum energy dwell; two hop results; R1–R5 gates; unassessed compatibility; model-domain and review status. The maximum energy dwell is not clipped when the nonservice sortie already fails. `evaluate` validates the complete configuration before calling this function.

## Prepared algebra: review rather than start from zero
Let nonbattery mass be $m_d$, installed pack mass $m_b$, and $\mu=m_b/m_d$. The B2 mount increment belongs in $m_d$. Let $P_0=a m_d^{3/2}$, $\lambda=P_a/P_0$, $\tau_q=\sum_{s\ne relay} k_s t_s$, and $t_q=\sum_{s\ne relay}t_s$. Pack specific energy $e_b$ is in J/kg; $\beta=u(1-r)$ combines usable and reserve fractions exactly once. Set $H=\beta e_bm_d/P_0$ (seconds).

For unity relay factor and constant auxiliary load:

$$T(\mu)=\frac{H\mu-(1+\mu)^{3/2}\tau_q-\lambda t_q}{(1+\mu)^{3/2}+\lambda}.$$

This follows by equating allocable pack energy to propulsion plus auxiliary energy over nonservice time and service time. Put $f=(1+\mu)^{3/2}$, $N=H\mu-f\tau_q-\lambda t_q$ and $D=f+\lambda$. Then

$$T' = \frac{(H-f'\tau_q)D-Nf'}{D^2},\qquad f'=\tfrac32\sqrt{1+\mu}.$$

The marginal-benefit condition is $T'>0$; stationary candidates solve its numerator=0. The admitted optimum also requires checking endpoints and mass/power constraints. At $\lambda=\tau_q=t_q=0$, the stationary point is $\mu=2$. This is a familiar limiting result, not a practical recommendation or novelty claim.

$H$, $\tau_q$ and $t_q$ retain time dimensions: the script nondimensionalizes mass and power, not time. A fully dimensionless time is $\theta=T/H$, with $\hat\tau_q=\tau_q/H$ and $\hat t_q=t_q/H$.

For a local continuous curve, hold specific energy, installation family, geometry, efficiency and segment factors fixed. The two actual packs have different specific energies and mounts; do not fit one continuous curve through both and call it a shared battery family.

## Three focused assignments
1. **Derive and constrain:** verify the algebra, identify the admitted mass interval and constrained optimum, and explain where adding battery stops improving service. Deliver an annotated 2–4-page note and changes to the starter script. Details in issue 10.
2. **Establish physical support:** inspect a small public source set; identify mass, thrust, power and operating-state validity. Separate fitted from held-out evidence. Fill `physics/evidence-template.csv` or replace it with a completed table. Hover agreement does not validate transit/descent multipliers. Details in issue 11.
3. **Bound the decision:** derive sensitivities and justified uncertainty intervals; propagate common parameters consistently through all six alternatives and the selector. Deliver one boundary figure and whether the preferred option survives. Details in issue 12.

For fixed mission and masses, energy margin decreases monotonically with a positive propulsion multiplier and increases with usable pack energy. Those endpoints suffice for these individual rectangular bounds. A shared parameter vector must apply to all alternatives when comparing winners. More general coupled parameters need their own extrema justification. The existing ±10% plot is an illustrative sensitivity, not an inferred discrepancy bound.

## Handback and stopping point
Return the reviewed note/script, evidence table, one physical decision-boundary figure and a short interpretation. Use a null result if choices cannot be distinguished. If data are inadequate, retain “unsupported” rather than adding a CFD or flight-test program. Noah/Codex handles formatting and integration.

Candidate reading, not validated input data: [Zeng, Xu and Zhang](https://arxiv.org/abs/1804.02238) develops rotary-wing propulsion/communications optimization; [energy-model experimental validation](https://arxiv.org/abs/2005.01305) is a candidate for operating-state evidence. Neither establishes this illustrative airframe's coefficients. No material from either has been copied into the numerical inputs.


## Added engineering preparation

`results/decision-boundaries.json` supplies the exact fixed-configuration energy and power break-even multipliers. `results/decision-boundary.png` shows an illustrative shared-power sweep with failed-link alternatives marked. These isolate why the baseline is sensitive; they do not replace your mass-domain derivation or source-based uncertainty assessment. The assembled Mermaid book explains the architecture; your work can proceed directly from the Python packet.
