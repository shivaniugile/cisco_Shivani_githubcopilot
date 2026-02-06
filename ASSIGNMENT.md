# Sales Analytics Flask API - Optimization Assignment

## 📋 Assignment Overview

You are tasked with **analyzing**, **optimizing**, and **benchmarking** a Sales Analytics Flask REST API. The API has intentional inefficiencies in both **time complexity** and **space complexity**.

### Learning Objectives
- Analyze time and space complexity of algorithms
- Identify performance bottlenecks
- Apply optimization techniques
- Use data structures effectively
- Benchmark and validate improvements
- Leverage Generative AI for code analysis and optimization

---

## 🎯 Assignment Tasks

### Task 1: Analysis (20 points)
Analyze the inefficient API (`sales_api_inefficient.py`) and document:

1. **Time Complexity Analysis**
   - For each endpoint, identify the time complexity
   - Explain why each operation is inefficient
   - Identify nested loops and redundant operations

2. **Space Complexity Analysis**
   - Identify excessive memory usage
   - Document redundant data structures
   - Analyze unnecessary copies and intermediate lists

3. **Create Analysis Document**
   - Use a table format
   - Document "Before" complexity for each function
   - Suggest "After" optimizations

**Deliverable**: `ANALYSIS.md` document

---

### Task 2: Optimization (40 points)

Optimize the following endpoints:

#### 2.1 Upload Transactions (`/transactions` POST)
**Current Issues:**
- O(n²) duplicate checking with nested loops
- No proper indexing

**Optimization Goals:**
- Reduce to O(n) using hash set
- Build indexes for fast queries

#### 2.2 Sales Per Product (`/sales/per-product` GET)
**Current Issues:**
- Multiple passes through data O(n*m)
- Bubble sort O(n²)
- No caching

**Optimization Goals:**
- Single pass aggregation O(n)
- Use built-in sort O(n log n)
- Implement caching

#### 2.3 Top Customers (`/customers/top` GET)
**Current Issues:**
- Multiple loops O(n*m)
- Manual sorting with selection sort O(n²)
- Unnecessary data copying

**Optimization Goals:**
- Single pass with dictionary O(n)
- Efficient sorting O(n log n)
- Eliminate unnecessary copies

#### 2.4 Filter Transactions (`/transactions/filter` GET)
**Current Issues:**
- Multiple filtering passes O(3n)
- No indexing
- String parsing on every request

**Optimization Goals:**
- Single pass filtering O(n)
- Use product index when applicable
- Combine all filters in one pass

#### 2.5 Analytics Summary (`/analytics/summary` GET)
**Current Issues:**
- Multiple complete passes O(5n)
- O(n²) unique counting

**Optimization Goals:**
- Single pass for all metrics O(n)
- Use sets for unique counting O(1)

**Deliverable**: `sales_api_optimized.py` (reference provided)

---

### Task 3: Testing (20 points)

Create comprehensive tests covering:

1. **Functional Tests**
   - Test all endpoints work correctly
   - Verify data accuracy
   - Test edge cases (empty data, duplicates, etc.)

2. **Performance Tests**
   - Compare execution time
   - Measure speedup achieved
   - Test with different data sizes (100, 500, 1000 records)

3. **Integration Tests**
   - Test complete workflows
   - Verify data consistency

**Deliverable**: `test_sales_api.py` (reference provided)

---

### Task 4: Benchmarking (10 points)

Run performance benchmarks comparing both versions:

1. **Upload Performance**
2. **Query Performance**
3. **Filtering Performance**
4. **Overall System Performance**

Document results with:
- Execution times (avg, min, max)
- Speedup ratios
- Percentage improvements

**Deliverable**: `BENCHMARK_RESULTS.md`

---

### Task 5: Documentation (10 points)

Create comprehensive documentation:

1. **README.md**
   - Setup instructions
   - API endpoints documentation
   - Usage examples

2. **OPTIMIZATION_REPORT.md**
   - Explain each optimization
   - Show before/after complexity
   - Justify design decisions

3. **Code Comments**
   - Document time/space complexity
   - Explain optimization techniques

**Deliverable**: Complete documentation set

---

## 📊 Complexity Analysis Reference

### Time Complexity Comparison

| Endpoint | Inefficient | Optimized | Improvement |
|----------|------------|-----------|-------------|
| Upload Transactions | O(n²) | O(n) | n times faster |
| Sales Per Product | O(n²) | O(n log n) | Significant |
| Top Customers | O(n²) | O(n log n) | Significant |
| Filter Transactions | O(3n) | O(n) or O(k) | 3x faster |
| Analytics Summary | O(5n²) | O(n) | Massive improvement |

### Space Complexity Comparison

| Component | Inefficient | Optimized | Notes |
|-----------|------------|-----------|-------|
| Storage | O(n) | O(n) | Same |
| Duplicate Check | O(1) | O(n) | Set for O(1) lookup |
| Indexes | None | O(n) | Trade space for time |
| Intermediate Lists | O(n) per query | O(1) | Eliminated copies |

---

## 🛠️ Setup Instructions

### Prerequisites
```bash
python >= 3.8
flask
pytest
requests
```

### Installation

1. **Install Dependencies**
```bash
cd /Users/shugile/Desktop/copilot\ /Cisco/
pip install flask pytest requests
```

2. **Run Inefficient API**
```bash
python sales_api_inefficient.py
# Runs on http://localhost:5000
```

3. **Run Optimized API** (in new terminal)
```bash
python sales_api_optimized.py
# Runs on http://localhost:5001
```

4. **Run Tests**
```bash
pytest test_sales_api.py -v
```

5. **Run Benchmark** (both APIs must be running)
```bash
python benchmark_sales_api.py
```

---

## 📝 API Endpoints

### 1. Upload Transactions
```http
POST /transactions
Content-Type: application/json

{
  "transactions": [
    {
      "transaction_id": "T001",
      "customer_id": "C001",
      "customer_name": "John Doe",
      "product_name": "Laptop",
      "amount": 1200.00,
      "quantity": 1,
      "date": "2026-01-15"
    }
  ]
}
```

### 2. Sales Per Product
```http
GET /sales/per-product

Response:
{
  "products": [
    {
      "product_name": "Laptop",
      "total_sales": 2400.00,
      "total_quantity": 2
    }
  ]
}
```

### 3. Top Customers
```http
GET /customers/top?limit=10

Response:
{
  "top_customers": [
    {
      "customer_id": "C001",
      "customer_name": "John Doe",
      "total_amount": 1275.00,
      "total_transactions": 2
    }
  ]
}
```

### 4. Filter Transactions
```http
GET /transactions/filter?start_date=2026-01-15&end_date=2026-01-20&product_name=Laptop
```

### 5. Analytics Summary
```http
GET /analytics/summary

Response:
{
  "total_sales": 2800.00,
  "total_transactions": 5,
  "unique_customers": 3,
  "unique_products": 4,
  "average_transaction": 560.00
}
```

---

## 🧪 Testing Examples

### Test Upload
```bash
curl -X POST http://localhost:5000/transactions \
  -H "Content-Type: application/json" \
  -d '{
    "transactions": [
      {
        "transaction_id": "T001",
        "customer_id": "C001",
        "customer_name": "John Doe",
        "product_name": "Laptop",
        "amount": 1200.00,
        "quantity": 1,
        "date": "2026-01-15"
      }
    ]
  }'
```

### Test Sales Per Product
```bash
curl http://localhost:5000/sales/per-product
```

### Test Top Customers
```bash
curl http://localhost:5000/customers/top?limit=5
```

---

## 🎓 Using Generative AI

### Recommended AI Prompts

1. **For Analysis:**
```
"Analyze this Python function and identify its time complexity.
Explain what makes it inefficient and suggest optimizations."
```

2. **For Optimization:**
```
"Optimize this function to reduce time complexity from O(n²) to O(n).
Use appropriate data structures and explain the changes."
```

3. **For Testing:**
```
"Generate pytest tests for this Flask endpoint including
positive tests, negative tests, and edge cases."
```

4. **For Documentation:**
```
"Document this optimized function with time/space complexity,
usage examples, and explain the optimization techniques used."
```

---

## 📈 Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| Analysis | 20 | Correct complexity identification, thorough documentation |
| Optimization | 40 | Working code, correct complexity, proper techniques |
| Testing | 20 | Comprehensive tests, edge cases, performance tests |
| Benchmarking | 10 | Accurate measurements, proper comparison |
| Documentation | 10 | Clear, complete, well-formatted |
| **Total** | **100** | |

---

## 💡 Optimization Techniques Used

1. **Hash Sets** - O(1) duplicate checking
2. **Dictionaries/Hash Maps** - O(1) lookups and aggregation
3. **Indexes** - Trade space for query speed
4. **Single-Pass Algorithms** - Reduce iterations
5. **Built-in Sorting** - O(n log n) vs O(n²) manual sort
6. **Set Operations** - Efficient unique counting
7. **Eliminate Copies** - Reduce memory usage
8. **Caching** - Avoid redundant calculations

---

## 🚀 Bonus Challenges (Optional)

1. **Add Database Support** - Replace in-memory storage with SQLite
2. **Implement Caching** - Use LRU cache for frequently accessed data
3. **Add Pagination** - Handle large result sets efficiently
4. **Create Dashboard** - Build a simple frontend to visualize data
5. **Add Authentication** - Implement API key authentication
6. **Docker Support** - Containerize both APIs

---

## 📚 Resources

- [Big O Notation](https://www.bigocheatsheet.com/)
- [Python Time Complexity](https://wiki.python.org/moin/TimeComplexity)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [pytest Documentation](https://docs.pytest.org/)

---

## ✅ Submission Checklist

- [ ] `ANALYSIS.md` - Complexity analysis document
- [ ] `sales_api_optimized.py` - Optimized API code
- [ ] `test_sales_api.py` - Comprehensive tests
- [ ] `BENCHMARK_RESULTS.md` - Performance comparison
- [ ] `README.md` - Setup and usage guide
- [ ] `OPTIMIZATION_REPORT.md` - Detailed explanations
- [ ] All tests passing
- [ ] Benchmark results documented

---

## 🎯 Expected Results

After optimization, you should see:
- **2-10x faster** query performance
- **90%+ reduction** in redundant operations
- **O(n log n)** or better for most operations
- **Proper** space-time tradeoffs

Good luck! 🚀
