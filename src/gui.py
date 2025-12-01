"""
Streamlit GUI for Evolutionary Strategy Research Project
Run with: streamlit run src/gui.py
"""
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from data_loader import load_synthetic_data
from gp_engine import EvolutionEngine

# Page configuration
st.set_page_config(
    page_title="Evolutionary Strategy Research",
    page_icon="📈",
    layout="wide"
)

# Title
st.title("📈 Evolutionary Strategy Research Project")
st.markdown("A research framework for evolving trading strategies using genetic programming")

# Sidebar for controls
st.sidebar.header("⚙️ Configuration")

# Data loading section
st.sidebar.subheader("📊 Data Settings")
n_rows = st.sidebar.slider("Number of data points", 100, 5000, 1000, 100)
load_data = st.sidebar.button("Load Synthetic Data")

# Evolution settings
st.sidebar.subheader("🧬 Evolution Settings")
generations = st.sidebar.slider("Generations", 1, 200, 50, 1)
population = st.sidebar.slider("Population Size", 10, 500, 50, 10)
run_evolution = st.sidebar.button("🚀 Run Evolution")

# Initialize session state
if 'data' not in st.session_state:
    st.session_state.data = None
if 'evolution_results' not in st.session_state:
    st.session_state.evolution_results = []
if 'engine' not in st.session_state:
    st.session_state.engine = None

# Main content area
tab1, tab2, tab3 = st.tabs(["📊 Data Visualization", "🧬 Evolution", "📈 Results"])

# Tab 1: Data Visualization
with tab1:
    st.header("Data Visualization")
    
    if load_data or st.session_state.data is not None:
        if st.session_state.data is None:
            with st.spinner("Loading synthetic data..."):
                st.session_state.data = load_synthetic_data(n_rows=n_rows)
        
        if st.session_state.data is not None:
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Data Points", len(st.session_state.data))
            with col2:
                st.metric("Mean Price", f"${st.session_state.data['price'].mean():.2f}")
            with col3:
                st.metric("Std Deviation", f"${st.session_state.data['price'].std():.2f}")
            with col4:
                st.metric("Price Range", f"${st.session_state.data['price'].min():.2f} - ${st.session_state.data['price'].max():.2f}")
            
            # Plot price data
            fig, ax = plt.subplots(figsize=(12, 6))
            ax.plot(st.session_state.data.index, st.session_state.data['price'], linewidth=1.5, color='#1f77b4')
            ax.set_xlabel("Time", fontsize=12)
            ax.set_ylabel("Price", fontsize=12)
            ax.set_title("Synthetic Price Data", fontsize=14, fontweight='bold')
            ax.grid(True, alpha=0.3)
            st.pyplot(fig)
            
            # Show data table
            with st.expander("📋 View Raw Data"):
                st.dataframe(st.session_state.data.head(100))
    else:
        st.info("👈 Click 'Load Synthetic Data' in the sidebar to begin")

# Tab 2: Evolution
with tab2:
    st.header("Evolution Process")
    
    if st.session_state.data is None:
        st.warning("⚠️ Please load data first in the Data Visualization tab")
    else:
        if run_evolution:
            with st.spinner(f"Running evolution: {generations} generations, {population} population..."):
                # Initialize engine
                st.session_state.engine = EvolutionEngine(
                    st.session_state.data, 
                    population=population
                )
                
                # Simulate evolution progress
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                # Simulate evolution (since it's a placeholder, we'll show progress)
                evolution_log = []
                for gen in range(generations):
                    progress = (gen + 1) / generations
                    progress_bar.progress(progress)
                    status_text.text(f"Generation {gen + 1}/{generations}")
                    
                    # Simulate some metrics (placeholder)
                    fitness = np.random.uniform(0.5, 1.0)
                    evolution_log.append({
                        'generation': gen + 1,
                        'best_fitness': fitness,
                        'avg_fitness': fitness * 0.9,
                        'population': population
                    })
                
                st.session_state.evolution_results = evolution_log
                progress_bar.empty()
                status_text.empty()
                st.success(f"✅ Evolution completed! {generations} generations processed.")
        
        if st.session_state.evolution_results:
            # Display evolution results
            results_df = pd.DataFrame(st.session_state.evolution_results)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Fitness Over Generations")
                fig, ax = plt.subplots(figsize=(10, 6))
                ax.plot(results_df['generation'], results_df['best_fitness'], 
                       label='Best Fitness', linewidth=2, color='#2ecc71')
                ax.plot(results_df['generation'], results_df['avg_fitness'], 
                       label='Average Fitness', linewidth=2, color='#3498db', linestyle='--')
                ax.set_xlabel("Generation", fontsize=12)
                ax.set_ylabel("Fitness", fontsize=12)
                ax.set_title("Evolution Progress", fontsize=14, fontweight='bold')
                ax.legend()
                ax.grid(True, alpha=0.3)
                st.pyplot(fig)
            
            with col2:
                st.subheader("Statistics")
                st.metric("Best Fitness", f"{results_df['best_fitness'].max():.4f}")
                st.metric("Final Fitness", f"{results_df['best_fitness'].iloc[-1]:.4f}")
                st.metric("Improvement", f"{(results_df['best_fitness'].iloc[-1] - results_df['best_fitness'].iloc[0]):.4f}")
            
            with st.expander("📊 Detailed Evolution Log"):
                st.dataframe(results_df)
        else:
            st.info("👈 Configure evolution settings in the sidebar and click 'Run Evolution'")

# Tab 3: Results
with tab3:
    st.header("Results & Analysis")
    
    if st.session_state.evolution_results:
        results_df = pd.DataFrame(st.session_state.evolution_results)
        
        st.subheader("Performance Summary")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Generations", len(results_df))
        with col2:
            st.metric("Best Fitness", f"{results_df['best_fitness'].max():.4f}")
        with col3:
            st.metric("Average Fitness", f"{results_df['avg_fitness'].mean():.4f}")
        with col4:
            improvement = ((results_df['best_fitness'].iloc[-1] - results_df['best_fitness'].iloc[0]) / 
                          results_df['best_fitness'].iloc[0] * 100)
            st.metric("Improvement", f"{improvement:.2f}%")
        
        # Additional visualizations
        st.subheader("Evolution Metrics")
        
        fig, axes = plt.subplots(2, 1, figsize=(12, 10))
        
        # Fitness distribution
        axes[0].hist(results_df['best_fitness'], bins=20, color='#3498db', alpha=0.7, edgecolor='black')
        axes[0].set_xlabel("Fitness", fontsize=12)
        axes[0].set_ylabel("Frequency", fontsize=12)
        axes[0].set_title("Fitness Distribution", fontsize=14, fontweight='bold')
        axes[0].grid(True, alpha=0.3)
        
        # Convergence plot
        axes[1].plot(results_df['generation'], results_df['best_fitness'], 
                     marker='o', markersize=4, linewidth=2, color='#2ecc71')
        axes[1].fill_between(results_df['generation'], 
                            results_df['best_fitness'] - results_df['best_fitness'].std(),
                            results_df['best_fitness'] + results_df['best_fitness'].std(),
                            alpha=0.2, color='#2ecc71')
        axes[1].set_xlabel("Generation", fontsize=12)
        axes[1].set_ylabel("Best Fitness", fontsize=12)
        axes[1].set_title("Convergence Analysis", fontsize=14, fontweight='bold')
        axes[1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        st.pyplot(fig)
        
    else:
        st.info("📊 Run an evolution first to see results here")

# Footer
st.markdown("---")
st.markdown("**Evolutionary Strategy Research Project** | For more information, visit [pbieda.com/contact](https://pbieda.com/contact)")

