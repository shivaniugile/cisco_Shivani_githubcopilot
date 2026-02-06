# Sales Analytics API - Quick Start Guide


### Step 1: Install Dependencies
```bash
cd "/Users/shugile/Desktop/copilot /Cisco/"
pip install flask pytest requests
```

### Step 2: Run the Inefficient API
```bash
python sales_api_inefficient.py
```
You should see:
```
INEFFICIENT SALES API - Running on http://localhost:5000
```

### Step 3: Test with Sample Data
Open a new terminal and run:
```bash
curl -X POST http://localhost:5000/transactions \
  -H "Content-Type: application/json" \
  -d @sample_data.json
```

### Step 4: Try the Endpoints

**Get all transactions:**
```bash
curl http://localhost:5000/transactions
```

**Sales per product:**
```bash
curl http://localhost:5000/sales/per-product
```

**Top customers:**
```bash
curl http://localhost:5000/customers/top?limit=5
```

**Analytics summary:**
```bash
curl http://localhost:5000/analytics/summary
```

---

## 📊 Compare Performance

### Step 1: Run Both APIs

**Terminal 1 - Inefficient API (Port 5000):**
```bash
python sales_api_inefficient.py
```

**Terminal 2 - Optimized API (Port 5001):**
```bash
python sales_api_optimized.py
```

### Step 2: Upload Data to Both
```bash
# Upload to inefficient
curl -X POST http://localhost:5000/transactions \
  -H "Content-Type: application/json" \
  -d @sample_data.json

# Upload to optimized
curl -X POST http://localhost:5001/transactions \
  -H "Content-Type: application/json" \
  -d @sample_data.json
```

### Step 3: Run Benchmark
**Terminal 3:**
```bash
python benchmark_sales_api.py
```

---

## 🧪 Run Tests

```bash
# Run all tests
pytest test_sales_api.py -v

# Run with coverage
pytest test_sales_api.py --cov=sales_api_inefficient --cov=sales_api_optimized -v

# Run specific test
pytest test_sales_api.py::TestPerformanceBenchmark -v
```

---


