# Diffusion Limited Aggregation Simulation
<i>" "Diffusion" because the particles forming the structure wander around randomly before attaching themselves ("Aggregating") to the structure. "Diffusion-limited" because the particles are considered to be in low concentrations so they don't come in contact with each other and the structure grows one particle at a time rather then by chunks of particles.... "</i> 
reference: http://paulbourke.net/fractals/dla/

<img align="center" src="simulation_results/sim_15_loop.gif" width="300" height="300" />

## Objective:
Computer simluate DLA. 


Run:
`python dlasimulation.py dimension stickiness drift max_dist iteration folder_path from_edge frame_count`

Example: ``python dlasimulation.py 501 0.5 2 500 40000 simulation_results/frames false 10 ``

* dimension - (integer) starting from 501. Dimension of Image or Field
* stickiness - (float) between 0 and 1. float) the stickiness factor which determines the probability of a particle aggregating
* drift - (float) greater than 0. the factor of drift towards the center. Higher the drift more strongly is the attraction to the center
* max_dist - (integer) represents the maximum allowed squared distance between 
the particle and the aggregated particles before the random walk begins.
 If greater the particle is regenerated
 
 ## Objects
 * [Particle](Particle.py) - A particle object performs the random walk. Assumption -  It can move to any of the 8 neighbouring pixels depending on the direction specified to it. 
    - NorthWest
    - North
    - NorthEast
    - East
    - SouthEast
    - South
    - SouthWest
    - West
 * [Field](Field.py) - Field / "Image" captures the particle movements and aggregation. The Field object allows certain customizations to the particle movements. Initially the field is empty with one particle at the center.
 * [DlaSimulation](dlasimulation.py) - DlaSimulation simulates the Diffusion Limited Aggregation and stores 
 images at regular intervals
 * [BinarySearchTree](BST.py) - The BinarySearchTree class is used to store the aggregated particles. It can find the nearest aggregated particle to a given particle. 
  
 ## Approaches
 |Approach 1 |Approach 2 A| Approach 2 B| Approach 3|
 |:---:|:---:|:---:|:---:|
 |![dla_1](simulation_results/randomwalk1.gif "low_drift")|![dla_1](simulation_results/randomwalk2.gif "low_drift")|![dla_1](simulation_results/randomwalk2_2.gif "low_drift")|![dla_1](simulation_results/randomwalk3.gif "low_drift")|
|No drift|Low drift|Higher drift|Drift with optimal start|
 ### Naive Approach 
  - The particle starts the random walk from the edge pixels
  - The particle moves to any of the four neighbouring pixels with equal probability.
 
 In this case the simulation is extremely slow. As the probability to reach the center pixel is negligible.
 
 ### Approach 2
   - The particle starts the random walk from the edge pixels
   - The particle moves randomly but in general drifts towards the center
   
  The simluation is still slow, as most of the time the particle is random walking far from the center.

   
 ### Approach 3 - drift towards center
   - The particle starts from a random pixel at a certain "max_dist" away from the nearest aggregated particle.
   - The particles also starts at a minimum distance from the aggregated particles
   - The particle moves randomly but in general drifts towards the center
     
   To get the distance from the nearest aggregated particle, a binary search tree (BST) is used to store the aggregated particles. 
   For a given particle, the BST can get the nearest aggregated particle or the distance to the nearest aggregated particle.
  
   
   This enhances the speed of simulation, as the starting pixel of a particle is not too far away.  

 ### Approach 4 - drift towards nearest aggregated particle
   - The particle starts from a random pixel at a certain "max_dist" away from the nearest aggregated particle.
   - The particles also starts at a minimum distance from the aggregated particles
   - The particle drifts towards the nearest aggregated particle

 ## [Simulation Results](simulation_results)
 * [sim1](simulation_results/sim1) - stickiness factor = 1, max_dist = 1000, iterations = 2000, attractor = center
 <img align="center" src="simulation_results/sim_1_loop.gif" width="300" height="300" />
 
 * [sim2](simulation_results/sim4) -  stickiness factor = 0.5, max_dist = 500, iterations = 3500, attractor = center
 <img align="center" src="simulation_results/sim_5_loop.gif" width="300" height="300" />
 
  * [sim3](simulation_results/sim5) -  stickiness factor = 0.5, max_dist = 500, iterations = 3500, attractor = nearest neighbour
 <img align="center" src="simulation_results/sim_14_loop.gif" width="300" height="300" />
 
  * [sim4](simulation_results/sim8) -  stickiness factor = 0.2, max_dist = 300, iterations = 20000, attractor = nearest neighbour
 <img align="center" src="simulation_results/sim_15_loop.gif" width="300" height="300" />
 
