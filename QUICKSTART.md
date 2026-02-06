# Sales Analytics API - Quick Start Guide

## 🚀 Quick Start (5 minutes)

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

## 📝 Your Assignment Tasks

1. **Analyze** `sales_api_inefficient.py`
   - Identify time complexity of each function
   - Document space complexity issues
   - Create `ANALYSIS.md`

2. **Study** `sales_api_optimized.py`
   - Understand optimizations applied
   - Compare with inefficient version
   - Document improvements

3. **Test** both versions
   - Run provided tests
   - Add your own tests
   - Verify correctness

4. **Benchmark** performance
   - Run benchmark script
   - Document results in `BENCHMARK_RESULTS.md`
   - Calculate speedup ratios

5. **Document** your findings
   - Create `OPTIMIZATION_REPORT.md`
   - Explain each optimization
   - Justify design decisions

---

## 💡 Key Inefficiencies to Find

### In `upload_transactions()`:
```python
# INEFFICIENT O(n²): Nested loops for duplicate check
for new_trans in new_transactions:
    for existing_trans in transactions:
        if existing_trans['transaction_id'] == new_trans['transaction_id']:
            # ...
```

**Optimization:** Use a set for O(1) lookup
```python
# OPTIMIZED O(n): Set lookup
if trans_id not in transaction_ids_set:
    transactions.append(trans)
    transaction_ids_set.add(trans_id)
```

### In `calculate_sales_per_product()`:
```python
# INEFFICIENT O(n²): Bubble sort
for i in range(n):
    for j in range(0, n - i - 1):
        if result[j]['total_sales'] < result[j + 1]['total_sales']:
            result[j], result[j + 1] = result[j + 1], result[j]
```

**Optimization:** Use built-in sort
```python
# OPTIMIZED O(n log n): Built-in sort
result.sort(key=lambda x: x['total_sales'], reverse=True)
```

### In `get_top_customers()`:
```python
# INEFFICIENT: Multiple passes through data
for customer_id in customer_ids:  # O(m)
    for trans in transactions:     # O(n)
        # Calculate totals
```

**Optimization:** Single pass with dictionary
```python
# OPTIMIZED: Single pass O(n)
customer_stats = defaultdict(lambda: {'total_amount': 0})
for trans in transactions:
    customer_id = trans.get('customer_id')
    customer_stats[customer_id]['total_amount'] += trans.get('amount', 0)
```

---

## 📈 Expected Performance Gains

With 1000 transactions, you should see:

| Operation | Inefficient | Optimized | Speedup |
|-----------|------------|-----------|---------|
| Upload | ~0.5s | ~0.05s | **10x** |
| Sales Calc | ~0.3s | ~0.03s | **10x** |
| Top Customers | ~0.4s | ~0.04s | **10x** |
| Filter | ~0.2s | ~0.02s | **10x** |
| Summary | ~0.3s | ~0.03s | **10x** |

---

## 🎯 Success Criteria

Your optimized version should:
- ✅ Pass all tests
- ✅ Be at least 5x faster for most operations
- ✅ Have O(n log n) or better time complexity
- ✅ Use appropriate data structures
- ✅ Be well documented

---

## 🆘 Troubleshooting

### Port Already in Use
```bash
# Kill process on port 5000
lsof -ti:5000 | xargs kill -9

# Kill process on port 5001
lsof -ti:5001 | xargs kill -9
```

### Module Not Found
```bash
pip install flask pytest requests
```

### Tests Failing
```bash
# Clear data before testing
curl -X DELETE http://localhost:5000/transactions
curl -X DELETE http://localhost:5001/transactions
```

---

## 📚 Additional Resources

- **Big O Cheat Sheet:** https://www.bigocheatsheet.com/
- **Python Time Complexity:** https://wiki.python.org/moin/TimeComplexity
- **Flask Documentation:** https://flask.palletsprojects.com/
- **pytest Tutorial:** https://docs.pytest.org/en/stable/getting-started.html

---

## 🎓 Using GitHub Copilot

### Helpful Prompts:

**For analysis:**
```
"Explain the time complexity of this function and identify inefficiencies"
```

**For optimization:**
```
"Optimize this function to reduce time complexity from O(n²) to O(n)"
```

**For testing:**
```
"Generate pytest unit tests for this Flask endpoint"
```

**For documentation:**
```
"Document this function with time/space complexity and usage examples"
```

---

## ✅ Next Steps

1. Read through both API files
2. Run the APIs and test endpoints
3. Run the benchmark to see performance difference
4. Start your analysis document
5. Study the optimizations
6. Complete your assignment

**Good luck! 🚀**
