# Layouts
 ## Geometric
| Feature | line | circle | shell | spiral | random | grid |
|--------|------|--------|-------|--------|--------|------|
| Angle (`theta`) | ✓ | ✓ | ✓ | ✓ | ✕ | ✕ |
| Center control | ✕ | ✓ | ✓ | ✓ | ✕ | ✕ |
| Scaling | ✕ | ✓ | ✓ | ✓ | ✓ | ✓ |
| random seed | ✕ | ✕ | ✕ | ✕ | ✓ | ✕ |
| sizes (`relative`) | ✕ | ? | ✕ | ✕ | ✓ | ✕ |

| Shape  | Angle (theta) | Center control | Scaling | Random seed | Sizing | Additional features |
|--------|----------------|----------------|---------|-------------|--------| --------|
| Line   | ✓              | ✓              | ✕       | ✕           | ✕      |
| Circle | ✕              | ✓              | ✓       | ✕           | ✓      |
| Shell  | ✓              | ✓              | ✓       | ✕           | ✓      |
| Spiral | ✓              | ✓              | ✓       | ✕           | ✓      |
| Random | ✕              | ✓              | ✕       | ✓           | ✓      |
| Grid   | ✕              | ✓              | ✓       | ✕           | ✓      |


Structure → 
Bipartite
- Network
- First
- theta
Multipartite
- Network
- Nlist
- theta
Sugiyama (layered graph)
- Network
- Theta
- Shift 
(node positioning, 1st partition, angle, List of lists of nodes in each layer, shift )

Spring
  Network
  Initial_coords
  optimal_distance
  Fixed
  Center
  Scale
  Gravity
Exponent attraction/repulsion
  Method
  Etol
  Max_iter
  Seed
  method
  Kamada_kawai
  Network
  seed
Attractive-repulsive forces layout
  Network
  Initial_coords
  Scaling
  Center
  Spring_strength
  Etol
  Dt
  max_iter
  Seed 
Forceatlas2
  Network
  intial_Coords
  Center
  Jitter_tolerance
  Scaling_ratio
  Gravity
  Distro_action
  Strong_gravity 
  Mass
  Size
  Dissuade_hubs
  Linlog
  Etol
  Max_iter
  seed
Graph_embedder
  Network
  Intiial_coords
  Center
  Etol
  Max_iter
  Seed
  inplace
Large_graph_layout
  Network
  Inital_coords
  Center
  Scaling
  Etol
  Max_iter
  Seed
  inplace
