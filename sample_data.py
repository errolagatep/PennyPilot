#!/usr/bin/env python3
"""
Generate sample data for the AI-Powered Budget Tracker
This script creates realistic sample transactions for testing and demonstration purposes.
"""

import pandas as pd
import random
from datetime import datetime, timedelta
from budget_tracker_web import BudgetTrackerWeb

def generate_sample_data():
    """Generate comprehensive sample data for the budget tracker"""
    
    print("🚀 Generating sample data for AI-Powered Budget Tracker...")
    
    # Initialize the tracker
    tracker = BudgetTrackerWeb()
    
    # Sample data categories and descriptions
    income_data = [
        {'description': 'Monthly Salary', 'amount': 50000, 'category': 'Income'},
        {'description': 'Freelance Work', 'amount': 15000, 'category': 'Income'},
        {'description': 'Investment Returns', 'amount': 5000, 'category': 'Income'},
        {'description': 'Side Business', 'amount': 8000, 'category': 'Income'},
    ]
    
    savings_data = [
        {'description': 'Emergency Fund Deposit', 'amount': 10000, 'category': 'Emergency Fund'},
        {'description': 'Retirement Contribution', 'amount': 5000, 'category': 'Retirement'},
        {'description': 'Investment Portfolio', 'amount': 8000, 'category': 'Investment'},
        {'description': 'Vacation Fund', 'amount': 3000, 'category': 'Vacation Fund'},
        {'description': 'House Down Payment', 'amount': 15000, 'category': 'House Down Payment'},
        {'description': '401k Contribution', 'amount': 7000, 'category': 'Retirement'},
        {'description': 'Emergency Buffer', 'amount': 2500, 'category': 'Emergency Fund'},
    ]
    
    expense_data = [
        # Housing
        {'description': 'Monthly Rent', 'amount': 18000, 'category': 'Housing'},
        {'description': 'Electricity Bill', 'amount': 3500, 'category': 'Utilities'},
        {'description': 'Water Bill', 'amount': 1200, 'category': 'Utilities'},
        {'description': 'Internet Bill', 'amount': 2500, 'category': 'Utilities'},
        
        # Food
        {'description': 'Grocery Shopping', 'amount': 4500, 'category': 'Food'},
        {'description': 'Restaurant Dinner', 'amount': 1800, 'category': 'Food'},
        {'description': 'Coffee Shop', 'amount': 250, 'category': 'Food'},
        {'description': 'Fast Food Lunch', 'amount': 450, 'category': 'Food'},
        {'description': 'Weekly Groceries', 'amount': 3200, 'category': 'Food'},
        
        # Transportation  
        {'description': 'Gas for Car', 'amount': 2500, 'category': 'Transportation'},
        {'description': 'Uber Ride', 'amount': 350, 'category': 'Transportation'},
        {'description': 'Bus Fare', 'amount': 150, 'category': 'Transportation'},
        {'description': 'Car Maintenance', 'amount': 5000, 'category': 'Transportation'},
        
        # Entertainment
        {'description': 'Movie Theater', 'amount': 800, 'category': 'Entertainment'},
        {'description': 'Netflix Subscription', 'amount': 550, 'category': 'Entertainment'},
        {'description': 'Spotify Premium', 'amount': 149, 'category': 'Entertainment'},
        {'description': 'Concert Tickets', 'amount': 3500, 'category': 'Entertainment'},
        {'description': 'Gaming Purchase', 'amount': 2000, 'category': 'Entertainment'},
        
        # Shopping
        {'description': 'Clothing Purchase', 'amount': 2500, 'category': 'Shopping'},
        {'description': 'Electronics Store', 'amount': 8000, 'category': 'Shopping'},
        {'description': 'Online Shopping', 'amount': 1200, 'category': 'Shopping'},
        {'description': 'Pharmacy', 'amount': 650, 'category': 'Healthcare'},
        
        # Healthcare
        {'description': 'Doctor Consultation', 'amount': 2000, 'category': 'Healthcare'},
        {'description': 'Dental Checkup', 'amount': 3500, 'category': 'Healthcare'},
        {'description': 'Medicine Purchase', 'amount': 800, 'category': 'Healthcare'},
        
        # Education
        {'description': 'Online Course', 'amount': 2500, 'category': 'Education'},
        {'description': 'Book Purchase', 'amount': 1200, 'category': 'Education'},
        
        # Other
        {'description': 'Bank Transfer Fee', 'amount': 50, 'category': 'Other'},
        {'description': 'ATM Fee', 'amount': 25, 'category': 'Other'},
        {'description': 'Gift Purchase', 'amount': 1500, 'category': 'Other'},
    ]
    
    # Generate transactions for the last 3 months
    start_date = datetime.now() - timedelta(days=90)
    transactions_added = 0
    
    # Add monthly income (3 months)
    for month_offset in range(3):
        month_date = start_date + timedelta(days=30 * month_offset)
        
        # Add regular monthly income
        for income in income_data[:2]:  # Salary and one other income source
            date_variation = random.randint(0, 5)  # Add some date variation
            transaction_date = month_date + timedelta(days=date_variation)
            
            # Add some variation to amounts
            amount_variation = random.uniform(0.9, 1.1)
            amount = int(income['amount'] * amount_variation)
            
            tracker.add_transaction(
                'income',
                amount,
                income['description'],
                income['category'],
                transaction_date.date()
            )
            transactions_added += 1
    
    # Add monthly savings (3 months)
    for month_offset in range(3):
        month_date = start_date + timedelta(days=30 * month_offset)
        
        # Add 2-3 savings transactions per month
        monthly_savings_count = random.randint(2, 3)
        for _ in range(monthly_savings_count):
            savings = random.choice(savings_data)
            date_variation = random.randint(0, 15)  # Spread throughout month
            transaction_date = month_date + timedelta(days=date_variation)
            
            # Add some variation to amounts
            amount_variation = random.uniform(0.8, 1.2)
            amount = int(savings['amount'] * amount_variation)
            
            tracker.add_transaction(
                'savings',
                amount,
                savings['description'],
                savings['category'],
                transaction_date.date()
            )
            transactions_added += 1
    
    # Add random expenses throughout the period
    current_date = start_date
    while current_date <= datetime.now():
        # Add 1-4 expenses per day
        daily_transactions = random.randint(1, 4)
        
        for _ in range(daily_transactions):
            expense = random.choice(expense_data)
            
            # Add variation to amounts (70% to 130% of base amount)
            amount_variation = random.uniform(0.7, 1.3)
            amount = int(expense['amount'] * amount_variation)
            
            # Skip if amount becomes too small
            if amount < 10:
                continue
                
            tracker.add_transaction(
                'expense',
                amount,
                expense['description'],
                expense['category'],
                current_date.date()
            )
            transactions_added += 1
        
        # Move to next day (with some random skips)
        skip_days = random.choices([1, 2, 3], weights=[70, 20, 10])[0]
        current_date += timedelta(days=skip_days)
    
    # Create sample user profile
    sample_profile = {
        'monthly_income': 65000,
        'savings_goal': 20000,
        'expense_limit': 45000,
        'financial_goals': 'Build emergency fund of ₱200,000, Save for house down payment, Pay off credit card debt',
        'budget_style': '50/30/20 Rule (Needs/Wants/Savings)',
        'setup_completed': True,
        'created_date': datetime.now().strftime('%Y-%m-%d')
    }
    
    tracker.save_user_profile(sample_profile)
    
    print(f"✅ Sample data generation completed!")
    print(f"📊 Generated {transactions_added} transactions")
    print(f"👤 Created user profile with financial goals")
    print(f"📅 Data spans from {start_date.strftime('%Y-%m-%d')} to {datetime.now().strftime('%Y-%m-%d')}")
    print(f"💾 Data saved to: {tracker.excel_file}")
    print(f"👤 Profile saved to: {tracker.user_profile_file}")
    print("\n🚀 You can now run the budget tracker and explore all features!")
    print("💡 Run: streamlit run streamlit_app.py")

def main():
    """Main function to run sample data generation"""
    try:
        generate_sample_data()
    except Exception as e:
        print(f"❌ Error generating sample data: {str(e)}")
        print("💡 Make sure all dependencies are installed: pip install -r requirements.txt")

if __name__ == "__main__":
    main()