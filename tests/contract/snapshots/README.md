# Contract test snapshots

Each `<endpoint_name>.json` file in this directory is a structural "shape" snapshot
of the `data` payload returned by the corresponding upstream Sure Petcare API
endpoint (see `tests/contract/shape.py` for the format).

## Bootstrapping / updating snapshots

Run the contract tests with real credentials and `--update-snapshots` to (re)write
all snapshot files based on the current live API responses:

```bash
export SUREHUB_EMAIL={your_email}
export SUREHUB_PASSWORD={your_password}
poetry run pytest tests/contract --update-snapshots
```

Review the diff of the generated/updated files before committing - this is the
point where an upstream schema change gets consciously accepted into the baseline.
If a Pydantic model in `surehub_api/entities/` needs to be updated to match, do that
as part of the same change.
