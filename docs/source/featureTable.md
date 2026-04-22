# Layouts

| Shape | Angle (theta) | Center control | Scaling | Random seed | Sizing | max iter | Init coords | Additional params* |
|-|-|-|-|-|-|-|-|-|
| Line| ✓ | ✕ | ✕| ✕| ✕ | ✕ | ✕ | todo: center control |
| Circle | ✓ | ✓ | ✓| ✕| ? |✕ | ✕ | Radius |
| Shell | ✓ | ✓ | ✓| ✕| ✕ |✕ | ✕ | Nlist, Radius |
| Spiral | ✓ | ✓ | ✓| ✕| ✕ |✕ | ✕ | Radius, slope, exponent |
| Random | ✕ | ✕ | ✕| ✓| ✕ |✕ | ✕ | Min & Max x,y, max_tries |
| Grid | ✕ | ✕ | ✓| ✕| ✕ |✕ | ✕ | width, shape, trim_even_rows (triangular) |
| Bipartite | ✕ | ✓ | ✕ | ✕| ✕ |✕ | ✕ | first partition |
| Multipartite | ✕ | ✓ | ✕| ✕| ✕ |✕ | ✕ | nlist (list of nodelist) |
| Sugiyama | ✕ | ✓ | ✕ | ✕| ✕ |✕ | ✕ | first partition |
| Spring | ✕ | ✕ | ✓ | ✓ | ✓ |✓ | ✓ | Optimal_distance, Gravity, Fixed nodes, method (force/energy), exponent attraction/repulsion, etol|
| Kamada Kawai | ✕ | ✕ | ✕ | ✓ | ✕ |✕ | ✕ | - |
| Arf | ✕ | ✓ | ✓ | ✓| ✕ |✓ | ✓ | Etol, Spring_strengh, dt (time step) |
| Forceatlas2| ✕| ✓ | ✓| ✓ | ✓ |✓ | ✓ | Jitter_tolerance, Gravity + Strong_gravity, Distribution_action, Mass, Dissuade_hubs, Linlog, Etol |
| Graph embedder| ✕| ✓ | ✓ | ✓ | ✓ | ✓| ✓ | etol, inplace |
| Large graph layout| ✕ | ✓ | ✓| ✓| ✕ | ✓|✓ | inplace |
| Geometric | ✕ | ✓ | ✕ | ✓| ✕ |✕ | ✕ | edge lengths, tol |
| Multidimensional scaling | ✕ | ✓ | ✕ | ✕ | ✕ |✕ | ✕| distance_matrix, inplace, check_connectedness |
| UMAP | ✕ | ✕ | ✕ | ✕ | ✕ |✓ | ✓ | edge distance & weights, fixed, min_dist, spread, negative_sampling_rate, inplace, backend |

* See [Layout documentation](./api/layouts.md) for exact requirements and further information about these params.