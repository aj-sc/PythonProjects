from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json
from flask import render_template

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

@app.route('/')
def index():
    return render_template('index.html')

# Generate realistic mockup data
def generate_sales_data():
    np.random.seed(42)  # For consistent data
    
    # Date range: last 12 months
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    
    products = ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Monitor', 'Keyboard', 'Mouse']
    regions = ['North America', 'Europe', 'Asia Pacific', 'Latin America']
    categories = ['Electronics', 'Accessories', 'Computers', 'Mobile']
    
    data = []
    
    for date in date_range:
        # More sales on weekdays, seasonal trends
        base_sales = 50 if date.weekday() < 5 else 30
        seasonal_factor = 1.2 if date.month in [11, 12] else 1.0  # Holiday boost
        daily_sales_count = int(base_sales * seasonal_factor * np.random.uniform(0.7, 1.3))
        
        for _ in range(daily_sales_count):
            product = np.random.choice(products)
            region = np.random.choice(regions)
            
            # Product-specific pricing
            price_ranges = {
                'Laptop': (800, 2000),
                'Smartphone': (300, 1200),
                'Tablet': (200, 800),
                'Headphones': (50, 300),
                'Monitor': (150, 600),
                'Keyboard': (30, 150),
                'Mouse': (20, 80)
            }
            
            min_price, max_price = price_ranges[product]
            price = np.random.uniform(min_price, max_price)
            quantity = np.random.choice([1, 1, 1, 1, 2, 2, 3], p=[0.4, 0.3, 0.15, 0.05, 0.05, 0.03, 0.02])
            
            # Assign category based on product
            if product in ['Laptop', 'Monitor']:
                category = 'Computers'
            elif product in ['Smartphone', 'Tablet']:
                category = 'Mobile'
            elif product in ['Headphones', 'Keyboard', 'Mouse']:
                category = 'Accessories'
            else:
                category = 'Electronics'
            
            data.append({
                'date': date.strftime('%Y-%m-%d'),
                'product': product,
                'category': category,
                'region': region,
                'price': round(price, 2),
                'quantity': quantity,
                'revenue': round(price * quantity, 2)
            })
    
    return pd.DataFrame(data)

# Generate data on startup
sales_df = generate_sales_data()

@app.route('/api/overview')
def get_overview():
    """Get high-level dashboard metrics"""
    total_revenue = sales_df['revenue'].sum()
    total_orders = len(sales_df)
    avg_order_value = sales_df['revenue'].mean()
    unique_products = sales_df['product'].nunique()
    
    # Month-over-month growth
    current_month = sales_df[sales_df['date'] >= (datetime.now() - timedelta(days=30))]
    previous_month = sales_df[
        (sales_df['date'] >= (datetime.now() - timedelta(days=60))) &
        (sales_df['date'] < (datetime.now() - timedelta(days=30)))
    ]
    
    mom_growth = 0
    if len(previous_month) > 0:
        current_revenue = current_month['revenue'].sum()
        previous_revenue = previous_month['revenue'].sum()
        mom_growth = ((current_revenue - previous_revenue) / previous_revenue) * 100 if previous_revenue > 0 else 0
    
    return jsonify({
        'total_revenue': round(total_revenue, 2),
        'total_orders': total_orders,
        'avg_order_value': round(avg_order_value, 2),
        'unique_products': unique_products,
        'mom_growth': round(mom_growth, 2)
    })

@app.route('/api/revenue-trend')
def get_revenue_trend():
    """Get monthly revenue trend"""
    monthly_data = sales_df.copy()
    monthly_data['date'] = pd.to_datetime(monthly_data['date'])
    monthly_data['month'] = monthly_data['date'].dt.to_period('M')
    
    trend = monthly_data.groupby('month')['revenue'].sum().reset_index()
    trend['month'] = trend['month'].astype(str)
    
    return jsonify({
        'labels': trend['month'].tolist(),
        'data': trend['revenue'].round(2).tolist()
    })

@app.route('/api/product-performance')
def get_product_performance():
    """Get product sales performance"""
    product_data = sales_df.groupby('product').agg({
        'revenue': 'sum',
        'quantity': 'sum'
    }).reset_index()
    
    product_data = product_data.sort_values('revenue', ascending=False)
    
    return jsonify({
        'products': product_data['product'].tolist(),
        'revenue': product_data['revenue'].round(2).tolist(),
        'quantity': product_data['quantity'].tolist()
    })

@app.route('/api/regional-breakdown')
def get_regional_breakdown():
    """Get sales by region"""
    regional_data = sales_df.groupby('region')['revenue'].sum().reset_index()
    regional_data = regional_data.sort_values('revenue', ascending=False)
    
    return jsonify({
        'regions': regional_data['region'].tolist(),
        'revenue': regional_data['revenue'].round(2).tolist()
    })

@app.route('/api/filtered-data')
def get_filtered_data():
    """Get filtered data based on parameters"""
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    category = request.args.get('category')
    region = request.args.get('region')
    
    filtered_df = sales_df.copy()
    
    if start_date:
        filtered_df = filtered_df[filtered_df['date'] >= start_date]
    if end_date:
        filtered_df = filtered_df[filtered_df['date'] <= end_date]
    if category and category != 'all':
        filtered_df = filtered_df[filtered_df['category'] == category]
    if region and region != 'all':
        filtered_df = filtered_df[filtered_df['region'] == region]
    
    # Return aggregated data
    daily_revenue = filtered_df.groupby('date')['revenue'].sum().reset_index()
    
    return jsonify({
        'daily_data': {
            'dates': daily_revenue['date'].tolist(),
            'revenue': daily_revenue['revenue'].round(2).tolist()
        },
        'summary': {
            'total_revenue': round(filtered_df['revenue'].sum(), 2),
            'total_orders': len(filtered_df),
            'avg_order_value': round(filtered_df['revenue'].mean(), 2) if len(filtered_df) > 0 else 0
        }
    })

@app.route('/api/categories')
def get_categories():
    """Get available categories"""
    categories = sales_df['category'].unique().tolist()
    return jsonify(categories)

@app.route('/api/regions')
def get_regions():
    """Get available regions"""
    regions = sales_df['region'].unique().tolist()
    return jsonify(regions)

if __name__ == '__main__':
    print(f"Generated {len(sales_df)} sales records")
    print("API Endpoints available:")
    print("- GET /api/overview")
    print("- GET /api/revenue-trend")
    print("- GET /api/product-performance")
    print("- GET /api/regional-breakdown")
    print("- GET /api/filtered-data")
    print("- GET /api/categories")
    print("- GET /api/regions")
    
    app.run(debug=True, port=5000)