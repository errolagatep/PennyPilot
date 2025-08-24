import streamlit as st
import pandas as pd
from datetime import datetime, date
from budget_tracker_web import BudgetTrackerWeb
import os
from io import BytesIO

# Page configuration
st.set_page_config(
    page_title="AI-Powered Budget Tracker",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize the budget tracker
@st.cache_resource
def get_tracker():
    return BudgetTrackerWeb()

tracker = get_tracker()

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1.5rem;
        font-weight: bold;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .success-message {
        padding: 0.8rem;
        background-color: #d4edda;
        border-color: #c3e6cb;
        color: #155724;
        border-radius: 0.25rem;
        font-size: 0.9rem;
    }
    .error-message {
        padding: 0.8rem;
        background-color: #f8d7da;
        border-color: #f5c6cb;
        color: #721c24;
        border-radius: 0.25rem;
        font-size: 0.9rem;
    }
    
    /* Improve sidebar styling */
    .css-1d391kg {
        padding-top: 1rem;
    }
    
    /* Better button spacing in sidebar */
    .stSidebar .stButton > button {
        width: 100%;
        margin-bottom: 0.5rem;
        border-radius: 0.5rem;
        font-weight: 500;
    }
    
    /* Improve metric display */
    .css-1r6slb0 {
        background-color: #f8f9fa;
        padding: 0.75rem;
        border-radius: 0.5rem;
        border: 1px solid #e9ecef;
    }
    
    /* Better form styling */
    .stForm {
        border: 1px solid #e9ecef;
        padding: 1.5rem;
        border-radius: 0.75rem;
        background-color: #fefefe;
    }
    
    /* Improve expander styling for transactions */
    .streamlit-expanderHeader {
        font-size: 0.95rem;
        font-weight: 500;
    }
    
    /* Better dataframe display */
    .stDataFrame {
        border-radius: 0.5rem;
    }
    
    /* Responsive text sizes */
    @media (max-width: 768px) {
        .main-header {
            font-size: 1.8rem;
        }
        .css-1r6slb0 {
            padding: 0.5rem;
        }
    }
    
    /* Improve caption styling */
    .css-183lzff {
        color: #6c757d;
        font-style: italic;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">💰 AI-Powered Budget Tracker</h1>', unsafe_allow_html=True)

# Check if first-time user
if tracker.is_first_time_user():
    st.session_state.current_page = "Setup"

# Sidebar Navigation
st.sidebar.title("🧭 Navigation")
st.sidebar.markdown("### Choose a section:")

# Navigation as vertical list of buttons
setup_btn = st.sidebar.button("⚙️ Setup Profile", use_container_width=True)
dashboard_btn = st.sidebar.button("📊 Dashboard", use_container_width=True)
add_btn = st.sidebar.button("➕ Add Transaction", use_container_width=True)
ai_btn = st.sidebar.button("🤖 AI Analysis", use_container_width=True)
data_btn = st.sidebar.button("📁 Data Management", use_container_width=True)

# Add data view selector in sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### 📅 Data View")
data_view = st.sidebar.selectbox(
    "Select time period:",
    ["All Time", "Current Month", "Current Year"],
    key="data_view_selector"
)

# Show user profile info in sidebar if setup is complete
if not tracker.is_first_time_user():
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 👤 Profile Overview")
    profile = tracker.load_user_profile()
    if profile.get('monthly_income', 0) > 0:
        st.sidebar.write(f"💰 Monthly Income: ₱{profile['monthly_income']:,.2f}")
    if profile.get('savings_goal', 0) > 0:
        st.sidebar.write(f"🎯 Savings Goal: ₱{profile['savings_goal']:,.2f}")
    st.sidebar.caption("Go to Setup to update your profile")

# Determine which page to show based on button clicks or session state
if 'current_page' not in st.session_state:
    if tracker.is_first_time_user():
        st.session_state.current_page = "Setup"
    else:
        st.session_state.current_page = "Dashboard"

if setup_btn:
    st.session_state.current_page = "Setup"
elif dashboard_btn:
    st.session_state.current_page = "Dashboard"
elif add_btn:
    st.session_state.current_page = "Add Transaction"
elif ai_btn:
    st.session_state.current_page = "AI Analysis"
elif data_btn:
    st.session_state.current_page = "Data Management"

page = st.session_state.current_page

# Show current page
st.sidebar.markdown(f"**Current Page:** {page}")

# Load data with appropriate filter based on selected view
date_filter_map = {
    "All Time": None,
    "Current Month": "current_month",
    "Current Year": "current_year"
}
df = tracker.load_data(date_filter_map.get(data_view))

if page == "Setup":
    st.header("⚙️ First-Time Setup")
    st.markdown("### Welcome to your AI-Powered Budget Tracker!")
    st.markdown("Let's set up your financial profile to get personalized insights.")
    
    with st.form("user_setup"):
        st.subheader("💰 Financial Information")
        
        col1, col2 = st.columns(2)
        
        with col1:
            monthly_income = st.number_input(
                "Monthly Income (₱)",
                min_value=0.0,
                step=1000.0,
                help="Your average monthly income before expenses"
            )
            
            savings_goal = st.number_input(
                "Monthly Savings Goal (₱)",
                min_value=0.0,
                step=500.0,
                help="How much you want to save each month"
            )
        
        with col2:
            expense_limit = st.number_input(
                "Monthly Expense Limit (₱)",
                min_value=0.0,
                step=1000.0,
                help="Maximum amount you want to spend monthly"
            )
        
        st.subheader("🎯 Financial Goals")
        financial_goals = st.text_area(
            "Describe your financial goals",
            placeholder="e.g., Save for emergency fund, Buy a house, Pay off debt...",
            height=100
        )
        
        st.subheader("💡 Budget Preferences")
        budget_style = st.selectbox(
            "Preferred budgeting approach",
            ["50/30/20 Rule (Needs/Wants/Savings)", "Envelope Method", "Zero-Based Budget", "Custom"]
        )
        
        submitted = st.form_submit_button("✅ Complete Setup", type="primary")
        
        if submitted:
            if monthly_income > 0:
                # Save user profile
                profile_data = {
                    'monthly_income': monthly_income,
                    'savings_goal': savings_goal,
                    'expense_limit': expense_limit,
                    'financial_goals': financial_goals,
                    'budget_style': budget_style,
                    'setup_completed': True,
                    'created_date': datetime.now().strftime('%Y-%m-%d')
                }
                
                tracker.save_user_profile(profile_data)
                st.success("🎉 Setup completed successfully! Welcome to your budget tracker.")
                st.balloons()
                
                # Redirect to dashboard
                st.session_state.current_page = "Dashboard"
                st.rerun()
            else:
                st.error("Please enter your monthly income to continue.")
    
    # Show sample data option
    st.markdown("---")
    st.markdown("### 📊 Want to see how it works?")
    if st.button("🔄 Add Sample Data", help="Add some sample transactions to explore features"):
        # Add sample transactions
        sample_transactions = [
            {'type': 'income', 'amount': 50000, 'description': 'Salary', 'category': 'Income', 'date': datetime.now().date()},
            {'type': 'expense', 'amount': 15000, 'description': 'Rent', 'category': 'Housing', 'date': datetime.now().date()},
            {'type': 'expense', 'amount': 3000, 'description': 'Groceries', 'category': 'Food', 'date': datetime.now().date()},
            {'type': 'expense', 'amount': 2000, 'description': 'Transportation', 'category': 'Transportation', 'date': datetime.now().date()},
            {'type': 'expense', 'amount': 1500, 'description': 'Coffee & Dining', 'category': 'Food', 'date': datetime.now().date()}
        ]
        
        for transaction in sample_transactions:
            tracker.add_transaction(
                transaction['type'],
                transaction['amount'],
                transaction['description'],
                transaction['category'],
                transaction['date']
            )
        
        st.success("✅ Sample data added! You can now explore all features.")
        st.rerun()

elif page == "Dashboard":
    st.header("📊 Financial Dashboard")
    
    # Show current view
    st.info(f"📅 Currently viewing: **{data_view}** data")
    
    # Key metrics in vertical list layout
    st.subheader("💰 Financial Summary")
    
    # Get comprehensive overview based on current view
    overview = tracker.get_financial_overview(df, 
        'current_month' if data_view == 'Current Month' else 
        'current_year' if data_view == 'Current Year' else 'all'
    )
    
    # Create metrics as a list with better spacing
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("💰 Current Balance", f"₱{overview['total_balance']:,.2f}")
        st.metric("📈 Total Income", f"₱{overview['total_income']:,.2f}")
        st.metric("📊 Transaction Count", f"{overview['transaction_count']:,}")
    
    with col2:
        st.metric("📉 Total Expenses", f"₱{overview['total_expenses']:,.2f}")
        st.metric("🏆 Largest Expense", f"₱{overview['largest_expense']:,.2f}")
        st.metric("🔄 Most Frequent Category", overview['most_frequent_category'])
    
    # Additional metrics for monthly view
    if data_view != "Current Month":
        st.markdown("### 📊 Average Monthly Overview")
        col3, col4 = st.columns(2)
        with col3:
            st.metric("📈 Avg Monthly Income", f"₱{overview['avg_monthly_income']:,.2f}")
        with col4:
            st.metric("📉 Avg Monthly Expenses", f"₱{overview['avg_monthly_expenses']:,.2f}")
    
    # Show date range
    if overview['date_range'] != 'No data':
        st.caption(f"📅 Data period: {overview['date_range']}")
        
    st.divider()
    
    # Charts section
    if not df.empty:
        st.header("📈 Visual Analytics")
        
        # Charts in vertical list layout
        st.subheader("📊 Expense Breakdown")
        pie_chart = tracker.create_expense_pie_chart(df)
        if pie_chart:
            st.plotly_chart(pie_chart, use_container_width=True)
        
        st.subheader("📈 Spending by Category")
        bar_chart = tracker.create_category_bar_chart(df)
        if bar_chart:
            st.plotly_chart(bar_chart, use_container_width=True)
        
        st.subheader("📉 Monthly Trends")
        trend_chart = tracker.create_monthly_trend_chart(df)
        if trend_chart:
            st.plotly_chart(trend_chart, use_container_width=True)
        
        st.subheader("💹 Balance History")
        balance_chart = tracker.create_balance_chart(df)
        if balance_chart:
            st.plotly_chart(balance_chart, use_container_width=True)
        
        # Recent transactions with delete functionality  
        st.header("📋 Recent Transactions")
        st.caption(f"Showing transactions for: {data_view}")
        
        if len(df) > 0:
            # Display last 10 transactions with delete options
            display_count = min(10, len(df))
            recent_df = df.tail(display_count).sort_values('date', ascending=False)
            
            for idx, transaction in recent_df.iterrows():
                with st.expander(f"ID: {transaction['id']} - {transaction['description']} - ₱{transaction['amount']:,.2f}"):
                    col1, col2 = st.columns([3, 1])
                    
                    with col1:
                        st.write(f"**📅 Date:** {transaction['date'].strftime('%Y-%m-%d') if hasattr(transaction['date'], 'strftime') else transaction['date']}")
                        st.write(f"**💼 Type:** {transaction['type'].title()}")
                        st.write(f"**💰 Amount:** ₱{transaction['amount']:,.2f}")
                        st.write(f"**🏷️ Category:** {transaction['category']}")
                        st.write(f"**📝 Description:** {transaction['description'][:50]}{'...' if len(str(transaction['description'])) > 50 else ''}")
                    
                    with col2:
                        if st.button(f"🗑️ Delete", key=f"delete_{transaction['id']}"):
                            try:
                                tracker.delete_transaction(int(transaction['id']))
                                st.success(f"Transaction {transaction['id']} deleted!")
                                st.rerun()
                            except Exception as e:
                                st.error(f"Error deleting transaction: {str(e)}")
        else:
            st.info(f"No transactions found for {data_view}. Try a different time period or add some transactions!")
    
    else:
        st.info(f"No data available for {data_view}. Please add some transactions to see your dashboard.")

elif page == "Add Transaction":
    st.header("➕ Add New Transaction")
    st.caption("Add income or expense transactions to track your finances")
    
    # Transaction form in list layout
    with st.form("add_transaction"):
        st.subheader("📝 Transaction Details")
        
        transaction_type = st.selectbox("Transaction Type", ["income", "expense"])
        amount = st.number_input("Amount (₱)", min_value=0.01, step=0.01)
        description = st.text_input("Description")
        
        if transaction_type == "expense":
            category = st.selectbox(
                "Category (leave blank for AI categorization)", 
                ["", "Food", "Transportation", "Entertainment", "Healthcare", 
                 "Shopping", "Utilities", "Housing", "Education", "Other"]
            )
        else:
            category = "Income"
            st.text("Category: Income")
        
        transaction_date = st.date_input("Date", value=date.today())
        
        submitted = st.form_submit_button("Add Transaction")
        
        if submitted:
            if amount > 0 and description:
                try:
                    # Add the transaction
                    updated_df = tracker.add_transaction(
                        transaction_type, amount, description, 
                        category if category else None, transaction_date
                    )
                    
                    st.success(f"✅ {transaction_type.title()} of ₱{amount:.2f} added successfully!")
                    st.rerun()  # Refresh the page to show updated data
                    
                except Exception as e:
                    st.error(f"❌ Error adding transaction: {str(e)}")
            else:
                st.error("❌ Please fill in all required fields with valid values.")

elif page == "AI Analysis":
    st.header("🤖 AI-Powered Financial Analysis")
    st.caption(f"AI insights based on your {data_view.lower()} data")
    
    if df.empty:
        st.warning("No data available for analysis. Please add some transactions first.")
    else:
        # Check if OpenAI API key is available
        if not os.getenv('OPENAI_API_KEY'):
            st.error("⚠️ OpenAI API key not found. Please set OPENAI_API_KEY in your environment variables to use AI features.")
        else:
            tab1, tab2 = st.tabs(["Spending Analysis", "Budget Recommendations"])
            
            with tab1:
                st.subheader("📊 AI Spending Analysis")
                
                if st.button("🔍 Generate Spending Analysis", type="primary", use_container_width=True):
                    with st.spinner("Analyzing your spending patterns..."):
                        analysis = tracker.ai_spending_analysis(df)
                        st.markdown("### 📊 Analysis Results")
                        st.write(analysis)
            
            with tab2:
                st.subheader("💡 AI Budget Recommendations")
                
                monthly_income = st.number_input("Enter your monthly income for personalized recommendations:", 
                                               min_value=0.0, step=100.0)
                
                if monthly_income > 0 and st.button("💡 Get Budget Recommendations", type="primary", use_container_width=True):
                    with st.spinner("Generating personalized budget recommendations..."):
                        recommendations = tracker.ai_budget_recommendations(df, monthly_income)
                        st.markdown("### 💰 Budget Recommendations")
                        st.write(recommendations)

elif page == "Data Management":
    st.header("📁 Data Management")
    st.caption(f"Manage and analyze your {data_view.lower()} transaction data")
    
    tab1, tab2, tab3 = st.tabs(["View Data", "Upload Data", "Download Data"])
    
    with tab1:
        st.subheader("📋 All Transactions")
        st.info(f"📅 Currently viewing: **{data_view}** transactions")
        
        if not df.empty:
            # Filters
            col1, col2, col3 = st.columns(3)
            
            with col1:
                type_filter = st.selectbox("Filter by type", ["All", "income", "expense"])
            
            with col2:
                if not df.empty:
                    categories = ["All"] + sorted(df['category'].unique().tolist())
                    category_filter = st.selectbox("Filter by category", categories)
                else:
                    category_filter = "All"
            
            with col3:
                if not df.empty:
                    date_range = st.date_input(
                        "Date range",
                        value=(df['date'].min().date(), df['date'].max().date()),
                        min_value=df['date'].min().date(),
                        max_value=df['date'].max().date()
                    )
                else:
                    date_range = (date.today(), date.today())
            
            # Apply filters
            filtered_df = df.copy()
            
            if type_filter != "All":
                filtered_df = filtered_df[filtered_df['type'] == type_filter]
            
            if category_filter != "All":
                filtered_df = filtered_df[filtered_df['category'] == category_filter]
            
            if len(date_range) == 2:
                start_date, end_date = date_range
                filtered_df = filtered_df[
                    (filtered_df['date'].dt.date >= start_date) & 
                    (filtered_df['date'].dt.date <= end_date)
                ]
            
            # Display filtered data
            if not filtered_df.empty:
                display_df = filtered_df.copy()
                display_df['amount'] = display_df['amount'].apply(lambda x: f"₱{x:,.2f}")
                display_df['date'] = display_df['date'].dt.strftime('%Y-%m-%d')
                
                # Truncate long descriptions for better display
                display_df['description'] = display_df['description'].apply(
                    lambda x: str(x)[:30] + '...' if len(str(x)) > 30 else str(x)
                )
                
                st.dataframe(
                    display_df[['date', 'type', 'amount', 'description', 'category']],
                    use_container_width=True,
                    hide_index=True,
                    column_config={
                        "date": st.column_config.TextColumn("Date", width="small"),
                        "type": st.column_config.TextColumn("Type", width="small"),
                        "amount": st.column_config.TextColumn("Amount", width="medium"),
                        "description": st.column_config.TextColumn("Description", width="large"),
                        "category": st.column_config.TextColumn("Category", width="medium")
                    }
                )
                
                # Summary statistics
                st.subheader("📊 Summary Statistics")
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Total Transactions", len(filtered_df))
                
                with col2:
                    income_total = filtered_df[filtered_df['type'] == 'income']['amount'].sum()
                    st.metric("Total Income", f"₱{income_total:,.2f}")
                
                with col3:
                    expense_total = filtered_df[filtered_df['type'] == 'expense']['amount'].sum()
                    st.metric("Total Expenses", f"₱{expense_total:,.2f}")
            
            else:
                st.info(f"No transactions match the selected filters for {data_view}.")
        else:
            st.info(f"No transactions found for {data_view}. Try a different time period or add some transactions.")
    
    with tab2:
        st.subheader("📤 Upload Data from Excel")
        
        uploaded_file = st.file_uploader("Choose an Excel file", type=['xlsx', 'xls'])
        
        if uploaded_file is not None:
            try:
                # Read the uploaded file
                upload_df = pd.read_excel(uploaded_file)
                
                # Display preview
                st.write("Preview of uploaded data:")
                st.dataframe(upload_df.head())
                
                # Validate required columns
                required_columns = ['type', 'amount', 'description', 'category', 'date']
                missing_columns = [col for col in required_columns if col not in upload_df.columns]
                
                if missing_columns:
                    st.error(f"Missing required columns: {', '.join(missing_columns)}")
                    st.write("Required columns: type, amount, description, category, date")
                else:
                    if st.button("Import Data"):
                        # Process and save the data
                        upload_df['date'] = pd.to_datetime(upload_df['date'])
                        upload_df['id'] = range(1, len(upload_df) + 1)
                        
                        tracker.save_data(upload_df)
                        st.success("✅ Data imported successfully!")
                        st.rerun()
            
            except Exception as e:
                st.error(f"❌ Error reading file: {str(e)}")
    
    with tab3:
        st.subheader("📥 Download Data")
        
        if not df.empty:
            # Prepare download data
            download_df = df.copy()
            download_df['date'] = download_df['date'].dt.strftime('%Y-%m-%d')
            
            # Convert to Excel bytes
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                download_df.to_excel(writer, index=False, sheet_name='Transactions')
            
            excel_data = output.getvalue()
            
            view_suffix = f"_{data_view.lower().replace(' ', '_')}" if data_view != "All Time" else ""
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.download_button(
                    label="📥 Download as Excel",
                    data=excel_data,
                    file_name=f"budget_data{view_suffix}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    use_container_width=True
                )
            
            with col2:
                # Also provide CSV download
                csv_data = download_df.to_csv(index=False)
                st.download_button(
                    label="📥 Download as CSV",
                    data=csv_data,
                    file_name=f"budget_data{view_suffix}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv",
                    use_container_width=True
                )
        else:
            st.info(f"No data available to download for {data_view}. Try a different time period or add some transactions.")

# Footer
st.markdown("---")
st.markdown("### ℹ️ Tips & Information")

col1, col2 = st.columns(2)
with col1:
    st.markdown("**💡 Tips:**")
    st.markdown("• Use different time views to analyze patterns")
    st.markdown("• Set up your profile for personalized insights")
    st.markdown("• Regular transaction entry improves AI analysis")

with col2:
    st.markdown("**🔧 Features:**")
    st.markdown("• Excel-based database storage")
    st.markdown("• AI-powered expense categorization")
    st.markdown("• Interactive charts and analytics")

if not os.getenv('OPENAI_API_KEY'):
    st.warning("⚠️ Set your OpenAI API key as environment variable to enable AI features!")

st.markdown("---")
st.markdown("🔗 **Built with:** Streamlit • Plotly • OpenAI API • Excel Integration")
st.markdown(f"📊 **Data View:** Currently showing {data_view.lower()} data")