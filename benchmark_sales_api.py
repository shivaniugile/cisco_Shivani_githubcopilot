"""
Performance Benchmarking Script
================================

Compare performance between inefficient and optimized APIs
"""

import requests
import time
import json
import random
from datetime import datetime, timedelta


def generate_transactions(count=1000):
    """Generate random transaction data"""
    transactions = []
    start_date = datetime(2026, 1, 1)
    
    products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones", 
                "Webcam", "Speaker", "USB Drive", "HDMI Cable", "Charger"]
    
    for i in range(count):
        date = start_date + timedelta(days=random.randint(0, 30))
        transactions.append({
            "transaction_id": f"T{i:06d}",
            "customer_id": f"C{random.randint(1, 100):04d}",
            "customer_name": f"Customer {random.randint(1, 100)}",
            "product_name": random.choice(products),
            "amount": round(random.uniform(10, 2000), 2),
            "quantity": random.randint(1, 5),
            "date": date.strftime("%Y-%m-%d")
        })
    
    return {"transactions": transactions}


def benchmark_endpoint(url, method='GET', data=None, iterations=5):
    """Benchmark an API endpoint"""
    times = []
    
    for _ in range(iterations):
        start = time.time()
        if method == 'POST':
            response = requests.post(url, json=data)
        else:
            response = requests.get(url)
        end = time.time()
        
        if response.status_code not in [200, 201]:
            print(f"Error: {response.status_code}")
            return None
        
        times.append(end - start)
    
    avg_time = sum(times) / len(times)
    min_time = min(times)
    max_time = max(times)
    
    return {
        'avg': avg_time,
        'min': min_time,
        'max': max_time,
        'times': times
    }


def run_benchmark():
    """Run comprehensive benchmark"""
    
    INEFFICIENT_BASE = "http://localhost:5000"
    OPTIMIZED_BASE = "http://localhost:5001"
    
    print("=" * 80)
    print("SALES API PERFORMANCE BENCHMARK")
    print("=" * 80)
    
    # Generate test data
    print("\nGenerating test data...")
    small_dataset = generate_transactions(100)
    medium_dataset = generate_transactions(500)
    large_dataset = generate_transactions(1000)
    
    # Clear existing data
    print("Clearing existing data...")
    requests.delete(f"{INEFFICIENT_BASE}/transactions")
    requests.delete(f"{OPTIMIZED_BASE}/transactions")
    
    # Benchmark 1: Upload Transactions
    print("\n" + "-" * 80)
    print("TEST 1: Upload Transactions (1000 records)")
    print("-" * 80)
    
    print("Testing INEFFICIENT API...")
    ineff_upload = benchmark_endpoint(
        f"{INEFFICIENT_BASE}/transactions",
        method='POST',
        data=large_dataset,
        iterations=1  # Only once for upload
    )
    
    print("Testing OPTIMIZED API...")
    opt_upload = benchmark_endpoint(
        f"{OPTIMIZED_BASE}/transactions",
        method='POST',
        data=large_dataset,
        iterations=1
    )
    
    print(f"\nResults:")
    print(f"  Inefficient: {ineff_upload['avg']:.4f}s")
    print(f"  Optimized:   {opt_upload['avg']:.4f}s")
    print(f"  Speedup:     {ineff_upload['avg']/opt_upload['avg']:.2f}x")
    
    # Benchmark 2: Sales Per Product
    print("\n" + "-" * 80)
    print("TEST 2: Calculate Sales Per Product")
    print("-" * 80)
    
    print("Testing INEFFICIENT API...")
    ineff_sales = benchmark_endpoint(
        f"{INEFFICIENT_BASE}/sales/per-product",
        iterations=5
    )
    
    print("Testing OPTIMIZED API...")
    opt_sales = benchmark_endpoint(
        f"{OPTIMIZED_BASE}/sales/per-product",
        iterations=5
    )
    
    print(f"\nResults (avg of 5 runs):")
    print(f"  Inefficient: {ineff_sales['avg']:.4f}s (min: {ineff_sales['min']:.4f}s, max: {ineff_sales['max']:.4f}s)")
    print(f"  Optimized:   {opt_sales['avg']:.4f}s (min: {opt_sales['min']:.4f}s, max: {opt_sales['max']:.4f}s)")
    print(f"  Speedup:     {ineff_sales['avg']/opt_sales['avg']:.2f}x")
    
    # Benchmark 3: Top Customers
    print("\n" + "-" * 80)
    print("TEST 3: Get Top Customers")
    print("-" * 80)
    
    print("Testing INEFFICIENT API...")
    ineff_customers = benchmark_endpoint(
        f"{INEFFICIENT_BASE}/customers/top?limit=10",
        iterations=5
    )
    
    print("Testing OPTIMIZED API...")
    opt_customers = benchmark_endpoint(
        f"{OPTIMIZED_BASE}/customers/top?limit=10",
        iterations=5
    )
    
    print(f"\nResults (avg of 5 runs):")
    print(f"  Inefficient: {ineff_customers['avg']:.4f}s")
    print(f"  Optimized:   {opt_customers['avg']:.4f}s")
    print(f"  Speedup:     {ineff_customers['avg']/opt_customers['avg']:.2f}x")
    
    # Benchmark 4: Filter Transactions
    print("\n" + "-" * 80)
    print("TEST 4: Filter Transactions")
    print("-" * 80)
    
    print("Testing INEFFICIENT API...")
    ineff_filter = benchmark_endpoint(
        f"{INEFFICIENT_BASE}/transactions/filter?product_name=Laptop",
        iterations=5
    )
    
    print("Testing OPTIMIZED API...")
    opt_filter = benchmark_endpoint(
        f"{OPTIMIZED_BASE}/transactions/filter?product_name=Laptop",
        iterations=5
    )
    
    print(f"\nResults (avg of 5 runs):")
    print(f"  Inefficient: {ineff_filter['avg']:.4f}s")
    print(f"  Optimized:   {opt_filter['avg']:.4f}s")
    print(f"  Speedup:     {ineff_filter['avg']/opt_filter['avg']:.2f}x")
    
    # Benchmark 5: Analytics Summary
    print("\n" + "-" * 80)
    print("TEST 5: Analytics Summary")
    print("-" * 80)
    
    print("Testing INEFFICIENT API...")
    ineff_summary = benchmark_endpoint(
        f"{INEFFICIENT_BASE}/analytics/summary",
        iterations=5
    )
    
    print("Testing OPTIMIZED API...")
    opt_summary = benchmark_endpoint(
        f"{OPTIMIZED_BASE}/analytics/summary",
        iterations=5
    )
    
    print(f"\nResults (avg of 5 runs):")
    print(f"  Inefficient: {ineff_summary['avg']:.4f}s")
    print(f"  Optimized:   {opt_summary['avg']:.4f}s")
    print(f"  Speedup:     {ineff_summary['avg']/opt_summary['avg']:.2f}x")
    
    # Overall Summary
    print("\n" + "=" * 80)
    print("OVERALL PERFORMANCE SUMMARY")
    print("=" * 80)
    
    total_ineff = (ineff_upload['avg'] + ineff_sales['avg'] + 
                   ineff_customers['avg'] + ineff_filter['avg'] + 
                   ineff_summary['avg'])
    
    total_opt = (opt_upload['avg'] + opt_sales['avg'] + 
                 opt_customers['avg'] + opt_filter['avg'] + 
                 opt_summary['avg'])
    
    print(f"\nTotal time for all operations:")
    print(f"  Inefficient: {total_ineff:.4f}s")
    print(f"  Optimized:   {total_opt:.4f}s")
    print(f"  Overall Speedup: {total_ineff/total_opt:.2f}x")
    print(f"  Time Saved: {(total_ineff - total_opt):.4f}s ({((total_ineff - total_opt)/total_ineff)*100:.1f}%)")
    
    print("\n" + "=" * 80)


if __name__ == "__main__":
    print("\nMake sure both APIs are running:")
    print("  Inefficient: python sales_api_inefficient.py (port 5000)")
    print("  Optimized:   python sales_api_optimized.py (port 5001)")
    print("\nPress Enter to start benchmark...")
    input()
    
    try:
        run_benchmark()
    except requests.exceptions.ConnectionError:
        print("\nError: Could not connect to APIs.")
        print("Make sure both servers are running on ports 5000 and 5001")
