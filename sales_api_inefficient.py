"""
Sales Analytics Flask API - INEFFICIENT VERSION
================================================

This is an intentionally inefficient implementation with:
- Poor time complexity O(n²) or worse
- Excessive space usage
- Redundant computations
- No caching
- Inefficient data structures

YOUR TASK: Analyze and optimize this code!
"""

from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# Global storage (inefficient - should use database)
transactions = []


@app.route('/transactions', methods=['POST'])
def upload_transactions():
    """
    Upload sales transactions
    
    INEFFICIENCIES:
    - Stores entire dataset in memory (Space: O(n))
    - No validation before storing
    - Duplicates allowed
    - Linear search on every check O(n)
    """
    data = request.get_json()
    
    if not data or 'transactions' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    
    new_transactions = data['transactions']
    
    # INEFFICIENT: Check for duplicates with nested loops O(n²)
    for new_trans in new_transactions:
        is_duplicate = False
        for existing_trans in transactions:
            if (existing_trans['transaction_id'] == new_trans['transaction_id']):
                is_duplicate = True
                break
        
        if not is_duplicate:
            transactions.append(new_trans)
    
    return jsonify({
        'message': 'Transactions uploaded',
        'total_count': len(transactions)
    }), 201


@app.route('/sales/per-product', methods=['GET'])
def calculate_sales_per_product():
    """
    Calculate total sales per product
    
    INEFFICIENCIES:
    - Recalculates from scratch every time O(n)
    - No caching
    - Multiple passes through data
    - Creates unnecessary intermediate lists
    """
    if not transactions:
        return jsonify({'error': 'No transactions available'}), 404
    
    # INEFFICIENT: Multiple loops instead of single pass
    products = []
    
    # First loop: Get all unique products O(n²)
    for trans in transactions:
        product_name = trans.get('product_name')
        if product_name not in products:
            products.append(product_name)
    
    # Second loop: Calculate sales for each product O(n*m)
    result = []
    for product in products:
        total_sales = 0
        total_quantity = 0
        
        # Third nested loop: Sum up sales O(n)
        for trans in transactions:
            if trans.get('product_name') == product:
                total_sales += trans.get('amount', 0)
                total_quantity += trans.get('quantity', 1)
        
        result.append({
            'product_name': product,
            'total_sales': total_sales,
            'total_quantity': total_quantity
        })
    
    # INEFFICIENT: Bubble sort O(n²) instead of built-in sort
    n = len(result)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j]['total_sales'] < result[j + 1]['total_sales']:
                result[j], result[j + 1] = result[j + 1], result[j]
    
    return jsonify({'products': result}), 200


@app.route('/customers/top', methods=['GET'])
def get_top_customers():
    """
    Get top N customers by total purchase amount
    
    INEFFICIENCIES:
    - No caching
    - Inefficient sorting O(n²)
    - Multiple passes through data
    - Creates deep copies unnecessarily
    """
    limit = request.args.get('limit', 10, type=int)
    
    if not transactions:
        return jsonify({'error': 'No transactions available'}), 404
    
    # INEFFICIENT: Multiple loops and unnecessary copying
    customers = []
    
    # Loop 1: Extract all customer IDs O(n)
    customer_ids = []
    for trans in transactions:
        customer_id = trans.get('customer_id')
        if customer_id not in customer_ids:
            customer_ids.append(customer_id)
    
    # Loop 2: Calculate totals for each customer O(n*m)
    for customer_id in customer_ids:
        total_amount = 0
        total_transactions = 0
        customer_name = ""
        
        # Loop 3: Sum transactions for this customer O(n)
        for trans in transactions:
            if trans.get('customer_id') == customer_id:
                total_amount += trans.get('amount', 0)
                total_transactions += 1
                customer_name = trans.get('customer_name', f"Customer_{customer_id}")
        
        customers.append({
            'customer_id': customer_id,
            'customer_name': customer_name,
            'total_amount': total_amount,
            'total_transactions': total_transactions
        })
    
    # INEFFICIENT: Manual sorting with nested loops O(n²)
    sorted_customers = []
    remaining = customers.copy()  # Unnecessary copy
    
    while len(remaining) > 0:
        max_customer = remaining[0]
        max_index = 0
        
        for i in range(len(remaining)):
            if remaining[i]['total_amount'] > max_customer['total_amount']:
                max_customer = remaining[i]
                max_index = i
        
        sorted_customers.append(max_customer)
        remaining.pop(max_index)
    
    # Return only top N
    top_customers = sorted_customers[:limit]
    
    return jsonify({'top_customers': top_customers}), 200


@app.route('/transactions/filter', methods=['GET'])
def filter_transactions():
    """
    Filter transactions by date range and product
    
    INEFFICIENCIES:
    - Linear search O(n) on every request
    - No indexing
    - String parsing on every filter
    - Creates multiple intermediate lists
    """
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    product_name = request.args.get('product_name')
    
    if not transactions:
        return jsonify({'error': 'No transactions available'}), 404
    
    # INEFFICIENT: Multiple filtering passes instead of single pass
    filtered = transactions.copy()  # Unnecessary copy
    
    # Filter by start date O(n)
    if start_date:
        temp_filtered = []
        for trans in filtered:
            trans_date = trans.get('date', '')
            if trans_date >= start_date:
                temp_filtered.append(trans)
        filtered = temp_filtered
    
    # Filter by end date O(n)
    if end_date:
        temp_filtered = []
        for trans in filtered:
            trans_date = trans.get('date', '')
            if trans_date <= end_date:
                temp_filtered.append(trans)
        filtered = temp_filtered
    
    # Filter by product O(n)
    if product_name:
        temp_filtered = []
        for trans in filtered:
            if trans.get('product_name') == product_name:
                temp_filtered.append(trans)
        filtered = temp_filtered
    
    # INEFFICIENT: Convert to JSON and back for no reason
    json_str = json.dumps(filtered)
    result = json.loads(json_str)
    
    return jsonify({
        'transactions': result,
        'count': len(result)
    }), 200


@app.route('/analytics/summary', methods=['GET'])
def get_summary():
    """
    Get overall analytics summary
    
    INEFFICIENCIES:
    - Recalculates everything from scratch
    - No memoization
    - Multiple complete passes through data O(n*m)
    """
    if not transactions:
        return jsonify({'error': 'No transactions available'}), 404
    
    # Calculate total sales - O(n)
    total_sales = 0
    for trans in transactions:
        total_sales += trans.get('amount', 0)
    
    # Count unique customers - O(n²)
    unique_customers = []
    for trans in transactions:
        customer_id = trans.get('customer_id')
        if customer_id not in unique_customers:
            unique_customers.append(customer_id)
    
    # Count unique products - O(n²)
    unique_products = []
    for trans in transactions:
        product_name = trans.get('product_name')
        if product_name not in unique_products:
            unique_products.append(product_name)
    
    # Calculate average transaction - O(n)
    avg_transaction = 0
    if len(transactions) > 0:
        sum_amount = 0
        for trans in transactions:
            sum_amount += trans.get('amount', 0)
        avg_transaction = sum_amount / len(transactions)
    
    return jsonify({
        'total_sales': total_sales,
        'total_transactions': len(transactions),
        'unique_customers': len(unique_customers),
        'unique_products': len(unique_products),
        'average_transaction': avg_transaction
    }), 200


@app.route('/transactions', methods=['GET'])
def get_all_transactions():
    """Return all transactions (inefficient for large datasets)"""
    return jsonify({'transactions': transactions, 'count': len(transactions)}), 200


@app.route('/transactions', methods=['DELETE'])
def clear_transactions():
    """Clear all transactions"""
    global transactions
    count = len(transactions)
    transactions = []
    return jsonify({'message': f'Cleared {count} transactions'}), 200


if __name__ == '__main__':
    print("\n" + "="*60)
    print("INEFFICIENT SALES API - Running on http://localhost:5000")
    print("="*60)
    print("\nThis version has intentional inefficiencies:")
    print("- Time Complexity: O(n²) or worse")
    print("- Space Complexity: Excessive memory usage")
    print("- No caching or indexing")
    print("\nYour task: Analyze and optimize!")
    print("="*60 + "\n")
    
    app.run(debug=True, port=5000)
