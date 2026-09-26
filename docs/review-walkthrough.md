# Ten-minute project walkthrough

How should Noah explain the work to Michael or a reviewer?

1. **The need (one minute):** a team needs temporary communications across an obstruction. Service time alone is insufficient; the aircraft must deploy and recover with reserve. Show the mission context.
2. **The architecture (two minutes):** explain mission management, flight support, relay service and energy support. Then show their physical allocations. Battery choice changes installed mass and energy, not the mission or radio architecture.
3. **The six choices (one minute):** two packs at three stations. The convenient station has a blocked service hop; balanced and elevated stations cost more flight energy.
4. **The accounting (two minutes):** use `results/worked-example.md`. Show the separate propulsion/auxiliary boundary, six segments and reserve. Explain that every input is illustrative.
5. **The result (two minutes):** no option meets the 900 s baseline; B2-S2 is close. Use the decision boundary to explain why a small power-model error matters. Tests establish calculation behavior, not physical performance.
6. **The contributions (two minutes):** Noah owns architecture, interfaces, trace and trade framing. Michael owns the constrained physical derivation, supporting evidence and uncertainty interpretation. The Mermaid presentation is assembled; architecture acceptance and physical validation remain separate reviews.

## Decisions to ask for at Noah's acceptance review

Accept or revise the fictional scenario, six-option scope, reserve convention, selection rule and conceptual physical interfaces. Decide whether the project remains a conceptual architecture study or substitutes evidenced hardware inputs. Do not ask Michael to independently rebuild the architecture, select radios or write a flight controller.

## What would make the result publishable?

A supported physical conclusion that explains or changes a meaningful configuration decision, with a clear distinction from existing work. The deliverables support that assessment; they do not establish novelty by themselves. If the result remains illustrative, describe it as an engineering case study or student project.
