# Armstrong Number Utilities

Utilities for checking and generating Armstrong (Narcissistic) numbers.

An Armstrong number (in base 10 by default) equals the sum of its digits,
each raised to the power of the number of digits. Examples: 0, 1, 153, 370,
371, 407.

## Features
- Typed API (`is_armstrong`, `generate_armstrong`).
- Robust input validation.
- Simple CLI for quick checks and listing.
- Optional support for arbitrary bases (`base >= 2`).

## Usage (CLI)
Check a single number:

```bash
python armstrong.py check 153
python armstrong.py check 154
python armstrong.py check 8208 --base 10
```

List numbers up to a limit:

```bash
python armstrong.py list 1000
python armstrong.py list 5000 --base 10
```

Exit codes:
- `0` when true or on success.
- `1` when false for `check`.
- `2` on invalid input.

## Programmatic API
```python
from armstrong import is_armstrong, generate_armstrong

assert is_armstrong(153)
assert not is_armstrong(154)

nums = generate_armstrong(1000)
assert 371 in nums
```

## Notes
- Complexity: `is_armstrong(n)` runs in O(k) where k is the number of digits.
- Base: If using `base != 10`, digits are computed in that base before powering.

---

# Sales Analytics Flask API

Optimized REST API for sales transactions: CRUD, totals per product, top customers, and filtered queries. Built for better time and space complexity using hash-indexes and incremental aggregates.

## Quick Start
- Install deps:

```bash
pip install -r requirements.txt
```

- Run the API:

```bash
python sales_analytics.py
```

- Health check:

```bash
curl http://127.0.0.1:5000/health
```

## Endpoints
- `POST /transactions` (body: `id`, `product_id`, `customer_id`, `amount`, `timestamp`)
- `GET /transactions/<id>`
- `GET /transactions` (query: `product_id`, `customer_id`, `min_amount`, `max_amount`, `start_ts`, `end_ts`)
- `PUT /transactions/<id>` (partial updates allowed)
- `DELETE /transactions/<id>`
- `GET /analytics/totals-per-product`
- `GET /analytics/top-customers?n=5`

## Complexity Improvements
- CRUD: O(1) average via dictionaries keyed by `id`.
- Totals per product: O(1) read using maintained `product_totals`.
- Top customers: O(C log n) using `heapq.nlargest` over `customer_totals`.
- Filtering: Indexed intersection first (product/customer → set of ids), then attribute checks; avoids full scans when filters are provided.
- Space: Minimal indexes (sets of ids), no duplicated datasets, aggregates compact and cleaned when zero.

## Benchmark
Run the server, then in a second shell:

```bash
python benchmark_sales_api.py
```

Outputs ingestion and analytics timings with counts.

## Tests
Run unit tests for CRUD and analytics correctness:

```bash
pytest -q
```

## Notes
- This API is intentionally kept in-memory for simplicity. Swap `SalesStore` with a DB-backed store (e.g., SQLite) for persistence or larger datasets.
- Timestamps are ISO 8601 strings; range filters parse with `datetime.fromisoformat`.
