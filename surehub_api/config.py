from dynaconf import Dynaconf, Validator

settings = Dynaconf(
    envvar_prefix="SUREHUB",
    settings_files=["settings.yaml", ".secrets.yaml"],
    validators=[
        Validator('email', 'password', must_exist=True),
        Validator('loglevel', is_in=['critical', 'error', 'warning', 'info', 'debug', 'trace']),
        Validator('endpoint', must_exist=True, condition=lambda v: isinstance(v, str) and v.startswith('https://')),
        Validator('port', must_exist=True, condition=lambda v: isinstance(v, int) and 1 <= v <= 65535),
        Validator('host', must_exist=True),
    ],
)
