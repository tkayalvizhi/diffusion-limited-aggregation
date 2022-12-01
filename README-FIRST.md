# Diffusion Limited Aggregation Simulation


Run:
`python dlasimulation.py dimension stickiness drift max_dist iteration folder_path from_edge frame_count`

Example: ``python dlasimulation.py 501 0.5 2 500 40000 simulation_results/frames false 10 ``

* dimension - (integer) starting from 501. Dimension of Image or Field
* stickiness - (float) between 0 and 1. float) the stickiness factor which determines the probability of a particle aggregating
* drift - (float) greater than 0. the factor of drift towards the center. Higher the drift more strongly is the attraction to the center
* max_dist - (integer) represents the maximum allowed squared distance between 
the particle and the aggregated particles before the random walk begins.
 If greater the particle is regenerated
 

