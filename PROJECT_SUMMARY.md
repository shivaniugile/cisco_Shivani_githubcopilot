# 📦 Sales Analytics API - Complete Project Summary

## 🎯 Project Overview

A comprehensive assignment on **optimizing a Sales Analytics Flask API** using time & space complexity analysis. Includes:
- Intentionally inefficient API
- Fully optimized version
- Comprehensive test suite
- Performance benchmarking tools
- Complete documentation

---

## 📁 Project Structure

```
/Users/shugile/Desktop/copilot /Cisco/
│
├── sales_api_inefficient.py       # Intentionally inefficient API (O(n²))
├── sales_api_optimized.py         # Optimized API (O(n) or O(n log n))
├── benchmark_sales_api.py         # Performance comparison script
├── sample_data.json               # Sample transaction data
│
├── tests/                         # Organized test suite
│   ├── conftest.py               # Shared fixtures
│   ├── test_inefficient_api.py   # Unit tests for inefficient
│   ├── test_optimized_api.py     # Unit tests for optimized
│   ├── test_performance.py       # Performance benchmarks
│   ├── test_integration.py       # Integration tests
│   └── README.md                 # Test documentation
│
├── requirements.txt               # Python dependencies
├── pytest.ini                     # Pytest configuration
├── ASSIGNMENT.md                  # Complete assignment guide
└── QUICKSTART.md                  # Quick start guide
```

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
cd "/Users/shugile/Desktop/copilot /Cisco/"
pip install flask pytest requests
```

### 2. Run Inefficient API (Terminal 1)
```bash
python sales_api_inefficient.py
# Runs on http://localhost:5000
```

### 3. Run Optimized API (Terminal 2)
```bash
python sales_api_optimized.py
# Runs on http://localhost:5001
```

### 4. Run Tests
```bash
# All tests
pytest tests/ -v

# Quick tests (skip slow performance tests)
pytest tests/ -m "not slow" -v

# Performance benchmarks only
pytest tests/test_performance.py -v -s
```

### 5. Run Benchmark Script
```bash
python benchmark_sales_api.py
```

---

## 📊 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/transactions` | POST | Upload transactions |
| `/transactions` | GET | Get all transactions |
| `/transactions` | DELETE | Clear all transactions |
| `/sales/per-product` | GET | Calculate sales by product |
| `/customers/top` | GET | Get top customers |
| `/transactions/filter` | GET | Filter transactions |
| `/analytics/summary` | GET | Get analytics summary |

---

## 🔍 Key Inefficiencies & Optimizations

### 1. Upload Transactions
**Inefficient:**
```python
# O(n²) - Nested loops for duplicate check
for new_trans in new_transactions:
    for existing_trans in transactions:
        if existing_trans['transaction_id'] == new_trans['transaction_id']:
            # ...
```

**Optimized:**
```python
# O(n) - Set lookup
if trans_id not in transaction_ids_set:
    transactions.append(trans)
    transaction_ids_set.add(trans_id)
```

### 2. Sales Per Product
**Inefficient:**
```python
# O(n²) - Bubble sort
for i in range(n):
    for j in range(0, n - i - 1):
        if result[j]['total_sales'] < result[j + 1]['total_sales']:
            result[j], result[j + 1] = result[j + 1], result[j]
```

**Optimized:**
```python
# O(n log n) - Built-in sort
result.sort(key=lambda x: x['total_sales'], reverse=True)
```

### 3. Top Customers
**Inefficient:**
```python
# O(n*m) - Multiple passes
for customer_id in customer_ids:  # O(m)
    for trans in transactions:     # O(n)
        # Calculate totals
```

**Optimized:**
```python
# O(n) - Single pass with dictionary
for trans in transactions:
    customer_stats[customer_id]['total_amount'] += trans.get('amount', 0)
```

---

## 📈 Complexity Comparison

| Endpoint | Inefficient | Optimized | Improvement |
|----------|------------|-----------|-------------|
| Upload | O(n²) | O(n) | **n times** |
| Sales Calc | O(n²) | O(n log n) | **Significant** |
| Top Customers | O(n²) | O(n log n) | **Significant** |
| Filter | O(3n) | O(n) or O(k) | **3x faster** |
| Summary | O(5n²) | O(n) | **Massive** |

---

## 🧪 Test Organization

### Test Files
1. **`conftest.py`** - Shared fixtures
2. **`test_inefficient_api.py`** - 40+ unit tests for inefficient API
3. **`test_optimized_api.py`** - 45+ unit tests for optimized API
4. **`test_performance.py`** - Performance benchmarks
5. **`test_integration.py`** - Integration & workflow tests

### Test Markers
- `@pytest.mark.unit` - Unit tests
- `@pytest.mark.integration` - Integration tests
- `@pytest.mark.performance` - Performance tests
- `@pytest.mark.slow` - Long-running tests

### Run Tests
```bash
# All tests
pytest tests/ -v

# By marker
pytest tests/ -m unit -v
pytest tests/ -m performance -v -s
pytest tests/ -m integration -v

# Skip slow tests
pytest tests/ -m "not slow" -v

# With coverage
pytest tests/ --cov=. --cov-report=html
```

---

## 📝 Assignment Tasks

### Task 1: Analysis (20 pts)
- Analyze `sales_api_inefficient.py`
- Document time/space complexity
- Create `ANALYSIS.md`

### Task 2: Optimization (40 pts)
- Study `sales_api_optimized.py`
- Understand each optimization
- Explain improvements

### Task 3: Testing (20 pts)
- Run all tests
- Add custom tests
- Verify correctness

### Task 4: Benchmarking (10 pts)
- Run performance tests
- Document results
- Calculate speedups

### Task 5: Documentation (10 pts)
- Create optimization report
- Explain design decisions
- Document complexity

---

## 🎓 Using GitHub Copilot

### Analysis Prompts
```
"Analyze this function's time complexity and identify inefficiencies"
"Explain why this nested loop is O(n²)"
```

### Optimization Prompts
```
"Optimize this function from O(n²) to O(n)"
"Suggest better data structures for this operation"
```

### Testing Prompts
```
"Generate pytest tests for this Flask endpoint"
"Create performance benchmark tests comparing two functions"
```

### Documentation Prompts
```
"Document this optimized function with complexity analysis"
"Explain the optimization techniques used here"
```

---

## 📦 Key Files Explained

### Core Files
- **`sales_api_inefficient.py`** - Has O(n²) complexity, bubble sort, multiple passes
- **`sales_api_optimized.py`** - Uses sets, dicts, built-in sort, single-pass algorithms
- **`benchmark_sales_api.py`** - Standalone benchmarking tool
- **`sample_data.json`** - 10 sample transactions for testing

### Documentation
- **`ASSIGNMENT.md`** - Complete assignment guide (100 points breakdown)
- **`QUICKSTART.md`** - 5-minute quick start guide
- **`tests/README.md`** - Test suite documentation

### Configuration
- **`requirements.txt`** - Python dependencies
- **`pytest.ini`** - Pytest configuration with markers

---

## 🎯 Expected Results

### Performance Gains (1000 transactions)
| Operation | Speedup |
|-----------|---------|
| Upload | **10x faster** |
| Sales Calc | **10x faster** |
| Top Customers | **10x faster** |
| Filter | **10x faster** |
| Summary | **10x faster** |

### Test Coverage
- **95%+** code coverage
- **100+** total tests
- All endpoints tested
- Performance validated

---

## ✅ How to Complete Assignment

1. **Read** `ASSIGNMENT.md` for full details
2. **Run** both APIs and test them
3. **Analyze** the inefficient code
4. **Study** the optimized code
5. **Run** all tests and benchmarks
6. **Document** your findings
7. **Submit** required files

---

## 📚 Key Learning Outcomes

✅ Understanding Big O notation  
✅ Identifying performance bottlenecks  
✅ Applying optimization techniques  
✅ Using appropriate data structures  
✅ Writing comprehensive tests  
✅ Benchmarking and profiling  
✅ Using AI for code analysis  

---

## 🆘 Troubleshooting

### Port in Use
```bash
lsof -ti:5000 | xargs kill -9
lsof -ti:5001 | xargs kill -9
```

### Module Not Found
```bash
pip install flask pytest requests
```

### Tests Failing
```bash
# Clear data
curl -X DELETE http://localhost:5000/transactions
curl -X DELETE http://localhost:5001/transactions

# Run tests from project root
cd "/Users/shugile/Desktop/copilot /Cisco/"
pytest tests/ -v
```

---

## 📞 Support Resources

- **Big O Cheat Sheet**: https://www.bigocheatsheet.com/
- **Python Time Complexity**: https://wiki.python.org/moin/TimeComplexity
- **Flask Documentation**: https://flask.palletsprojects.com/
- **pytest Guide**: https://docs.pytest.org/

---

## 🎉 Success Criteria

Your completed assignment should have:
- ✅ Comprehensive analysis document
- ✅ All tests passing
- ✅ Performance improvements documented
- ✅ 5-10x speedup achieved
- ✅ Clear explanations of optimizations
- ✅ Well-organized code and tests

---

**Good luck with your assignment! 🚀**

For quick start, see `QUICKSTART.md`  
For full assignment details, see `ASSIGNMENT.md`  
For test documentation, see `tests/README.md`
