from logging_config import init_logging_configurations


tenant = "sigma"
model = "info"

init_logging_configurations(tenant, model)

import helper
from db import initialize_db, simulate_error

initialize_db()

simulate_error()

initialize_db()

