---
url: https://en.wikipedia.org/wiki/Swarm_intelligence
title: Swarm Intelligence
scraped_at: '2026-05-03T04:55:10Z'
word_count: 2941
raw_file: raw/2026-05-03_swarm-intelligence_c28cc8a7.txt
tldr: Swarm intelligence is the study of decentralized, self-organized collective behavior in simple agents—illustrated by boids, ant colony optimization, particle swarm optimization, robotics, routing, and human swarming—with the article mixing foundational models, applications, and several newer or more speculative examples.
key_quote: Swarm intelligence (SI) is the collective behavior of decentralized, self-organized systems, natural or artificial.
durability: medium
content_type: mixed
density: high
originality: synthesis
reference_style: deep-study
scrape_quality: partial
people:
- Jing Wang
- Gerardo Beni
- Craig Reynolds
- John H. Reif
- Hongyan Wang
- Marco Dorigo
- Russell C. Eberhart
- James Kennedy
- Louis Rosenberg
- al-Rifaie
- Michael Theodore
- Nikolaus Correll
- Eric Bonabeau
- Guy Theraulaz
- Andries Engelbrecht
tools:
- Massive
libraries: []
companies:
- Hewlett-Packard
- NASA
- European Space Agency
- Southwest Airlines
- Stanford University School of Medicine
- University of California San Francisco
- Food and Agriculture Organization
tags:
- swarm-intelligence
- collective-behavior
- optimization
- robotics
- metaheuristics
---

### TL;DR
Swarm intelligence is the study of decentralized, self-organized collective behavior in simple agents—illustrated by boids, ant colony optimization, particle swarm optimization, robotics, routing, and human swarming—with the article mixing foundational models, applications, and several newer or more speculative examples.

### Key Quote
"Swarm intelligence (SI) is the collective behavior of decentralized, self-organized systems, natural or artificial."

### Summary
- **Core definition**
  - Swarm intelligence (SI) refers to collective behavior in **decentralized, self-organized systems**.
  - The term was introduced by **Jing Wang and Gerardo Beni in 1989** in the context of **cellular robotic systems**.
  - Typical SI systems contain many **simple agents/boids** that interact locally with each other and their environment.
  - There is **no centralized controller**; global “intelligent” behavior emerges from local and partly random interactions.
  - Natural inspirations include **ant colonies, bee colonies, bird flocking, herding, fish schooling, bacterial growth, and microbial intelligence**.

- **Relationship to robotics and optimization**
  - **Swarm robotics** is the application of swarm principles to robots.
  - **Swarm intelligence** is the broader category of algorithms inspired by swarms.
  - The article also mentions **swarm prediction** for forecasting and **synthetic collective intelligence** for genetically modified organisms.

- **Models of swarm behavior**
  - **Boids (Reynolds 1987)**
    - Craig Reynolds’ 1986/1987 artificial life simulation of flocking.
    - Based on three simple rules:
      - **Separation**: avoid crowding neighbors
      - **Alignment**: steer toward average heading
      - **Cohesion**: move toward average position
    - Can be extended with obstacle avoidance and goal seeking.
  - **Self-propelled particles / Vicsek model (1995)**
    - Particles move at constant speed and adjust direction toward the average direction of local neighbors, with random perturbation.
    - Used to study universal, robust group-level swarming behavior.
    - Presented as a minimal statistical model of collective motion.
  - **Social Potential Fields (Reif & Wang 1999)**
    - Early robot-swarm control model using artificial attraction/repulsion force laws.
    - Distributed and asynchronous.
    - Demonstrated behaviors like **clustering, guarding, escorting, patrolling**.
    - Claimed robustness to sensor and actuator errors.

- **Metaheuristics**
  - The article identifies major nature-inspired optimization methods as:
    - **Evolutionary algorithms (EA)**
    - **Particle swarm optimization (PSO)**
    - **Differential evolution (DE)**
    - **Ant colony optimization (ACO)**
  - It notes that many newer metaphor-based metaheuristics have been criticized for lacking novelty.
  - A key limitation of metaheuristics: they do not provide a built-in confidence measure for solution quality unless the problem allows it.

- **Key optimization algorithms**
  - **Ant colony optimization (Dorigo 1992)**
    - Probabilistic optimization modeled on ant foraging and pheromone trails.
    - Artificial ants explore solution spaces and reinforce better paths.
  - **Particle swarm optimization (Kennedy, Eberhart & Shi 1995)**
    - Global optimization method where particles move through n-dimensional solution space.
    - Particles accelerate toward better-performing neighbors.
    - Highlighted for resilience against local minima.

- **Artificial swarm intelligence / human swarming**
  - **Artificial Swarm Intelligence (ASI, 2015)**
    - Uses control algorithms modeled on natural swarms to amplify the collective intelligence of human groups.
    - Also called **human swarming** or **Swarm AI**.
    - Cited applications:
      - Business forecasting
      - Sports betting predictions
      - Medical diagnosis
      - FAO famine forecasting
  - **Human swarming (Louis Rosenberg, 2015)**
    - Real-time closed-loop systems connect distributed users into “human swarms.”
    - The article cites studies where doctors working in swarms achieved:
      - **33% reduction in diagnostic errors** for chest X-rays
      - **22% improvement over traditional machine learning**
      - **23% increase in MRI diagnostic accuracy** versus majority voting in a UCSF preprint

- **Applications**
  - **Military and aerospace**
    - U.S. military: unmanned vehicles
    - ESA: orbital swarm for self-assembly/interferometry
    - NASA: planetary mapping
  - **Medicine**
    - Tumor localization and cancer-related nanobot concepts
    - Medical diagnosis and bioinformatics
  - **Networks and telecom**
    - Ant-based routing in telecommunication networks
    - Wireless sensor network placement and routing
  - **IoT and networking**
    - Applied to **Internet of Things** and **Intent-Based Networking**
  - **Data mining and clustering**
    - Used for feature selection, cluster analysis, and optimization
  - **Traffic, power, and smart grids**
    - Traffic signal control, routing, congestion reduction
    - Load balancing and energy optimization
  - **Gaming, simulations, and crowd behavior**
    - Crowd simulation and realistic group motion

- **Ant-based routing**
  - Describes network routing inspired by ants, with control packets (“ants”) reinforcing successful routes.
  - Developed in the mid-1990s by **Dorigo et al.** and **Hewlett-Packard**.
  - Notes practical challenges because the method is stochastic and less repeatable.
  - Also mentions **stochastic diffusion search (SDS)** for wireless infrastructure placement.
  - Gives an airline example: **Southwest Airlines** used ant-based routing ideas for airport gate assignment.

- **Crowd simulation**
  - Swarm methods are used for generating complex crowds and motion.
  - Examples cited:
    - **The Lord of the Rings** trilogy via **Massive** software
    - **Stanley and Stella in: Breaking the Ice** for fish and bird motion
    - **Batman Returns** for bats
  - Also mentions plane boarding simulation at Southwest Airlines.

- **Creative and artistic uses**
  - **Swarm grammars**
    - Evolved stochastic grammars applied to art and architecture.
  - **Swarmic art**
    - Uses hybrid swarm algorithms to generate drawings, sketches, and color-based artwork.
    - Mentions work by **al-Rifaie et al.** using:
      - **SDS** for local search/attention
      - **PSO** for sketching/global behavior
    - Also mentions the idea of computational creativity and lifelike behavior in engineered systems.

- **Article structure and completeness**
  - The extract includes sections for:
    - Models of swarm behavior
    - Metaheuristics
    - Applications
    - Notable researchers
    - See also
    - References
    - Further reading
    - External links
  - However, several sections like **Notable researchers**, **See also**, and **References** appear empty in the provided capture.

### Assessment
This is a **reference** article with a **mixed** content type: it combines foundational definitions, historical notes, model descriptions, applications, and examples. Durability is **medium-high**: the core concept of swarm intelligence is stable, but some application claims and especially newer sections like human swarming/ASI and current application examples may age as the field changes. Density is **high**, with many specific algorithms, dates, authors, and use cases packed into the extract. Originality is primarily **synthesis** rather than a single original research source, since it summarizes a broad field and cites many works. It is best used **deep-study** or **refer-back** style if you want an overview plus pointers to specific models. Scrape quality is **partial**: the capture includes substantial article text, but some standard Wikipedia sections appear incomplete or empty, and references/details may be missing.
