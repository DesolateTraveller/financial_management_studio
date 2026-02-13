#---------------------------------------------------------------------------------------------------------------------------------
### Authenticator
#---------------------------------------------------------------------------------------------------------------------------------
import streamlit as st
#---------------------------------------------------------------------------------------------------------------------------------
### Import Libraries
#---------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#----------------------------------------
from io import BytesIO, StringIO
from PIL import Image
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objs as go
#----------------------------------------
import scipy.stats as stats
from scipy.stats import gaussian_kde
#---------------------------------------------------------------------------------------------------------------------------------
### Title for your Streamlit app
#---------------------------------------------------------------------------------------------------------------------------------
st.set_page_config(page_title="Financial Management Studio | v0.1",
                    layout="wide",
                    page_icon="📊",            
                    initial_sidebar_state="auto")
#---------------------------------------------------------------------------------------------------------------------------------
### CSS
#---------------------------------------------------------------------------------------------------------------------------------
st.markdown(
    """
    <style>
    /* Card styling (matches your screenshot) */
    .card {
        background-color: white;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
        border: 1px solid #e1e5eb;
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    .card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
        border-color: #66b2ff;
    }
    .card-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #1a365d;
        margin-bottom: 16px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .card-icon {
        font-size: 1.8rem;
    }
    .card-list {
        padding-left: 0;
        margin-top: 12px;
    }
    .card-list li {
        margin-bottom: 8px;
        font-size: 0.95rem;
        color: #4a5568;
    }
    .card-list li::before {
        content: "✅";
        margin-right: 8px;
        color: #3182ce;
    }

    /* Home button style (top-left) */
    .home-btn {
        background: #f7fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 6px 16px;
        font-size: 14px;
        font-weight: 500;
        color: #2d3748;
        display: inline-flex;
        align-items: center;
        gap: 6px;
        cursor: pointer;
        transition: all 0.2s;
    }
    .home-btn:hover {
        background: #edf2f7;
        color: #1a365d;
    }

    /* Sidebar-like input panel */
    .input-panel {
        background: #f8fafc;
        border-radius: 10px;
        padding: 20px;
        border: 1px solid #e2e8f0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#---------------------------------------------------------------------------------------------------------------------------------
### Description for your Streamlit app
#---------------------------------------------------------------------------------------------------------------------------------
st.markdown(
    """
    <style>
    .title-large {
        text-align: center;
        font-size: 35px;
        font-weight: bold;
        background: linear-gradient(to left, red, orange, blue, indigo, violet);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .title-small {
        text-align: center;
        font-size: 20px;
        background: linear-gradient(to left, red, orange, blue, indigo, violet);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .version-badge {
        text-align: center;
        display: inline-block;
        background: linear-gradient(120deg, #0056b3, #0d4a96);
        color: white;
        padding: 2px 12px;
        border-radius: 20px;
        font-size: 1.15rem;
        margin-top: 8px;
        font-weight: 600;
        letter-spacing: 0.5px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
    }
    </style>
    <div style="text-align: center;">
        <div class="title-large">Financial Management Studio</div>
        <div class="version-badge"> Play with Money | v0.1 </div>
    </div>
    """,
    unsafe_allow_html=True
)

#----------------------------------------
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #F0F2F6;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        color: #333;
        z-index: 100;
    }
    .footer p {
        margin: 0;
    }
    .footer .highlight {
        font-weight: bold;
        color: blue;
    }
    </style>

    <div class="footer">
        <p>© 2026 | Created by : <span class="highlight">Avijit Chakraborty</span> <a href="mailto:avijit.mba18@gmail.com"> 📩 </a> | <span class="highlight">Thank you for visiting the app | Unauthorized uses or copying is strictly prohibited | For best view of the app, please zoom out the browser to 75%.</span> </p>
    </div>
    """,
    unsafe_allow_html=True)

#---------------------------------------------------------------------------------------------------------------------------------
### Connections
#---------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------
### Functions & Definitions
#---------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------
### Main app
#---------------------------------------------------------------------------------------------------------------------------------

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def go_home():
    st.session_state.page = 'home'

# ------------------------------------------------------------------
# HOME PAGE: 3 CALCULATOR CARDS (responsive grid)
# ------------------------------------------------------------------
if st.session_state.page == 'home':

    st.markdown("""
    <style>
    .banner {
        background: linear-gradient(135deg, #f0f7ff 0%, #e6f2ff 100%);
        border-radius: 12px;
        padding: 15px;
        margin: 25px 0;
        border: 1px solid rgba(0, 86, 179, 0.15);
        text-align: center;
        font-size: 1.15rem;
        color: #0056b3;
        font-weight: 600;
    }
    </style>

    <div class="banner">
        Click the cards below to access different sections and explore the following features
    </div>
    """, unsafe_allow_html=True)

    # Use 3 columns (adjust for responsiveness)
    cols = st.columns(4)

    # Fixed Deposit Card
    with cols[0]:
        
        st.markdown(
            """
            <div class="card">
                <div class="card-title"><span class="card-icon">💰</span> Fixed Deposit </div>
                <ul class="card-list">
                    <li>Lump-sum investment</li>
                    <li>Compounding options</li>
                    <li>Maturity & interest calculation</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Open Calculator", key="btn_fd", use_container_width=True, type="primary"):
            st.session_state.page = 'fd'
            st.rerun()

        st.markdown(
            """
            <div class="card">
                <div class="card-title"><span class="card-icon">🏦</span> Loan EMI </div>
                <ul class="card-list">
                    <li>EMI calculation</li>
                    <li>Interest vs principal breakdown</li>
                    <li>Flexible tenure & rate</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Open Calculator", key="btn_loan", use_container_width=True, type="primary"):
            st.session_state.page = 'loan'
            st.rerun()
            
        st.markdown(
            """
            <div class="card">
                <div class=" "card-title"><span class="card-icon">🧾</span> Income Tax (India)</div>
                <ul class="card-list">
                    <li>New vs Old tax regime</li>
                    <li>80C, HRA, deductions</li>
                    <li>Take-home salary</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Open Calculator", key="btn_tax", use_container_width=True, type="primary"):
            st.session_state.page = 'tax'
            st.rerun()
        
        st.markdown(
            """
            <div class="card">
                <div class="card-title"><span class="card-icon">📊</span> CAGR Compound Annual Growth Rate) Calculator</div>
                <ul class="card-list">
                    <li>Annualized return</li>
                    <li>Compare multiple assets</li>
                    <li>Visual growth chart</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Open Calculator", key="btn_cagr", use_container_width=True, type="primary"):
            st.session_state.page = 'cagr'
            st.rerun()
            
    with cols[1]:
        st.markdown(
            """
            <div class="card">
                <div class="card-title"><span class="card-icon">🔄</span> Recurring Deposit</div>
                <ul class="card-list">
                    <li>Monthly deposits</li>
                    <li>Quarterly/Monthly compounding</li>
                    <li>Total maturity estimation</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Open Calculator", key="btn_rd", use_container_width=True, type="primary"):
            st.session_state.page = 'rd'
            st.rerun()

        st.markdown(
            """
            <div class="card">
                <div class="card-title"><span class="card-icon">🏠</span> Home Affordability</div>
                <ul class="card-list">
                    <li>Max home price estimation</li>
                    <li>Based on income & down payment</li>
                    <li>Property tax, insurance, maintenance</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True)
        if st.button("Open Calculator", key="btn_home_af", use_container_width=True, type="primary"):
                st.session_state.page = 'home_af'
                st.rerun()

        st.markdown(
            """
            <div class="card">
                <div class="card-title"><span class="card-icon">🇮🇳</span> PPF / Sukanya / NSC</div>
                <ul class="card-list">
                    <li>India-specific tax-saving instruments</li>
                    <li>Auto current interest rates</li>
                    <li>Maturity & interest projection</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True)
        if st.button("Open Calculator", key="btn_tax_saving", use_container_width=True, type="primary"):
                st.session_state.page = 'tax_saving'
                st.rerun()
                
        st.markdown(
            """
            <div class="card">
                <div class="card-title"><span class="card-icon">📉</span> Inflation Impact</div>
                <ul class="card-list">
                    <li>What will ₹X be worth in Y years?</li>
                    <li>How much needed today for ₹Z future?</li>
                    <li>Real vs nominal value</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True)
        if st.button("Open Calculator", key="btn_inflation", use_container_width=True, type="primary"):
                st.session_state.page = 'inflation'
                st.rerun()
                        
    with cols[2]:
        
        st.markdown(
            """
            <div class="card">
                <div class="card-title"><span class="card-icon">📈</span> SIP (Systematic Investment Plan)</div>
                <ul class="card-list">
                    <li>Monthly mutual fund investments</li>
                    <li>Lumpsum vs SIP comparison</li>
                    <li>Inflation-adjusted returns</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True)
        if st.button("Open Calculator", key="btn_sip", use_container_width=True, type="primary"):
                st.session_state.page = 'sip'
                st.rerun()

        st.markdown(
            """
            <div class="card">
                <div class="card-title"><span class="card-icon">🚗</span> Car Loan + Depreciation</div>
                <ul class="card-list">
                    <li>EMI and total cost</li>
                    <li>Resale value over time</li>
                    <li>20% annual depreciation</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True)
        if st.button("Open Calculator", key="btn_car", use_container_width=True, type="primary"):
                st.session_state.page = 'car'
                st.rerun()
                                                        
    with cols[3]:
        
        st.markdown(
            """
            <div class="card">
                <div class="card-title"><span class="card-icon">🏖️</span> Retirement Planner</div>
                <ul class="card-list">
                    <li>Corpus estimation</li>
                    <li>Monthly savings required</li>
                    <li>EPF, NPS, PPF options</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True)
        if st.button("Open Calculator", key="btn_retirement", use_container_width=True, type="primary"):
                st.session_state.page = 'retirement'
                st.rerun()
                                    
# ------------------------------------------------------------------
# FIXED DEPOSIT PAGE
# ------------------------------------------------------------------
elif st.session_state.page == 'fd':
    
    st.divider()
    
    # ← Home button (top-left)
    col_home, title= st.columns([1,15,])
    with col_home:
        if st.button("← Home", key="home_fd", type="secondary", use_container_width=True):
            go_home()
            st.rerun()

    #st.title("Fixed Deposit Calculator")
    with title:
        st.markdown("""
        <style>
        .banner {
            background: linear-gradient(135deg, #f0f7ff 0%, #e6f2ff 100%);
            border-radius: 12px;
            padding: 5px;
            margin: 5px 0;
            border: 1px solid rgba(0, 86, 179, 0.15);
            text-align: center;
            font-size: 1.15rem;
            color: #0056b3;
            font-weight: 600;
        }
        </style>

        <div class="banner">
            Fixed Deposit Calculator
        </div>
        """, unsafe_allow_html=True)
    
    # Layout: left = inputs, right = results

    input_col, result_col, display_col = st.columns([0.2, 0.3, 0.5])

    with input_col:
        with st.form("fd_form"):
            principal = st.number_input("Principal Amount (₹)", min_value=1000, value=50000, step=1000)
            rate = st.slider("Annual Interest Rate (%)", min_value=1.0, max_value=15.0, value=6.5, step=0.1)
            years = st.slider("Tenure (Years)", min_value=0.5, max_value=10.0, value=3.0, step=0.5)
            
            interest_type = st.radio(
                "Interest Type",
                ["Simple Interest", "Compound Interest", "Compare Both"],
                index=2
            )
            
            compounding = st.selectbox(
                "Compounding Frequency",
                ["Annually", "Semi-Annually", "Quarterly", "Monthly"],
                index=2,
                disabled=(interest_type == "Simple Interest")
            )
            
            submitted = st.form_submit_button("Calculate")

    # ----------------------------
    # RESULT COLUMN
    # ----------------------------
    with result_col:
        if submitted:
            P = principal
            r = rate / 100
            t = years
            n_map = {"Annually": 1, "Semi-Annually": 2, "Quarterly": 4, "Monthly": 12}
            n = n_map[compounding]

            # Calculate both (always, for comparison)
            si_amount = P * (1 + r * t)
            si_interest = si_amount - P

            ci_amount = P * (1 + r / n) ** (n * t)
            ci_interest = ci_amount - P

            # Always show both metric rows (even if only one selected)

            # --- Simple Interest Metrics ---
            with st.container(border=True):
                st.caption("🔹 Simple Interest")
                col_s1, col_s2, col_s3 = st.columns(3)
                col_s1.metric("Principal", f"₹{P:,.0f}")
                col_s2.metric("Maturity", f"₹{si_amount:,.0f}")
                col_s3.metric("Interest", f"₹{si_interest:,.0f}")

            # --- Compound Interest Metrics ---
            with st.container(border=True):
                st.caption("🔸 Compound Interest")
                col_c1, col_c2, col_c3 = st.columns(3)
                col_c1.metric("Principal", f"₹{P:,.0f}")
                col_c2.metric("Maturity", f"₹{ci_amount:,.0f}")
                col_c3.metric("Interest", f"₹{ci_interest:,.0f}")

            # --- Difference ---
            with st.container(border=True):
                diff_maturity = ci_amount - si_amount
                diff_interest = ci_interest - si_interest
                st.metric("📈 Extra Gain (CI over SI)", f"₹{diff_maturity:,.0f}")

            # --- Tabs for Calculation & Growth ---
            with st.container(border=True):
                tab_calc, tab_growth = st.tabs(["🧮 Calculation", "📊 Growth Table"])

                with tab_calc:
                    st.markdown("#### Simple Interest")
                    st.markdown(f"$ A = P(1 + rt) = {P} \\times (1 + {r} \\times {t}) = ₹{si_amount:,.0f} $")
                    
                    st.markdown("#### Compound Interest")
                    st.markdown(f"$ A = P \\left(1 + \\frac{{r}}{{n}}\\right)^{{nt}} = {P} \\times \\left(1 + \\frac{{{r}}}{{{n}}}\\right)^{{{n} \\times {t}}} = ₹{ci_amount:,.0f} $")

                with tab_growth:
                    max_year = int(t) + (1 if t > int(t) else 0)
                    years_list = []
                    si_vals = []
                    ci_vals = []
                    diff_vals = []
                    pct_diff_vals = []

                    for yr in range(0, max_year + 1):
                        T = min(yr, t)
                        si_val = P * (1 + r * T)
                        ci_val = P * (1 + r / n) ** (n * T)
                        diff_val = ci_val - si_val
                        pct_diff = (diff_val / si_val * 100) if si_val != 0 else 0

                        years_list.append(T)
                        si_vals.append(round(si_val, 2))
                        ci_vals.append(round(ci_val, 2))
                        diff_vals.append(round(diff_val, 2))
                        pct_diff_vals.append(round(pct_diff, 2))

                    growth_df = pd.DataFrame({
                        "Year": years_list,
                        "Simple (₹)": si_vals,
                        "Compound (₹)": ci_vals,
                        "Diff (₹)": diff_vals,
                        "Diff (%)": pct_diff_vals
                    })

                    # Apply color gradient to 'Diff (₹)' and 'Diff (%)'
                    def color_diff(val):
                        # Green for positive, red for negative (though usually positive)
                        color = '#4ade80' if val >= 0 else '#f87171'
                        return f'color: {color}; font-weight: bold'

                    styled_df = growth_df.style.map(color_diff, subset=["Diff (₹)", "Diff (%)"])
                    st.dataframe(styled_df, use_container_width=True, hide_index=True)

    # ----------------------------
    # DISPLAY COLUMN (Graph)
    # ----------------------------
    with display_col:
        if submitted:
            P = principal
            r = rate / 100
            t = years
            n = n_map[compounding]
            
            time_points = np.linspace(0, t, max(50, int(t * 12)))
            si_values = [P * (1 + r * T) for T in time_points]
            ci_values = [P * (1 + r / n) ** (n * T) for T in time_points]
            
            with st.container(border=True):
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=time_points, y=si_values, mode='lines', name='Simple Interest', line=dict(color='#38a169')))
                fig.add_trace(go.Scatter(x=time_points, y=ci_values, mode='lines', name='Compound Interest', line=dict(color='#2b6cb0')))
                fig.add_hline(y=P, line_dash="dot", line_color="gray", annotation_text="Principal")
                
                fig.update_layout(
                    title="Interest Growth Over Time",
                    xaxis_title="Time (Years)",
                    yaxis_title="Amount (₹)",
                    hovermode="x unified",
                    template="plotly_white",
                    height=500,
                    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
                )
                fig.update_yaxes(tickprefix="₹")
                st.plotly_chart(fig, use_container_width=True)
            
# ------------------------------------------------------------------
# RECURRING DEPOSIT PAGE
# ------------------------------------------------------------------
elif st.session_state.page == 'rd':
 
    st.divider()
    
    # ← Home button (top-left)
    col_home, title= st.columns([1,15,])
    with col_home:
        if st.button("← Home", key="home_rd", type="secondary", use_container_width=True):
            go_home()
            st.rerun()

    #st.title("Fixed Deposit Calculator")
    with title:
        st.markdown("""
        <style>
        .banner {
            background: linear-gradient(135deg, #f0f7ff 0%, #e6f2ff 100%);
            border-radius: 12px;
            padding: 5px;
            margin: 5px 0;
            border: 1px solid rgba(0, 86, 179, 0.15);
            text-align: center;
            font-size: 1.15rem;
            color: #0056b3;
            font-weight: 600;
        }
        </style>

        <div class="banner">
            Recurring Deposit Calculator
        </div>
        """, unsafe_allow_html=True)

    # Inside the 'rd' page block
    input_col, result_col, display_col = st.columns([0.2, 0.3, 0.5])

    with input_col:
        with st.form("rd_form"):
            monthly_deposit = st.number_input("Monthly Deposit (₹)", min_value=500, value=5000, step=500)
            rate = st.slider("Annual Interest Rate (%)", min_value=1.0, max_value=15.0, value=7.0, step=0.1)
            months = st.slider("Tenure (Months)", min_value=6, max_value=120, value=36, step=1)
            
            rd_type = st.radio(
                "Interest Type",
                ["Simple Interest", "Compound Interest", "Compare Both"],
                index=2
            )
            
            compounding = st.selectbox(
                "Compounding Frequency",
                ["Quarterly", "Monthly"],
                index=0,
                disabled=(rd_type == "Simple Interest")
            )
            
            submitted = st.form_submit_button("Calculate RD")

    with result_col:
        if submitted:
            P = monthly_deposit
            r = rate / 100
            n_months = months

            # --- Simple Interest RD ---
            # Each deposit earns simple interest for its remaining months
            maturity_simple = 0
            for m in range(1, n_months + 1):
                remaining_months = n_months - m
                time_years = remaining_months / 12
                maturity_simple += P * (1 + r * time_years)

            interest_simple = maturity_simple - (P * n_months)

            # --- Compound Interest RD ---
            if compounding == "Quarterly":
                i = r / 4
                maturity_compound = 0
                for m in range(1, n_months + 1):
                    quarters_left = (n_months - m) // 3
                    maturity_compound += P * (1 + i) ** quarters_left
            else:  # Monthly
                i = r / 12
                maturity_compound = 0
                for m in range(1, n_months + 1):
                    maturity_compound += P * (1 + i) ** (n_months - m)

            interest_compound = maturity_compound - (P * n_months)

            total_deposited = P * n_months

            # --- Metrics ---
            #st.markdown("### 📊 Results")
            if rd_type in ["Simple Interest", "Compare Both"]:
                    with st.container(border=True):
                        st.caption("🔹 Simple Interest RD")
                        c1, c2, c3 = st.columns(3)
                        c1.metric("Deposited", f"₹{total_deposited:,.0f}")
                        c2.metric("Maturity", f"₹{maturity_simple:,.0f}")
                        c3.metric("Interest", f"₹{interest_simple:,.0f}")
            
            if rd_type in ["Compound Interest", "Compare Both"]:
                    with st.container(border=True):
                        st.caption("🔸 Compound Interest RD")
                        c1, c2, c3 = st.columns(3)
                        c1.metric("Deposited", f"₹{total_deposited:,.0f}")
                        c2.metric("Maturity", f"₹{maturity_compound:,.0f}")
                        c3.metric("Interest", f"₹{interest_compound:,.0f}")

            with st.container(border=True):
                if rd_type == "Compare Both":
                    diff_amt = maturity_compound - maturity_simple
                    st.metric("📈 Extra Gain (Compound over Simple)", f"₹{diff_amt:,.0f}")

            # --- Tabs ---
            with st.container(border=True):
                tab_calc, tab_growth = st.tabs(["🧮 Calculation", "📊 Growth Table"])

                with tab_calc:
                    st.markdown("#### 📌 Simple Interest RD")
                    st.caption("Each monthly deposit earns simple interest for its remaining tenure.")
                    st.markdown(f"""
                    For a deposit made in month $ k $ (where $ k = 1 $ to $ {n_months} $),  
                    it remains invested for $ ({n_months} - k) $ months = $ \\frac{{{n_months} - k}}{{12}} $ years.

                    Maturity of deposit $ k $:  
                    $$
                    A_k = P \\left(1 + r \\cdot \\frac{{{n_months} - k}}{{12}}\\right)
                    $$

                    Total Maturity:
                    $$
                    A = \\sum_{{k=1}}^{{{n_months}}} A_k = \\sum_{{k=1}}^{{{n_months}}} {P} \\left(1 + {r} \\cdot \\frac{{{n_months} - k}}{{12}}\\right) = ₹{maturity_simple:,.0f}
                    $$
                    """)

                    st.markdown("#### 📌 Compound Interest RD")
                    if compounding == "Quarterly":
                        st.caption("Standard method: interest compounded every 3 months.")
                        st.markdown(f"""
                        For deposit $ k $, number of full quarters remaining = $ \\left\\lfloor \\frac{{{n_months} - k}}{{3}} \\right\\rfloor $

                        Maturity of deposit $ k $:  
                        $$
                        A_k = P \\left(1 + \\frac{{r}}{{4}}\\right)^{{\\left\\lfloor \\frac{{{n_months} - k}}{{3}} \\right\\rfloor}}
                        $$

                        Total Maturity:
                        $$
                        A = \\sum_{{k=1}}^{{{n_months}}} A_k = ₹{maturity_compound:,.0f}
                        $$
                        """)
                    else:  # Monthly
                        st.caption("Theoretical: interest compounded every month.")
                        st.markdown(f"""
                        For deposit $ k $, months remaining = $ {n_months} - k $

                        Maturity of deposit $ k $:  
                        $$
                        A_k = P \\left(1 + \\frac{{r}}{{12}}\\right)^{{{n_months} - k}}
                        $$

                        Total Maturity:
                        $$
                        A = \\sum_{{k=1}}^{{{n_months}}} A_k = ₹{maturity_compound:,.0f}
                        $$
                        """)

                with tab_growth:
                    # Build table at key intervals
                    step = max(3, months // 10)
                    time_points = list(range(0, months + 1, step))
                    if months not in time_points:
                        time_points.append(months)

                    rows = []
                    for m in time_points:
                        if m == 0:
                            si_val = ci_val = 0
                        else:
                            # Simple up to month m
                            si_val = sum(P * (1 + r * ((m - k) / 12)) for k in range(1, m + 1))
                            # Compound up to month m
                            if compounding == "Quarterly":
                                ci_val = sum(P * (1 + r/4) ** ((m - k) // 3) for k in range(1, m + 1))
                            else:
                                ci_val = sum(P * (1 + r/12) ** (m - k) for k in range(1, m + 1))
                        
                        diff = ci_val - si_val
                        pct_diff = (diff / si_val * 100) if si_val > 0 else 0
                        rows.append({
                            "Month": m,
                            "Simple (₹)": round(si_val, 2),
                            "Compound (₹)": round(ci_val, 2),
                            "Diff (₹)": round(diff, 2),
                            "Diff (%)": round(pct_diff, 2)
                        })

                    rd_df = pd.DataFrame(rows)
                    def color_diff(val):
                        color = '#4ade80' if val >= 0 else '#f87171'
                        return f'color: {color}; font-weight: bold'
                    styled_rd = rd_df.style.map(color_diff, subset=["Diff (₹)", "Diff (%)"])
                    st.dataframe(styled_rd, use_container_width=True, hide_index=True)

    with display_col:
        if submitted:
            months_arr = np.arange(0, months + 1)
            si_vals = []
            ci_vals = []
            for m in months_arr:
                if m == 0:
                    si_vals.append(0)
                    ci_vals.append(0)
                else:
                    si = sum(P * (1 + r * ((m - k) / 12)) for k in range(1, m + 1))
                    if compounding == "Quarterly":
                        ci = sum(P * (1 + r/4) ** ((m - k) // 3) for k in range(1, m + 1))
                    else:
                        ci = sum(P * (1 + r/12) ** (m - k) for k in range(1, m + 1))
                    si_vals.append(si)
                    ci_vals.append(ci)

            fig = go.Figure()
            if rd_type in ["Simple Interest", "Compare Both"]:
                fig.add_trace(go.Scatter(x=months_arr, y=si_vals, mode='lines', name='Simple Interest', line=dict(color='#38a169')))
            if rd_type in ["Compound Interest", "Compare Both"]:
                fig.add_trace(go.Scatter(x=months_arr, y=ci_vals, mode='lines', name='Compound Interest', line=dict(color='#2b6cb0')))
            
            fig.update_layout(
                title="RD Growth: Simple vs Compound Interest",
                xaxis_title="Months",
                yaxis_title="Amount (₹)",
                hovermode="x unified",
                template="plotly_white",
                height=500
            )
            fig.update_yaxes(tickprefix="₹")
            with st.container(border=True):
                st.plotly_chart(fig, use_container_width=True)
                     
# ------------------------------------------------------------------
# LOAN EMI PAGE
# ------------------------------------------------------------------
elif st.session_state.page == 'loan':

    st.divider()
    
    # ← Home button (top-left)
    col_home, title= st.columns([1,15,])
    with col_home:
        if st.button("← Home", key="home_loan", type="secondary", use_container_width=True):
            go_home()
            st.rerun()

    #st.title("Fixed Deposit Calculator")
    with title:
        st.markdown("""
        <style>
        .banner {
            background: linear-gradient(135deg, #f0f7ff 0%, #e6f2ff 100%);
            border-radius: 12px;
            padding: 5px;
            margin: 5px 0;
            border: 1px solid rgba(0, 86, 179, 0.15);
            text-align: center;
            font-size: 1.15rem;
            color: #0056b3;
            font-weight: 600;
        }
        </style>

        <div class="banner">
            Loan EMI Calculator
        </div>
        """, unsafe_allow_html=True)
        
    # Inside the 'loan' page block
    input_col, result_col, display_col = st.columns([0.2, 0.3, 0.5])

    with input_col:
        with st.form("loan_form"):
            loan_amount = st.number_input("Loan Amount (₹)", min_value=10000, value=500000, step=10000)
            rate = st.slider("Annual Interest Rate (%)", min_value=1.0, max_value=25.0, value=8.5, step=0.1)
            tenure_months = st.slider("Tenure (Months)", min_value=6, max_value=360, value=120, step=1)
            compare_mode = st.checkbox("Compare with Flat Rate", value=True)
            submitted = st.form_submit_button("Calculate EMI")

    with result_col:
        if submitted:
            P = loan_amount
            r = rate / 100
            n = tenure_months
            r_monthly = r / 12

            # --- Reducing Balance (Standard) ---
            if r_monthly > 0:
                emi_rb = P * r_monthly * (1 + r_monthly)**n / ((1 + r_monthly)**n - 1)
            else:
                emi_rb = P / n
            total_rb = emi_rb * n
            interest_rb = total_rb - P

            # Compute amortization schedule (for reducing balance only)
            balance = P
            schedule = []
            for month in range(1, n + 1):
                interest_part = balance * r_monthly
                principal_part = emi_rb - interest_part
                balance -= principal_part
                if balance < 0:
                    principal_part += balance
                    balance = 0
                schedule.append({
                    "Month": month,
                    "EMI (₹)": round(emi_rb, 2),
                    "Principal (₹)": round(principal_part, 2),
                    "Interest (₹)": round(interest_part, 2),
                    "Balance (₹)": round(balance, 2)
                })
                if balance <= 0:
                    break

            # --- Flat Rate (if enabled) ---
            if compare_mode:
                total_flat = P * (1 + r * (n / 12))
                emi_flat = total_flat / n
                interest_flat = total_flat - P

            # --- Metrics ---
            #st.markdown("### 📊 Loan Comparison")
            
            # Reducing Balance
            with st.container(border=True):
                st.caption("🔹 Reducing Balance (Standard)")
                c1, c2, c3 = st.columns(3)
                c1.metric("Loan", f"₹{P:,.0f}")
                c2.metric("EMI", f"₹{emi_rb:,.0f}")
                c3.metric("Total Int.", f"₹{interest_rb:,.0f}")

            # Flat Rate (if enabled)
            if compare_mode:
                with st.container(border=True):
                    st.caption("🔸 Flat Rate (Less Common)")
                    c1, c2, c3 = st.columns(3)
                    c1.metric("Loan", f"₹{P:,.0f}")
                    c2.metric("EMI", f"₹{emi_flat:,.0f}")
                    c3.metric("Total Int.", f"₹{interest_flat:,.0f}")
                    
            with st.container(border=True):
                extra_cost = interest_flat - interest_rb
                st.metric("⚠️ Extra Cost (Flat vs Reducing)", f"₹{extra_cost:,.0f}", delta="Higher!", delta_color="inverse")

            # --- Amortization Schedule (Reducing Balance Only) ---
            with st.container(border=True):
                tab_calc, tab_growth = st.tabs(["🧮 Calculation", "📉 Amortization Schedule (Reducing Balance)"])

                # --- Calculation Details ---
                with tab_calc:
                    st.markdown("#### Reducing Balance EMI Formula")
                    st.markdown(f"""
                    $$
                    EMI = P \\cdot \\frac{{r(1+r)^n}}{{(1+r)^n - 1}} = {P} \\cdot \\frac{{{r_monthly:.6f}(1+{r_monthly:.6f})^{{{n}}}}}{{(1+{r_monthly:.6f})^{{{n}}} - 1}} = ₹{emi_rb:,.0f}
                    $$
                    """)
                    if compare_mode:
                        st.markdown("#### Flat Rate Formula")
                        st.markdown(f"""
                        $$
                        \\text{{Total Payment}} = P(1 + r \\cdot t) = {P}(1 + {r} \\cdot {n/12}) = ₹{total_flat:,.0f}
                        $$
                        $$
                        EMI = \\frac{{\\text{{Total Payment}}}}{{n}} = \\frac{{{total_flat:,.0f}}}{{{n}}} = ₹{emi_flat:,.0f}
                        $$
                        """)
                
                with tab_growth:
                
                    #st.markdown("### 📉 Amortization Schedule (Reducing Balance)")
                    amort_df = pd.DataFrame(schedule)
                    st.dataframe(amort_df, use_container_width=True, hide_index=True, height=400)
                            
    with display_col:
        if submitted:

            # Plot: Reducing Balance EMI breakdown — PARALLEL BARS
            amort_df = pd.DataFrame(schedule)
            fig1 = go.Figure()

            fig1.add_trace(go.Bar(
                x=amort_df["Month"],
                y=amort_df["Principal (₹)"],
                name="Principal",
                marker_color="#4ade80"
            ))

            fig1.add_trace(go.Bar(
                x=amort_df["Month"],
                y=amort_df["Interest (₹)"],
                name="Interest",
                marker_color="#f87171"
            ))

            fig1.update_layout(
                title="Reducing Balance: EMI Breakdown",
                xaxis_title="Month",
                yaxis_title="Amount (₹)",
                barmode='group',  # ✅ Changed from 'stack' to 'group'
                template="plotly_white",
                height=400,
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )

            fig1.update_yaxes(tickprefix="₹")
            fig1.update_xaxes(rangeslider_visible=True)
            with st.container(border=True):
                st.plotly_chart(fig1, use_container_width=True)

            # If comparing, show pie charts
            if compare_mode:
                fig2 = go.Figure()
                fig2.add_trace(go.Pie(
                    labels=["Principal", "Interest"],
                    values=[P, interest_rb],
                    name="Reducing",
                    domain={'x': [0, 0.45]},
                    marker_colors=['#4a90e2', '#f56565']
                ))
                fig2.add_trace(go.Pie(
                    labels=["Principal", "Interest"],
                    values=[P, interest_flat],
                    name="Flat",
                    domain={'x': [0.55, 1]},
                    marker_colors=['#4a90e2', '#ed8936']
                ))
                fig2.update_layout(
                    title="Interest vs Principal: Reducing vs Flat",
                    annotations=[
                        dict(text="Reducing", x=0.22, y=0.5, font_size=12, showarrow=False),
                        dict(text="Flat", x=0.78, y=0.5, font_size=12, showarrow=False)
                    ],
                    height=350
                )
                with st.container(border=True):
                    st.plotly_chart(fig2, use_container_width=True)

# ------------------------------------------------------------------
# SIP PAGE
# ------------------------------------------------------------------                    
                    
elif st.session_state.page == 'sip':

    st.divider()
    
    # ← Home button (top-left)
    col_home, title= st.columns([1,15,])
    with col_home:
        if st.button("← Home", key="home_sip", type="secondary", use_container_width=True):
            go_home()
            st.rerun()

    with title:
        st.markdown("""
        <style>
        .banner {
            background: linear-gradient(135deg, #f0f7ff 0%, #e6f2ff 100%);
            border-radius: 12px;
            padding: 5px;
            margin: 5px 0;
            border: 1px solid rgba(0, 86, 179, 0.15);
            text-align: center;
            font-size: 1.15rem;
            color: #0056b3;
            font-weight: 600;
        }
        </style>

        <div class="banner">
            SIP Calculator
        </div>
        """, unsafe_allow_html=True)

    input_col, result_col, display_col = st.columns([0.2, 0.3, 0.5])

    with input_col:
        with st.form("sip_form"):
            monthly_invest = st.number_input("Monthly Investment (₹)", min_value=500, value=5000, step=500)
            rate = st.slider("Expected Annual Return (%)", min_value=4.0, max_value=20.0, value=12.0, step=0.5)
            years = st.slider("Investment Tenure (Years)", min_value=1, max_value=30, value=10, step=1)
            inflation = st.checkbox("Adjust for Inflation (6%)", value=False)
            compare_lumpsum = st.checkbox("Compare with Lumpsum", value=True)
            submitted = st.form_submit_button("Calculate")

    with result_col:
        if submitted:
            P = monthly_invest
            r = rate / 100
            n = years * 12
            monthly_r = r / 12

            # SIP Future Value
            if monthly_r > 0:
                fv_sip = P * (((1 + monthly_r)**n - 1) / monthly_r) * (1 + monthly_r)
            else:
                fv_sip = P * n

            total_invested = P * n

            # Lumpsum (same total invested as lumpsum at start)
            if compare_lumpsum:
                fv_lumpsum = total_invested * (1 + r)**years

            # Adjust for inflation
            inflation_rate = 0.06 if inflation else 0
            real_fv_sip = fv_sip / ((1 + inflation_rate) ** years)
            if compare_lumpsum:
                real_fv_lumpsum = fv_lumpsum / ((1 + inflation_rate) ** years)

            # Display
            with st.container(border=True):
                c1, c2, c3 = st.columns(3)
                c1.metric("Total Invested", f"₹{total_invested:,.0f}")
                
            with st.container(border=True):
                c1, c2, c3 = st.columns(3)
                c1.metric("SIP Maturity (Nominal)", f"₹{fv_sip:,.0f}")
                if inflation:
                    c2.metric("SIP Maturity (Real)", f"₹{real_fv_sip:,.0f}")

            if compare_lumpsum:
                with st.container(border=True):
                    c1, c2, c3 = st.columns(3)
                    c1.metric("Lumpsum Maturity (Nominal)", f"₹{fv_lumpsum:,.0f}")
                    if inflation:
                        c2.metric("Lumpsum Maturity (Real)", f"₹{real_fv_lumpsum:,.0f}")

            with st.expander("🧮 Formula", expanded=True):
                st.markdown(f"""
                **SIP Future Value**:  
                $$
                FV = P \\cdot \\frac{{(1 + r)^n - 1}}{{r}} \\cdot (1 + r)
                $$
                Where $ P = ₹{P} $, $ r = {monthly_r:.4f} $, $ n = {n} $
                """)

    with display_col:
        if submitted:
            months = np.arange(1, n + 1)
            sip_vals = []
            lumpsum_vals = []
            for m in months:
                # SIP up to month m
                if monthly_r > 0:
                    val = P * (((1 + monthly_r)**m - 1) / monthly_r) * (1 + monthly_r)
                else:
                    val = P * m
                sip_vals.append(val)
                
                # Lumpsum grows from day 1
                if compare_lumpsum:
                    lumpsum_vals.append(total_invested * (1 + r) ** (m / 12))

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=months/12, y=sip_vals, mode='lines', name='SIP', line=dict(color='#2563eb')))
            if compare_lumpsum:
                fig.add_trace(go.Scatter(x=months/12, y=lumpsum_vals, mode='lines', name='Lumpsum', line=dict(color='#dc2626')))
            fig.update_layout(
                title="SIP vs Lumpsum Growth",
                xaxis_title="Years",
                yaxis_title="Amount (₹)",
                hovermode="x unified",
                template="plotly_white",
                height=500
            )
            fig.update_yaxes(tickprefix="₹")
            with st.container(border=True):
                st.plotly_chart(fig, use_container_width=True)
                
# ------------------------------------------------------------------
# INCOME TAX PAGE
# ------------------------------------------------------------------                    
                    
elif st.session_state.page == 'tax':

    st.divider()
    
    # ← Home button (top-left)
    col_home, title= st.columns([1,15,])
    with col_home:
        if st.button("← Home", key="home_tax", type="secondary", use_container_width=True):
            go_home()
            st.rerun()

    #st.title("Fixed Deposit Calculator")
    with title:
        st.markdown("""
        <style>
        .banner {
            background: linear-gradient(135deg, #f0f7ff 0%, #e6f2ff 100%);
            border-radius: 12px;
            padding: 5px;
            margin: 5px 0;
            border: 1px solid rgba(0, 86, 179, 0.15);
            text-align: center;
            font-size: 1.15rem;
            color: #0056b3;
            font-weight: 600;
        }
        </style>

        <div class="banner">
            INCOME TAX Calculator (India - FY 2025-26)
        </div>
        """, unsafe_allow_html=True)
        
    input_col, result_col, display_col = st.columns([0.2, 0.3, 0.5])

    with input_col:
        with st.form("tax_form"):
            income = st.number_input("Annual Income (₹)", min_value=0, value=1000000, step=50000)
            
            st.divider()
            # Old Regime Deductions
            st.markdown("##### 📌 Old Regime Deductions")
            sec_80c = st.number_input("80C (PPF, ELSS, etc.)", min_value=0, max_value=150000, value=150000, step=10000)
            hra = st.number_input("HRA Exemption", min_value=0, value=0, step=10000)
            sec_80d = st.number_input("80D (Health Insurance)", min_value=0, max_value=50000, value=25000, step=5000)
            
            submitted = st.form_submit_button("Calculate Tax")

    with result_col:
        if submitted:
            # === NEW REGIME (default from FY 2023-24) ===
            # Slabs: 0-3L: 0%, 3-6L: 5%, 6-9L: 10%, 9-12L: 15%, 12-15L: 20%, >15L: 30%
            def calc_new_regime(income):
                tax = 0
                if income <= 300000:
                    return 0
                elif income <= 600000:
                    tax = (income - 300000) * 0.05
                elif income <= 900000:
                    tax = 15000 + (income - 600000) * 0.10
                elif income <= 1200000:
                    tax = 45000 + (income - 900000) * 0.15
                elif income <= 1500000:
                    tax = 90000 + (income - 1200000) * 0.20
                else:
                    tax = 150000 + (income - 1500000) * 0.30
                return tax + (0.04 * tax)  # +4% cess

            # === OLD REGIME ===
            def calc_old_regime(income, hra, sec_80c, sec_80d):
                taxable = income - hra - min(sec_80c, 150000) - min(sec_80d, 50000)
                if taxable < 0:
                    taxable = 0
                tax = 0
                if taxable <= 250000:
                    tax = 0
                elif taxable <= 500000:
                    tax = (taxable - 250000) * 0.05
                elif taxable <= 1000000:
                    tax = 12500 + (taxable - 500000) * 0.20
                else:
                    tax = 112500 + (taxable - 1000000) * 0.30
                return tax + (0.04 * tax)

            tax_new = calc_new_regime(income)
            tax_old = calc_old_regime(income, hra, sec_80c, sec_80d)

            take_home_new = income - tax_new
            take_home_old = income - tax_old

            with st.container(border=True):
                col1, col2 = st.columns(2)
                with col1:
                    st.caption("**🔹 New Regime**")
                    st.metric("Tax Payable", f"₹{tax_new:,.0f}")
                    st.metric("Take-Home", f"₹{take_home_new:,.0f}")
                with col2:
                    st.caption("**🔸 Old Regime**")
                    st.metric("Tax Payable", f"₹{tax_old:,.0f}")
                    st.metric("Take-Home", f"₹{take_home_old:,.0f}")

                better = "New Regime" if tax_new < tax_old else "Old Regime"
                savings = abs(tax_new - tax_old)
                st.success(f"💡 **{better} saves you ₹{savings:,.0f}**")

    with display_col:
        if submitted:
            labels = ['New Regime', 'Old Regime']
            taxes = [tax_new, tax_old]
            fig = go.Figure(data=[go.Bar(
                x=labels,
                y=taxes,
                marker_color=['#4ade80', '#f87171']
            )])
            fig.update_layout(
                title="Tax Payable Comparison",
                yaxis_title="Tax (₹)",
                template="plotly_white",
                height=400
            )
            fig.update_yaxes(tickprefix="₹")
            with st.container(border=True):
                st.plotly_chart(fig, use_container_width=True)
                
# ------------------------------------------------------------------
# CAGR PAGE
# ------------------------------------------------------------------                    
                    
elif st.session_state.page == 'cagr':

    st.divider()
    
    # ← Home button (top-left)
    col_home, title= st.columns([1,15,])
    with col_home:
        if st.button("← Home", key="home_cagr", type="secondary", use_container_width=True):
            go_home()
            st.rerun()

    #st.title("Fixed Deposit Calculator")
    with title:
        st.markdown("""
        <style>
        .banner {
            background: linear-gradient(135deg, #f0f7ff 0%, #e6f2ff 100%);
            border-radius: 12px;
            padding: 5px;
            margin: 5px 0;
            border: 1px solid rgba(0, 86, 179, 0.15);
            text-align: center;
            font-size: 1.15rem;
            color: #0056b3;
            font-weight: 600;
        }
        </style>

        <div class="banner">
            CAGR Calculator
        </div>
        """, unsafe_allow_html=True)

    input_col, result_col, display_col = st.columns([0.3, 0.3, 0.4])

    with input_col:
        with st.form("cagr_form"):
            st.markdown("#### Asset 1")
            initial1 = st.number_input("Initial Value (₹)", min_value=1, value=100000, step=10000, key="i1")
            final1 = st.number_input("Final Value (₹)", min_value=1, value=200000, step=10000, key="f1")
            years1 = st.number_input("Years", min_value=0.1, value=5.0, step=0.5, key="y1")
            
            st.markdown("#### Asset 2 (Optional)")
            initial2 = st.number_input("Initial Value (₹)", min_value=0, value=0, step=10000, key="i2")
            final2 = st.number_input("Final Value (₹)", min_value=0, value=0, step=10000, key="f2")
            years2 = st.number_input("Years", min_value=0.1, value=5.0, step=0.5, key="y2")
            
            submitted = st.form_submit_button("Calculate CAGR")

    with result_col:
        if submitted:
            def cagr(initial, final, years):
                if initial <= 0 or final <= 0 or years <= 0:
                    return None
                return (final / initial) ** (1 / years) - 1

            cagr1 = cagr(initial1, final1, years1)
            cagr2 = cagr(initial2, final2, years2) if initial2 > 0 and final2 > 0 else None

            st.markdown("### 📊 Results")
            if cagr1 is not None:
                st.metric("Asset 1 CAGR", f"{cagr1:.2%}")
            if cagr2 is not None:
                st.metric("Asset 2 CAGR", f"{cagr2:.2%}")
                diff = cagr1 - cagr2
                st.metric("Difference", f"{diff:.2%}", delta="Higher" if diff > 0 else "Lower")

            with st.expander("🧮 Formula"):
                st.markdown(r"""
                $$
                \text{CAGR} = \left( \frac{\text{Final Value}}{\text{Initial Value}} \right)^{\frac{1}{\text{Years}}} - 1
                $$
                """)

    with display_col:
        if submitted and cagr1 is not None:
            years_range = np.linspace(0, years1, 50)
            values1 = [initial1 * (1 + cagr1) ** y for y in years_range]
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=years_range, y=values1, mode='lines', name='Asset 1', line=dict(color='#2563eb')))
            
            if cagr2 is not None:
                years_range2 = np.linspace(0, years2, 50)
                values2 = [initial2 * (1 + cagr2) ** y for y in years_range2]
                fig.add_trace(go.Scatter(x=years_range2, y=values2, mode='lines', name='Asset 2', line=dict(color='#dc2626')))
            
            fig.update_layout(
                title="Growth Over Time",
                xaxis_title="Years",
                yaxis_title="Value (₹)",
                hovermode="x unified",
                template="plotly_white",
                height=500
            )
            fig.update_yaxes(tickprefix="₹")
            st.plotly_chart(fig, use_container_width=True)

# ------------------------------------------------------------------
# RETIREMENT PAGE
# ------------------------------------------------------------------             

elif st.session_state.page == 'retirement':

    st.divider()
    
    # ← Home button (top-left)
    col_home, title= st.columns([1,15,])
    with col_home:
        if st.button("← Home", key="home_tax", type="secondary", use_container_width=True):
            go_home()
            st.rerun()

    with title:
        st.markdown("""
        <style>
        .banner {
            background: linear-gradient(135deg, #f0f7ff 0%, #e6f2ff 100%);
            border-radius: 12px;
            padding: 5px;
            margin: 5px 0;
            border: 1px solid rgba(0, 86, 179, 0.15);
            text-align: center;
            font-size: 1.15rem;
            color: #0056b3;
            font-weight: 600;
        }
        </style>

        <div class="banner">
            Retirement Planning Calculator
        </div>
        """, unsafe_allow_html=True)

    input_col, result_col, display_col = st.columns([0.2, 0.3, 0.54])

    with input_col:
        with st.form("retire_form"):
            current_age = st.number_input("Current Age", min_value=20, max_value=70, value=35)
            retire_age = st.number_input("Retirement Age", min_value=40, max_value=80, value=60)
            monthly_expense = st.number_input("Monthly Expense Today (₹)", min_value=5000, value=50000, step=5000)
            st.divider()
            inflation = st.slider("Inflation Rate (%)", min_value=3.0, max_value=10.0, value=6.0, step=0.5)
            roi_post = st.slider("Post-Retirement ROI (%)", min_value=3.0, max_value=10.0, value=7.0, step=0.5)
            roi_pre = st.slider("Pre-Retirement ROI (%)", min_value=6.0, max_value=15.0, value=10.0, step=0.5)
            instrument = st.selectbox("Investment Instrument", ["None", "EPF (8.15%)", "PPF (7.1%)", "NPS (10%)"])
            submitted = st.form_submit_button("Calculate")

    with result_col:
        if submitted:
            # Override ROI based on instrument
            instrument_roi = {"EPF (8.15%)": 8.15, "PPF (7.1%)": 7.1, "NPS (10%)": 10.0}.get(instrument, None)
            if instrument_roi:
                roi_pre = instrument_roi

            years_to_retire = retire_age - current_age
            years_in_retirement = 85 - retire_age  # assume life till 85

            # Future monthly expense at retirement
            future_monthly = monthly_expense * ((1 + inflation / 100) ** years_to_retire)
            # Annual expense
            annual_expense = future_monthly * 12
            # Retirement corpus (PV of annuity)
            r = roi_post / 100
            if r > 0:
                corpus = annual_expense * (1 - (1 + r) ** (-years_in_retirement)) / r
            else:
                corpus = annual_expense * years_in_retirement

            # Monthly savings needed
            n = years_to_retire * 12
            r_monthly = (roi_pre / 100) / 12
            if r_monthly > 0:
                monthly_savings = corpus * r_monthly / ((1 + r_monthly) ** n - 1)
            else:
                monthly_savings = corpus / n

            with st.container(border=True):
                c1, c2 = st.columns(2)
                c1.metric("Retirement Corpus Needed", f"₹{corpus:,.0f}")
                c2.metric("Monthly Savings Required", f"₹{monthly_savings:,.0f}")
                st.caption(f"Based on {instrument if instrument != 'None' else 'Custom'} ROI")

    with display_col:
        if submitted:
            # Show expense growth and corpus buildup
            years = np.arange(0, years_to_retire + 1)
            expenses = [monthly_expense * ((1 + inflation/100) ** y) for y in years]
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=years + current_age, y=expenses, mode='lines', name='Monthly Expense (Future Value)'))
            fig.update_layout(
                title="Future Monthly Expense at Retirement",
                xaxis_title="Age",
                yaxis_title="Expense (₹)",
                template="plotly_white",
                height=400
            )
            fig.update_yaxes(tickprefix="₹")
            with st.container(border=True):
                st.plotly_chart(fig, use_container_width=True)

# ------------------------------------------------------------------
# EMERGENCY FUND PAGE
# ------------------------------------------------------------------              

elif st.session_state.page == 'emergency':
    col_home, _ = st.columns([1, 9])
    with col_home:
        if st.button("← Home", key="home_emergency", type="secondary", use_container_width=True):
            go_home()
            st.rerun()

    st.title("Emergency Fund Calculator")

    input_col, result_col, display_col = st.columns([0.3, 0.3, 0.4])

    with input_col:
        with st.form("emergency_form"):
            monthly_expense = st.number_input("Monthly Essential Expenses (₹)", min_value=5000, value=40000, step=5000)
            months_cover = st.slider("Coverage (Months)", min_value=3, max_value=12, value=6, step=1)
            current_fund = st.number_input("Current Emergency Fund (₹)", min_value=0, value=100000, step=10000)
            submitted = st.form_submit_button("Calculate")

    with result_col:
        if submitted:
            recommended = monthly_expense * months_cover
            gap = max(0, recommended - current_fund)

            st.markdown("### 📊 Results")
            st.metric("Recommended Fund", f"₹{recommended:,.0f}")
            st.metric("Current Fund", f"₹{current_fund:,.0f}")
            st.metric("Gap to Fill", f"₹{gap:,.0f}")

            if gap <= 0:
                st.success("✅ You're fully covered!")
            else:
                months_to_save = gap / (monthly_expense * 0.2)  # assuming 20% savings
                st.warning(f"💡 Save ₹{gap/months_to_save:,.0f}/month for {months_to_save:.1f} months")

    with display_col:
        if submitted:
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=current_fund / recommended * 100 if recommended > 0 else 0,
                title={'text': "Emergency Fund Status"},
                gauge={
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "#4ade80" if current_fund >= recommended else "#f87171"},
                    'steps': [
                        {'range': [0, 50], 'color': "#fee2e2"},
                        {'range': [50, 100], 'color': "#dcfce7"}
                    ],
                    'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 100}
                }
            ))
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)

# ------------------------------------------------------------------
# HOME AFFORDABILITY PAGE
# ------------------------------------------------------------------ 
            
elif st.session_state.page == 'home_af':

    st.divider()
    
    # ← Home button (top-left)
    col_home, title= st.columns([1,15,])
    with col_home:
        if st.button("← Home", key="home_tax", type="secondary", use_container_width=True):
            go_home()
            st.rerun()

    with title:
        st.markdown("""
        <style>
        .banner {
            background: linear-gradient(135deg, #f0f7ff 0%, #e6f2ff 100%);
            border-radius: 12px;
            padding: 5px;
            margin: 5px 0;
            border: 1px solid rgba(0, 86, 179, 0.15);
            text-align: center;
            font-size: 1.15rem;
            color: #0056b3;
            font-weight: 600;
        }
        </style>

        <div class="banner">
            Home Affordability Calculator
        </div>
        """, unsafe_allow_html=True)

    #st.title("Home Affordability Calculator")

    input_col, result_col, display_col = st.columns([0.2, 0.3, 0.5])

    with input_col:
        with st.form("home_form"):
            annual_income = st.number_input("Annual Income (₹)", min_value=300000, value=1200000, step=100000)
            down_payment = st.number_input("Down Payment (₹)", min_value=100000, value=1000000, step=100000)
            st.divider()
            interest_rate = st.slider("Home Loan Interest (%)", min_value=6.0, max_value=12.0, value=8.5, step=0.1)
            loan_tenure = st.slider("Loan Tenure (Years)", min_value=5, max_value=30, value=20, step=1)
            st.divider()
            property_tax = st.number_input("Annual Property Tax (₹)", min_value=0, value=20000, step=5000)
            insurance = st.number_input("Annual Insurance (₹)", min_value=0, value=10000, step=1000)
            maintenance = st.number_input("Annual Maintenance (₹)", min_value=0, value=30000, step=5000)
            submitted = st.form_submit_button("Calculate")

    with result_col:
        if submitted:
            # Max EMI (typically 60% of monthly income)
            monthly_income = annual_income / 12
            max_emi = monthly_income * 0.6

            # Loan amount based on EMI
            r = interest_rate / 100 / 12
            n = loan_tenure * 12
            if r > 0:
                loan_amount = max_emi * ((1 + r)**n - 1) / (r * (1 + r)**n)
            else:
                loan_amount = max_emi * n

            home_price = loan_amount + down_payment
            total_annual_cost = property_tax + insurance + maintenance + (max_emi * 12)

            with st.container(border=True):
                c1, c2 = st.columns(2)
                c1.metric("Max Home Price", f"₹{home_price:,.0f}")
                c2.metric("Loan Eligible", f"₹{loan_amount:,.0f}")
                
            with st.container(border=True):
                c1, c2 = st.columns(2)                
                c1.metric("Monthly EMI", f"₹{max_emi:,.0f}")
                c2.metric("Total Annual Cost", f"₹{total_annual_cost:,.0f}")

    with display_col:
        if submitted:
            labels = ['Down Payment', 'Loan Amount']
            values = [down_payment, loan_amount]
            fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.4)])
            fig.update_layout(title="Home Purchase Breakdown", height=400)
            
            with st.container(border=True):
                st.plotly_chart(fig, use_container_width=True)
            
# ------------------------------------------------------------------
# CAR LOAN & DEPRECIATION PAGE
# ------------------------------------------------------------------ 
            
elif st.session_state.page == 'car':

    st.divider()
    
    # ← Home button (top-left)
    col_home, title= st.columns([1,15,])
    with col_home:
        if st.button("← Home", key="home_tax", type="secondary", use_container_width=True):
            go_home()
            st.rerun()

    with title:
        st.markdown("""
        <style>
        .banner {
            background: linear-gradient(135deg, #f0f7ff 0%, #e6f2ff 100%);
            border-radius: 12px;
            padding: 5px;
            margin: 5px 0;
            border: 1px solid rgba(0, 86, 179, 0.15);
            text-align: center;
            font-size: 1.15rem;
            color: #0056b3;
            font-weight: 600;
        }
        </style>

        <div class="banner">
            Car Loan & Depreciation Calculator
        </div>
        """, unsafe_allow_html=True)

    #st.title("Car Loan & Depreciation Calculator")

    input_col, result_col, display_col = st.columns([0.2, 0.3, 0.5])

    with input_col:
        with st.form("car_form"):
            car_price = st.number_input("Car Price (₹)", min_value=100000, value=1000000, step=50000)
            down_payment = st.number_input("Down Payment (₹)", min_value=0, value=200000, step=10000)
            st.divider()
            interest_rate = st.slider("Loan Interest (%)", min_value=7.0, max_value=14.0, value=9.0, step=0.1)
            loan_tenure = st.slider("Loan Tenure (Years)", min_value=1, max_value=7, value=5, step=1)
            depreciation = st.slider("Annual Depreciation (%)", min_value=10.0, max_value=30.0, value=20.0, step=1.0)
            submitted = st.form_submit_button("Calculate")

    with result_col:
        if submitted:
            loan_amount = car_price - down_payment
            r = interest_rate / 100 / 12
            n = loan_tenure * 12
            if r > 0:
                emi = loan_amount * r * (1 + r)**n / ((1 + r)**n - 1)
            else:
                emi = loan_amount / n

            total_payment = emi * n
            total_interest = total_payment - loan_amount

            # Depreciation over 5 years
            years = np.arange(0, 6)
            resale_values = [car_price * ((1 - depreciation/100) ** y) for y in years]

            with st.container(border=True):
                c1, c2, c3 = st.columns(3)
                c1.metric("Loan Amount", f"₹{loan_amount:,.0f}")
                c2.metric("EMI", f"₹{emi:,.0f}")
                c3.metric("Total Interest", f"₹{total_interest:,.0f}")

            with st.container(border=True):
                c1, c2, c3 = st.columns(3)                
                c1.metric("Resale Value (Year 5)", f"₹{resale_values[5]:,.0f}")

    with display_col:
        if submitted:
            years = np.arange(0, 6)
            resale_values = [car_price * ((1 - depreciation/100) ** y) for y in years]
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=years, y=resale_values, mode='lines+markers', name='Resale Value'))
            fig.update_layout(
                title="Car Depreciation Over Time",
                xaxis_title="Years",
                yaxis_title="Value (₹)",
                template="plotly_white",
                height=400
            )
            fig.update_yaxes(tickprefix="₹")
            with st.container(border=True):
                st.plotly_chart(fig, use_container_width=True)

# ------------------------------------------------------------------
# INFLATION IMPACT PAGE
# ------------------------------------------------------------------ 
            
elif st.session_state.page == 'inflation':
    
    st.divider()
    
    # ← Home button (top-left)
    col_home, title= st.columns([1,15,])
    with col_home:
        if st.button("← Home", key="home_tax", type="secondary", use_container_width=True):
            go_home()
            st.rerun()

    with title:
        st.markdown("""
        <style>
        .banner {
            background: linear-gradient(135deg, #f0f7ff 0%, #e6f2ff 100%);
            border-radius: 12px;
            padding: 5px;
            margin: 5px 0;
            border: 1px solid rgba(0, 86, 179, 0.15);
            text-align: center;
            font-size: 1.15rem;
            color: #0056b3;
            font-weight: 600;
        }
        </style>

        <div class="banner">
            Inflation Impact Calculator
        </div>
        """, unsafe_allow_html=True)

    #st.title("Inflation Impact Calculator")

    input_col, result_col, display_col = st.columns([0.2, 0.3, 0.5])

    with input_col:
        
        with st.form("inflation_form"):
            calc_type = st.radio("Calculation Type", ["Future Value", "Present Value"])
            st.divider()
            if calc_type == "Future Value":
                present_value = st.number_input("Amount Today (₹)", min_value=1000, value=100000, step=10000)
                years = st.slider("Years", min_value=1, max_value=30, value=10, step=1)
            else:
                future_value = st.number_input("Future Amount (₹)", min_value=1000, value=200000, step=10000)
                years = st.slider("Years", min_value=1, max_value=30, value=10, step=1)
            inflation = st.slider("Inflation Rate (%)", min_value=3.0, max_value=12.0, value=6.0, step=0.5)
            submitted = st.form_submit_button("Calculate")

    with result_col:
        if submitted:
            if calc_type == "Future Value":
                future_val = present_value * ((1 + inflation/100) ** years)
                with st.container(border=True):
                    c1, c2, c3 = st.columns(3)
                    c1.metric("Future Value", f"₹{future_val:,.0f}")
                    st.caption(f"₹{present_value:,.0f} today will be worth ₹{future_val:,.0f} in {years} years")
            else:
                present_val = future_value / ((1 + inflation/100) ** years)
                with st.container(border=True):
                    c1, c2, c3 = st.columns(3)
                    c1.metric("Present Value", f"₹{present_val:,.0f}")
                    st.caption(f"You need ₹{present_val:,.0f} today to have ₹{future_value:,.0f} in {years} years")

    with display_col:
        if submitted:
            years_range = np.arange(0, years + 1)
            if calc_type == "Future Value":
                values = [present_value * ((1 + inflation/100) ** y) for y in years_range]
                title = "Purchasing Power Erosion"
            else:
                values = [future_value / ((1 + inflation/100) ** (years - y)) for y in years_range]
                title = "Required Investment Growth"

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=years_range, y=values, mode='lines', name='Value'))
            fig.update_layout(
                title=title,
                xaxis_title="Years",
                yaxis_title="Amount (₹)",
                template="plotly_white",
                height=400
            )
            fig.update_yaxes(tickprefix="₹")
            with st.container(border=True):
                st.plotly_chart(fig, use_container_width=True)

# ------------------------------------------------------------------
# PPF / Sukanya Samriddhi / NSC PAGE
# ------------------------------------------------------------------ 
            
elif st.session_state.page == 'tax_saving':

    st.divider()
    
    # ← Home button (top-left)
    col_home, title= st.columns([1,15,])
    with col_home:
        if st.button("← Home", key="home_tax", type="secondary", use_container_width=True):
            go_home()
            st.rerun()

    with title:
        st.markdown("""
        <style>
        .banner {
            background: linear-gradient(135deg, #f0f7ff 0%, #e6f2ff 100%);
            border-radius: 12px;
            padding: 5px;
            margin: 5px 0;
            border: 1px solid rgba(0, 86, 179, 0.15);
            text-align: center;
            font-size: 1.15rem;
            color: #0056b3;
            font-weight: 600;
        }
        </style>

        <div class="banner">
            Tax-Saving Instruments Calculator | PPF / Sukanya Samriddhi / NSC
        </div>
        """, unsafe_allow_html=True)

    #st.title("Tax-Saving Instruments Calculator")

    input_col, result_col, display_col = st.columns([0.2, 0.3, 0.5])

    with input_col:
        
        with st.form("tax_saving_form"):
            instrument = st.selectbox("Instrument", ["PPF", "Sukanya Samriddhi", "NSC"])
            st.divider()
            yearly_deposit = st.number_input("Yearly Deposit (₹)", min_value=1000, max_value=150000, value=150000, step=5000)
            years = st.slider("Tenure (Years)", min_value=5, max_value=20, 
                              value={"PPF": 15, "Sukanya Samriddhi": 14, "NSC": 5}[instrument], 
                              step=1, disabled=True)
            submitted = st.form_submit_button("Calculate")

    with result_col:
        if submitted:
            # Current rates (as of 2025)
            rates = {"PPF": 7.1, "Sukanya Samriddhi": 8.2, "NSC": 7.7}
            rate = rates[instrument]
            r = rate / 100

            # PPF/Sukanya: compounding annually, deposit at year start
            maturity = 0
            balance = 0
            for y in range(years):
                balance = (balance + yearly_deposit) * (1 + r)
                maturity = balance

            total_invested = yearly_deposit * years
            interest_earned = maturity - total_invested

            with st.container(border=True):
                c1, c2, c3 = st.columns(3)
                c1.metric("Total Invested", f"₹{total_invested:,.0f}")
                c2.metric("Maturity Amount", f"₹{maturity:,.0f}")
                c3.metric("Interest Earned", f"₹{interest_earned:,.0f}")
                st.caption(f"Interest Rate: {rate}% (as of 2025)")

    with display_col:
        if submitted:
            # Year-wise growth
            balance = 0
            years_list = []
            balances = []
            for y in range(1, years + 1):
                balance = (balance + yearly_deposit) * (1 + r)
                years_list.append(y)
                balances.append(balance)

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=years_list, y=balances, mode='lines+markers', name='Maturity Value'))
            fig.update_layout(
                title=f"{instrument} Growth Over Time",
                xaxis_title="Years",
                yaxis_title="Amount (₹)",
                template="plotly_white",
                height=400
            )
            fig.update_yaxes(tickprefix="₹")
            with st.container(border=True):
                st.plotly_chart(fig, use_container_width=True)
