"""
Test Suite for Sales Analytics API
===================================

Tests both inefficient and optimized versions
Includes performance benchmarking
"""

import pytest
import json
import time
from sales_api_inefficient import app as inefficient_app
from sales_api_optimized import app as optimized_app

# Sample test data
SAMPLE_TRANSACTIONS = {
    "transactions": [
        {
            "transaction_id": "T001",
            "customer_id": "C001",
            "customer_name": "John Doe",
            "product_name": "Laptop",
            "amount": 1200.00,
            "quantity": 1,
            "date": "2026-01-15"
        },
        {
            "transaction_id": "T002",
            "customer_id": "C002",
            "customer_name": "Jane Smith",
            "product_name": "Mouse",
            "amount": 25.00,
            "quantity": 2,
            "date": "2026-01-16"
        },
        {
            "transaction_id": "T003",
            "customer_id": "C001",
            "customer_name": "John Doe",
            "product_name": "Keyboard",
            "amount": 75.00,
            "quantity": 1,
            "date": "2026-01-17"
        },
        {
            "transaction_id": "T004",
            "customer_id": "C003",
            "customer_name": "Bob Johnson",
            "product_name": "Laptop",
            "amount": 1200.00,
            "quantity": 1,
            "date": "2026-01-18"
        },
        {
            "transaction_id": "T005",
            "customer_id": "C002",
            "customer_name": "Jane Smith",
            "product_name": "Monitor",
            "amount": 300.00,
            "quantity": 1,
            "date": "2026-01-19"
        }
    ]
}


@pytest.fixture
def inefficient_client():
    """Create test client for inefficient API"""
    inefficient_app.config['TESTING'] = True
    with inefficient_app.test_client() as client:
        yield client
    # Cleanup
    client.delete('/transactions')


@pytest.fixture
def optimized_client():
    """Create test client for optimized API"""
    optimized_app.config['TESTING'] = True
    with optimized_app.test_client() as client:
        yield client
    # Cleanup
    client.delete('/transactions')


class TestUploadTransactions:
    """Test transaction upload functionality"""
    
    def test_upload_transactions_inefficient(self, inefficient_client):
        """Test upload with inefficient API"""
        response = inefficient_client.post(
            '/transactions',
            data=json.dumps(SAMPLE_TRANSACTIONS),
            content_type='application/json'
        )
        assert response.status_code == 201
        data = json.loads(response.data)
        assert data['total_count'] == 5
    
    def test_upload_transactions_optimized(self, optimized_client):
        """Test upload with optimized API"""
        response = optimized_client.post(
            '/transactions',
            data=json.dumps(SAMPLE_TRANSACTIONS),
            content_type='application/json'
        )
        assert response.status_code == 201
        data = json.loads(response.data)
        assert data['total_count'] == 5
        assert data['added'] == 5
    
    def test_upload_duplicate_transactions(self, optimized_client):
        """Test that duplicates are handled correctly"""
        # Upload once
        optimized_client.post(
            '/transactions',
            data=json.dumps(SAMPLE_TRANSACTIONS),
            content_type='application/json'
        )
        
        # Upload again (should skip duplicates)
        response = optimized_client.post(
            '/transactions',
            data=json.dumps(SAMPLE_TRANSACTIONS),
            content_type='application/json'
        )
        data = json.loads(response.data)
        assert data['added'] == 0  # No new transactions
        assert data['total_count'] == 5  # Still 5 total


class TestSalesPerProduct:
    """Test sales per product endpoint"""
    
    def test_sales_per_product_inefficient(self, inefficient_client):
        """Test product sales calculation - inefficient"""
        inefficient_client.post(
            '/transactions',
            data=json.dumps(SAMPLE_TRANSACTIONS),
            content_type='application/json'
        )
        
        response = inefficient_client.get('/sales/per-product')
        assert response.status_code == 200
        data = json.loads(response.data)
        
        products = data['products']
        assert len(products) == 4  # 4 unique products
        
        # Check Laptop is highest
        assert products[0]['product_name'] == 'Laptop'
        assert products[0]['total_sales'] == 2400.00
    
    def test_sales_per_product_optimized(self, optimized_client):
        """Test product sales calculation - optimized"""
        optimized_client.post(
            '/transactions',
            data=json.dumps(SAMPLE_TRANSACTIONS),
            content_type='application/json'
        )
        
        response = optimized_client.get('/sales/per-product')
        assert response.status_code == 200
        data = json.loads(response.data)
        
        products = data['products']
        assert len(products) == 4
        assert products[0]['product_name'] == 'Laptop'
        assert products[0]['total_sales'] == 2400.00


class TestTopCustomers:
    """Test top customers endpoint"""
    
    def test_top_customers_inefficient(self, inefficient_client):
        """Test top customers - inefficient"""
        inefficient_client.post(
            '/transactions',
            data=json.dumps(SAMPLE_TRANSACTIONS),
            content_type='application/json'
        )
        
        response = inefficient_client.get('/customers/top?limit=2')
        assert response.status_code == 200
        data = json.loads(response.data)
        
        customers = data['top_customers']
        assert len(customers) == 2
        
        # John Doe should be first (1200 + 75 = 1275)
        assert customers[0]['customer_id'] == 'C001'
        assert customers[0]['total_amount'] == 1275.00
    
    def test_top_customers_optimized(self, optimized_client):
        """Test top customers - optimized"""
        optimized_client.post(
            '/transactions',
            data=json.dumps(SAMPLE_TRANSACTIONS),
            content_type='application/json'
        )
        
        response = optimized_client.get('/customers/top?limit=2')
        assert response.status_code == 200
        data = json.loads(response.data)
        
        customers = data['top_customers']
        assert len(customers) == 2
        assert customers[0]['customer_id'] == 'C001'
        assert customers[0]['total_amount'] == 1275.00


class TestFilterTransactions:
    """Test transaction filtering"""
    
    def test_filter_by_product(self, optimized_client):
        """Test filtering by product name"""
        optimized_client.post(
            '/transactions',
            data=json.dumps(SAMPLE_TRANSACTIONS),
            content_type='application/json'
        )
        
        response = optimized_client.get('/transactions/filter?product_name=Laptop')
        assert response.status_code == 200
        data = json.loads(response.data)
        
        assert data['count'] == 2
        assert all(t['product_name'] == 'Laptop' for t in data['transactions'])
    
    def test_filter_by_date_range(self, optimized_client):
        """Test filtering by date range"""
        optimized_client.post(
            '/transactions',
            data=json.dumps(SAMPLE_TRANSACTIONS),
            content_type='application/json'
        )
        
        response = optimized_client.get(
            '/transactions/filter?start_date=2026-01-16&end_date=2026-01-18'
        )
        assert response.status_code == 200
        data = json.loads(response.data)
        
        assert data['count'] == 3


class TestAnalyticsSummary:
    """Test analytics summary endpoint"""
    
    def test_summary_inefficient(self, inefficient_client):
        """Test summary - inefficient"""
        inefficient_client.post(
            '/transactions',
            data=json.dumps(SAMPLE_TRANSACTIONS),
            content_type='application/json'
        )
        
        response = inefficient_client.get('/analytics/summary')
        assert response.status_code == 200
        data = json.loads(response.data)
        
        assert data['total_sales'] == 2800.00
        assert data['total_transactions'] == 5
        assert data['unique_customers'] == 3
        assert data['unique_products'] == 4
    
    def test_summary_optimized(self, optimized_client):
        """Test summary - optimized"""
        optimized_client.post(
            '/transactions',
            data=json.dumps(SAMPLE_TRANSACTIONS),
            content_type='application/json'
        )
        
        response = optimized_client.get('/analytics/summary')
        assert response.status_code == 200
        data = json.loads(response.data)
        
        assert data['total_sales'] == 2800.00
        assert data['total_transactions'] == 5
        assert data['unique_customers'] == 3
        assert data['unique_products'] == 4


class TestPerformanceBenchmark:
    """Performance comparison tests"""
    
    def generate_large_dataset(self, size=1000):
        """Generate large dataset for performance testing"""
        transactions = []
        for i in range(size):
            transactions.append({
                "transaction_id": f"T{i:06d}",
                "customer_id": f"C{i % 100:04d}",
                "customer_name": f"Customer {i % 100}",
                "product_name": f"Product {i % 50}",
                "amount": 100.00 + (i % 1000),
                "quantity": 1 + (i % 5),
                "date": f"2026-01-{(i % 28) + 1:02d}"
            })
        return {"transactions": transactions}
    
    def test_upload_performance(self, inefficient_client, optimized_client):
        """Compare upload performance"""
        large_dataset = self.generate_large_dataset(1000)
        
        # Test inefficient version
        start = time.time()
        inefficient_client.post(
            '/transactions',
            data=json.dumps(large_dataset),
            content_type='application/json'
        )
        inefficient_time = time.time() - start
        
        # Test optimized version
        start = time.time()
        optimized_client.post(
            '/transactions',
            data=json.dumps(large_dataset),
            content_type='application/json'
        )
        optimized_time = time.time() - start
        
        print(f"\nUpload Performance (1000 transactions):")
        print(f"  Inefficient: {inefficient_time:.4f}s")
        print(f"  Optimized:   {optimized_time:.4f}s")
        print(f"  Speedup:     {inefficient_time/optimized_time:.2f}x")
        
        # Optimized should be faster
        assert optimized_time < inefficient_time
    
    def test_sales_calculation_performance(self, inefficient_client, optimized_client):
        """Compare sales calculation performance"""
        large_dataset = self.generate_large_dataset(1000)
        
        # Upload data to both
        inefficient_client.post(
            '/transactions',
            data=json.dumps(large_dataset),
            content_type='application/json'
        )
        optimized_client.post(
            '/transactions',
            data=json.dumps(large_dataset),
            content_type='application/json'
        )
        
        # Test inefficient version
        start = time.time()
        inefficient_client.get('/sales/per-product')
        inefficient_time = time.time() - start
        
        # Test optimized version
        start = time.time()
        optimized_client.get('/sales/per-product')
        optimized_time = time.time() - start
        
        print(f"\nSales Calculation Performance:")
        print(f"  Inefficient: {inefficient_time:.4f}s")
        print(f"  Optimized:   {optimized_time:.4f}s")
        print(f"  Speedup:     {inefficient_time/optimized_time:.2f}x")
        
        assert optimized_time < inefficient_time


if __name__ == "__main__":
    pytest.main([__file__, '-v', '--tb=short'])
