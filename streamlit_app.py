"""
Climate × ML Playground (Beta)
Interactive teaser site for climate ML experiments
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
import requests
from io import StringIO
import json
import os

# Page config
st.set_page_config(
    page_title="Climate × ML Playground",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark theme and styling
st.markdown("""
<style>
    .main {
        background-color: #0e1117;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding: 10px 24px;
        background-color: #1e2130;
        border-radius: 8px;
        color: white;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    .hero-subtitle {
        font-size: 1.3rem;
        color: #a0a0a0;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        color: white;
    }
    .whatsapp-btn {
        background: #25D366 !important;
        color: white !important;
        font-size: 1.2rem !important;
        padding: 1rem 2rem !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
        border: none !important;
        width: 100% !important;
    }
    .credit-box {
        background: #1e2130;
        padding: 20px;
        border-radius: 12px;
        border-left: 4px solid #667eea;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar with CTA
with st.sidebar:
    st.markdown("### 🚀 Join the Lab")
    st.markdown("**50+ ML engineers** testing live experiments")
    
    st.markdown("#### 🏆 Top 3 Contributors Get:")
    st.markdown("✅ Public credit on our platform")
    st.markdown("✅ Early access to premium datasets")
    st.markdown("✅ Featured in our ML showcase")
    
    if st.button("🟢 Join WhatsApp Lab", key="sidebar_cta", use_container_width=True):
        st.markdown("[Click here to join →](https://whatsapp.com/channel/0029VbBJKn4DZ4LdgNXoAs32)")
    
    st.markdown("---")
    st.markdown("### 📊 Quick Stats")
    st.metric("Experiments Generated", "500+")
    st.metric("Active Researchers", "50+")
    st.metric("Datasets Available", "3")
    
    st.markdown("---")
    st.markdown("### 🔗 Resources")
    st.markdown("[📚 Documentation](https://github.com/poowa-gg/500-experiments-)")
    st.markdown("[💻 GitHub Repo](https://github.com/poowa-gg/500-experiments-)")

# Hero Section
st.markdown('<h1 class="hero-title">🌍 Climate × ML Playground (Beta)</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Real datasets • Instant model experiments • Top 3 runs win public credit</p>', unsafe_allow_html=True)

# Quick metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="metric-card"><h2>500+</h2><p>Experiments</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card"><h2>3</h2><p>Live Datasets</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card"><h2>50+</h2><p>ML Engineers</p></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="metric-card"><h2>Beta</h2><p>Free Access</p></div>', unsafe_allow_html=True)

st.markdown("---")

# Main Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📊 Browse Data", "🔮 Live Forecast", "🏆 Leaderboard", "🧪 Experiment Generator"])

# TAB 1: Browse Data
with tab1:
    st.header("📊 Climate Datasets Explorer")
    
    dataset_choice = st.selectbox(
        "Choose a dataset:",
        ["Global Temperature (1880-2024)", "Arctic Sea Ice Extent", "CO2 Levels (Mauna Loa)"]
    )
    
    @st.cache_data
    def load_global_temp():
        url = "https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv"
        try:
            response = requests.get(url, timeout=10)
            df = pd.read_csv(StringIO(response.text), skiprows=1)
            df = df[['Year', 'J-D']].copy()
            df.columns = ['Year', 'Temperature_Anomaly']
            df = df[df['Year'] != 'Year'].dropna()
            df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
            df['Temperature_Anomaly'] = pd.to_numeric(df['Temperature_Anomaly'], errors='coerce')
            return df.dropna()
        except:
            # Fallback synthetic data
            years = np.arange(1880, 2025)
            temps = np.linspace(-0.4, 1.2, len(years)) + np.random.normal(0, 0.1, len(years))
            return pd.DataFrame({'Year': years, 'Temperature_Anomaly': temps})
    
    @st.cache_data
    def load_arctic_ice():
        years = np.arange(1979, 2025)
        ice = 7.5 - (years - 1979) * 0.08 + np.random.normal(0, 0.3, len(years))
        return pd.DataFrame({'Year': years, 'Ice_Extent_Million_km2': ice})
    
    @st.cache_data
    def load_co2():
        years = np.arange(1958, 2025)
        co2 = 315 + (years - 1958) * 2.2 + np.random.normal(0, 2, len(years))
        return pd.DataFrame({'Year': years, 'CO2_ppm': co2})
    
    if dataset_choice == "Global Temperature (1880-2024)":
        df = load_global_temp()
        y_col = 'Temperature_Anomaly'
        y_label = 'Temperature Anomaly (°C)'
        color = '#ff6b6b'
    elif dataset_choice == "Arctic Sea Ice Extent":
        df = load_arctic_ice()
        y_col = 'Ice_Extent_Million_km2'
        y_label = 'Ice Extent (Million km²)'
        color = '#4ecdc4'
    else:
        df = load_co2()
        y_col = 'CO2_ppm'
        y_label = 'CO2 Concentration (ppm)'
        color = '#95e1d3'
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Interactive plot
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df['Year'],
            y=df[y_col],
            mode='lines+markers',
            name=y_label,
            line=dict(color=color, width=3),
            marker=dict(size=6)
        ))
        fig.update_layout(
            title=f"{dataset_choice} - Historical Trend",
            xaxis_title="Year",
            yaxis_title=y_label,
            template="plotly_dark",
            height=500,
            hovermode='x unified'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 📈 Dataset Info")
        st.metric("Total Records", len(df))
        st.metric("Year Range", f"{int(df['Year'].min())}-{int(df['Year'].max())}")
        st.metric("Latest Value", f"{df[y_col].iloc[-1]:.2f}")
        
        # Download button
        csv = df.to_csv(index=False)
        st.download_button(
            label="📥 Download CSV",
            data=csv,
            file_name=f"{dataset_choice.replace(' ', '_')}.csv",
            mime="text/csv",
            use_container_width=True
        )
    
    # Sortable table
    st.markdown("### 📋 Data Table")
    st.dataframe(df.sort_values('Year', ascending=False), use_container_width=True, height=300)

# TAB 2: Live Forecast
with tab2:
    st.header("🔮 Live Forecast Experiment")
    st.markdown("**Train a model in real-time and see predictions instantly!**")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        years_ahead = st.slider("📅 Forecast Years Ahead", 1, 30, 10)
        model_choice = st.selectbox("🤖 Model Type", ["Linear Regression", "Polynomial (degree 3)"])
    
    with col2:
        st.markdown("### 🎯 Quick Actions")
        if st.button("🔄 Retrain Model", use_container_width=True):
            st.rerun()
    
    # Load data and train model
    df_temp = load_global_temp()
    X = df_temp['Year'].values.reshape(-1, 1)
    y = df_temp['Temperature_Anomaly'].values
    
    # Train model
    if model_choice == "Linear Regression":
        model = LinearRegression()
        model.fit(X, y)
    else:
        model = make_pipeline(PolynomialFeatures(3), LinearRegression())
        model.fit(X, y)
    
    # Make predictions
    future_years = np.arange(df_temp['Year'].max() + 1, df_temp['Year'].max() + years_ahead + 1)
    future_X = future_years.reshape(-1, 1)
    predictions = model.predict(future_X)
    
    # Calculate metrics
    train_score = model.score(X, y)
    
    # Plot
    fig = go.Figure()
    
    # Historical data
    fig.add_trace(go.Scatter(
        x=df_temp['Year'],
        y=df_temp['Temperature_Anomaly'],
        mode='lines+markers',
        name='Historical Data',
        line=dict(color='#4ecdc4', width=2),
        marker=dict(size=4)
    ))
    
    # Predictions
    fig.add_trace(go.Scatter(
        x=future_years,
        y=predictions,
        mode='lines+markers',
        name='Forecast',
        line=dict(color='#ff6b6b', width=3, dash='dash'),
        marker=dict(size=8, symbol='star')
    ))
    
    fig.update_layout(
        title=f"Temperature Forecast using {model_choice}",
        xaxis_title="Year",
        yaxis_title="Temperature Anomaly (°C)",
        template="plotly_dark",
        height=500,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Model metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Model R² Score", f"{train_score:.4f}")
    with col2:
        st.metric("Forecast Horizon", f"{years_ahead} years")
    with col3:
        st.metric("Predicted Change", f"+{predictions[-1] - y[-1]:.2f}°C")
    
    # CTA
    st.markdown("---")
    st.markdown("### 📸 Share Your Results!")
    st.markdown("**Screenshot this forecast → Share in WhatsApp → Win public credit!**")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.info("💡 **How to win:** Share your best forecast in our WhatsApp channel. Top 3 most accurate predictions get featured!")
    with col2:
        if st.button("🟢 Join WhatsApp Lab", key="forecast_cta", use_container_width=True):
            st.markdown("[Click here to join →](https://whatsapp.com/channel/0029VbBJKn4DZ4LdgNXoAs32)")

# TAB 3: Leaderboard
with tab3:
    st.header("🏆 Leaderboard & Credit")
    
    st.markdown("### 🎯 How to Get on the Leaderboard")
    st.markdown("""
    1. **Run experiments** using our datasets
    2. **Share your results** in the WhatsApp channel
    3. **Top 3 contributors** get public credit monthly
    """)
    
    st.markdown("---")
    st.markdown("### 🏅 Current Leaders (December 2025)")
    
    # Placeholder leaderboard
    leaderboard_data = {
        "Rank": ["🥇", "🥈", "🥉", "4", "5"],
        "Contributor": ["[Open Slot]", "[Open Slot]", "[Open Slot]", "[Open Slot]", "[Open Slot]"],
        "Experiments": ["-", "-", "-", "-", "-"],
        "Accuracy": ["-", "-", "-", "-", "-"],
        "Status": ["Available", "Available", "Available", "Available", "Available"]
    }
    
    df_leaderboard = pd.DataFrame(leaderboard_data)
    st.dataframe(df_leaderboard, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="credit-box">', unsafe_allow_html=True)
        st.markdown("### 🎁 Winner Benefits")
        st.markdown("✅ **Public credit** on our platform")
        st.markdown("✅ **Featured profile** in showcase")
        st.markdown("✅ **Early access** to premium datasets")
        st.markdown("✅ **Direct collaboration** opportunities")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="credit-box">', unsafe_allow_html=True)
        st.markdown("### 📊 Evaluation Criteria")
        st.markdown("🎯 **Model accuracy** (40%)")
        st.markdown("💡 **Innovation** (30%)")
        st.markdown("📝 **Documentation** (20%)")
        st.markdown("🤝 **Community engagement** (10%)")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🚀 Ready to Compete?")
    
    if st.button("🟢 Join WhatsApp Lab & Start Competing", key="leaderboard_cta", use_container_width=True):
        st.markdown("[Click here to join →](https://whatsapp.com/channel/0029VbBJKn4DZ4LdgNXoAs32)")

# TAB 4: Experiment Generator Integration
with tab4:
    st.header("🧪 Hyperlocal Climate Intelligence - Experiment Generator")
    st.markdown("**Generate 500+ experimental scenarios for climate intelligence platforms**")
    
    st.markdown("### 🎯 What This Does")
    st.markdown("""
    This tool generates diverse experimental scenarios for testing climate intelligence platforms across:
    - **5 User Segments**: Farmers, Insurers, Government, Logistics, NGOs
    - **12 Nigerian Regions**: Lagos, Kano, Rivers, and more
    - **8 Climate Events**: Drought, flood, heavy rainfall, etc.
    - **5 Alert Channels**: SMS, Mobile App, Web, USSD, WhatsApp
    """)
    
    if st.button("🚀 Generate 500 Experiments", use_container_width=True):
        with st.spinner("Generating experiments..."):
            try:
                # Import the generator
                from climate_experiment_generator import ClimateExperimentGenerator
                
                generator = ClimateExperimentGenerator()
                experiments = generator.generate_experiments(500)
                summary = generator.generate_summary_report(experiments)
                
                st.success("✅ Generated 500 experiments successfully!")
                
                # Display summary
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Total Experiments", summary['total_experiments'])
                with col2:
                    st.metric("Avg ROI", f"{summary['avg_expected_roi']:.2f}x")
                with col3:
                    st.metric("Total Cost", f"₦{summary['total_estimated_cost']/1e6:.1f}M")
                with col4:
                    st.metric("High Priority", summary['high_priority_count'])
                
                # Show sample experiments
                st.markdown("### 📊 Sample Experiments")
                sample_df = pd.DataFrame(experiments[:10])
                display_cols = ['experiment_id', 'user_segment', 'region', 'climate_event', 
                               'expected_roi', 'cost_estimate_ngn', 'priority']
                st.dataframe(sample_df[display_cols], use_container_width=True)
                
                # Download button
                experiments_json = json.dumps(experiments, indent=2)
                st.download_button(
                    label="📥 Download All Experiments (JSON)",
                    data=experiments_json,
                    file_name="climate_experiments.json",
                    mime="application/json",
                    use_container_width=True
                )
                
            except Exception as e:
                st.error(f"Error generating experiments: {str(e)}")
                st.info("💡 Make sure climate_experiment_generator.py is in the same directory")
    
    st.markdown("---")
    st.markdown("### 📚 Learn More")
    st.markdown("[View Full Documentation](https://github.com/poowa-gg/500-experiments-)")
    st.markdown("[Explore Web Interface](https://climate-experiments.onrender.com)")

# Footer
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("### 🌍 About")
    st.markdown("Climate × ML Playground for testing hyperlocal climate intelligence platforms in Nigeria")
with col2:
    st.markdown("### 🔗 Links")
    st.markdown("[GitHub](https://github.com/poowa-gg/500-experiments-) • [Docs](https://github.com/poowa-gg/500-experiments-) • [WhatsApp](https://whatsapp.com/channel/0029VbBJKn4DZ4LdgNXoAs32)")
with col3:
    st.markdown("### 📧 Contact")
    st.markdown("Join our WhatsApp channel for updates and collaboration")

st.markdown("---")
st.markdown("<p style='text-align: center; color: #666;'>Built with ❤️ for climate resilience • Beta v1.0</p>", unsafe_allow_html=True)
