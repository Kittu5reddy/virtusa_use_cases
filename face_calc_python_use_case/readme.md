# CityCab — FareCalc (Python)

## Table of Contents

- Problem Statement
- Project Structure
- Installation
- Command-line Usage
- GUI (Streamlit) Usage
- Persistence & Database
- Scalability & Next Steps
- Contributing
- License

## Problem Statement

Core Python: The "FareCalc" Travel Optimizer

Business Case: A ride-sharing startup, "CityCab," needs a backend script to calculate fares. The fare isn't flat; it changes based on the time of day (Peak Hours) and the type of vehicle requested.

Write a script that calculates the final "Ride Estimate" based on distance, vehicle type, and a "Surge Pricing" multiplier.

Student Tasks implemented in this repository:

1. Dictionary Mapping: Vehicle rates per km are stored in `constants.py` (e.g., ECONOMY, PREMIUM, SUV).
2. Surge Logic: If the travel hour is between 17 and 20 (5 PM - 8 PM), a 1.5x surge multiplier is applied.
3. Function Definition: `service.fare_service.calculate_fare(km, type, hour)` returns the final price and surge multiplier.
4. Error Handling: Invalid vehicle types raise `VehicleTypeNotFoundException`.

## Project Structure

Top-level layout:

```
__init__.py
app.py
constants.py
main.py
problem_statement.txt
readme.md
requirements.txt
database/
	__init__.py
	model.py
	repositary.py
exceptions/
	vehicle_type_not_found_exception.py
images/
repository/
	fare_repository.py
service/
	fare_service.py
```

- `main.py` — Command-line entrypoint and DB initialization (runs `command_line_main()` when executed).
- `app.py` — Streamlit GUI for Fare Calculator and Transactions dashboard.
- `service/fare_service.py` — Core fare calculation logic (`calculate_fare`).
- `repository/fare_repository.py` — DB access for storing and retrieving fare transactions.
- `database/` — SQLAlchemy model and DB engine/session.
- `exceptions/vehicle_type_not_found_exception.py` — Custom exception for unsupported vehicle types.

## Installation

Prerequisites:

- Python 3.8+
- pip

Install dependencies:

```bash
pip install -r requirements.txt
```

The repository includes `requirements.txt` with `streamlit`, `sqlalchemy`, and `pandas` (verify versions as needed).

## Command-line Usage

Run the command-line version which prompts for inputs and prints a receipt:

```bash
python main.py
```

Behavior:

- Creates database tables on first run (via `Base.metadata.create_all`).
- Prompts for distance (km), vehicle type (Economy/Premium/SUV), and hour (0-23).
- Prints a formatted Ride Estimate and handles invalid inputs.

## GUI (Streamlit) Usage

Run the Streamlit dashboard for an interactive UI:

```bash
streamlit run app.py
```

Features:

- Fare Calculator page with inputs for distance, vehicle type and hour.
- Transactions page showing saved rides (reads from the configured DB).

## Persistence & Database

- A simple SQLite/SQLAlchemy setup is used via `database/*` and `repository/fare_repository.py`.
- `main.py` ensures tables are created automatically on startup.
- The Streamlit app uses `SessionLocal` to query transactions for the Transactions page.

## Scalability & Next Steps

Design considerations and steps to scale this prototype into a production-ready service:

- API Layer: Expose the fare calculator as a REST API (Flask/FastAPI) so multiple clients can consume it.
- Microservices: Split responsibilities (pricing service, transactions service, auth) for independent scaling.
- Persistent DB: Move from SQLite to a managed DB (Postgres, Azure Database) for concurrency and reliability.
- Caching: Use Redis to cache frequently used rate info and reduce DB reads.
- Load Testing: Simulate traffic with tools like `locust` or `k6` before scaling horizontally.
- Containerization: Add `Dockerfile` and orchestration manifests (Kubernetes / Docker Compose) for reproducible deployments.
- Observability: Add logging, metrics (Prometheus), and tracing (OpenTelemetry) for production diagnostics.

## Contributing

1. Fork the repo
2. Create a feature branch
3. Open a PR with a clear description

Please run existing checks and unit tests (if any) before submitting a PR.

## License

Specify your license here (e.g., MIT). If unsure, add a `LICENSE` file.

---

If you want, I can also:

- Add a short `docker-compose.yml` demonstrating local DB + app run.
- Generate a `requirements.txt` with pinned versions.
- Add examples of unit tests for `calculate_fare`.
