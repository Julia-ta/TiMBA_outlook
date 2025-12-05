
# Development Workflow

- Follow NumPy docstrings, type hints, line length 88.
- Comments should explain scientific rationale. Include references to relevant
  literature and standards where applicable
- Track agent operations with git commit hash numbers


# Agent Operations

- Modified the load_timba_output_pickle function in TiMBA/outlook/post_processor.py to
- rename dictionary keys to snake case using the to_snake_case function.
- Updated the load_metadata_from_world_input_file function in
  TiMBA/outlook/post_processor.py to use snake_case column names for DataFrame
  selections after renaming columns.
- Defined EU_COUNTRIES_LIST as a list containing EU country names in
  TiMBA/outlook/post_processor.py.

