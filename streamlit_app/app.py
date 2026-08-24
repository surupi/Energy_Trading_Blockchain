import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from web3_service import Web3Service

# Page Config
st.set_page_config(
    page_title="Energy Trading DEX",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Clean, Modern Light Mode Design System
st.markdown("""
<style>
    /* Global Background & Text */
    .stApp {
        background-color: #f8fafc;
        color: #0f172a;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e2e8f0;
    }
    
    /* Custom Card Containers */
    .energy-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
    }
    
    .metric-card {
        background: #ffffff;
        border: 1px solid #cbd5e1;
        border-radius: 12px;
        padding: 18px 20px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    
    .metric-value {
        font-size: 28px;
        font-weight: 700;
        color: #0284c7;
        margin-top: 4px;
    }
    
    .metric-label {
        font-size: 13px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #64748b;
    }
    
    /* Custom Badges */
    .energy-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 16px;
        font-size: 12px;
        font-weight: 600;
        background: #e0f2fe;
        color: #0369a1;
        border: 1px solid #bae6fd;
    }
    
    .price-tag {
        font-size: 20px;
        font-weight: 700;
        color: #059669;
    }

    .wallet-box {
        background: #f1f5f9;
        padding: 14px;
        border-radius: 10px;
        border: 1px solid #e2e8f0;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Web3 Service
web3_service = Web3Service()

# Session State for Mock Orders
if "listings" not in st.session_state:
    st.session_state["listings"] = web3_service.get_mock_listings()

if "transactions" not in st.session_state:
    st.session_state["transactions"] = web3_service.get_mock_transactions()

# Sidebar Navigation
st.sidebar.title("⚡ Energy DEX")
st.sidebar.caption("Decentralized P2P Microgrid Exchange")

role = st.sidebar.selectbox("Active Account Role", ["Seller (Prosumer)", "Buyer (Consumer)", "Grid Operator"])
account = st.sidebar.selectbox("Connected Wallet", web3_service.get_accounts())
balance = web3_service.get_balance(account)
st.sidebar.markdown(f"""
<div class="wallet-box">
    <span style="color:#64748b; font-size:12px; font-weight:600;">WALLET BALANCE</span><br>
    <strong style="color:#059669; font-size:18px;">{balance:.4f} ETH</strong>
</div>
""", unsafe_allow_html=True)

nav = st.sidebar.radio("Navigation", [
    "🛒 Marketplace & Orderbook", 
    "📊 Telemetry & Smart Meter", 
    "📈 Analytics & Ledger", 
    "🔗 Chainlink Oracles"
])

st.sidebar.markdown("---")
st.sidebar.caption("Network: **Ethereum Local (Ganache/Hardhat)**")
st.sidebar.caption(f"Status: **{'Connected' if web3_service.connected else 'Simulated Mode'}**")

# --- VIEW 1: MARKETPLACE & ORDERBOOK ---
if nav == "🛒 Marketplace & Orderbook":
    st.title("⚡ P2P Energy Marketplace")
    st.caption("Direct microgrid clean energy trading powered by smart contracts")

    col1, col2, col3 = st.columns(3)
    active_listings = [l for l in st.session_state["listings"] if l["active"]]
    active_count = len(active_listings)
    total_volume = sum([l["units"] for l in active_listings])
    avg_price = np.mean([l["price_per_unit_eth"] for l in active_listings]) if active_count > 0 else 0

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Active Listings</div>
            <div class="metric-value">{active_count} Offers</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Available Energy</div>
            <div class="metric-value">{total_volume} kWh</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Avg Price / kWh</div>
            <div class="metric-value">{avg_price:.4f} ETH</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["🛒 Live Orderbook", "➕ Post Energy Listing"])

    with tab1:
        st.subheader("Available Energy Sell Listings")
        if not active_listings:
            st.warning("No active listings currently available.")
        else:
            for l in active_listings:
                st.markdown(f"""
                <div class="energy-card">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <span class="energy-badge">{l['energy_type']}</span>
                            <span style="margin-left: 10px; color: #64748b; font-size: 13px; font-weight: 500;">Listing #{l['id']}</span>
                            <h3 style="margin: 8px 0 2px 0; color: #0f172a;">{l['units']} kWh Available</h3>
                            <span style="font-size: 13px; color: #475569;">Seller: <code>{l['seller'][:14]}...</code></span>
                        </div>
                        <div style="text-align: right;">
                            <div class="price-tag">{l['price_per_unit_eth']} ETH <span style="font-size:13px; font-weight:normal; color:#64748b;">/ kWh</span></div>
                            <div style="font-size: 13px; color: #64748b; margin-top:4px;">Total Lot: <strong>{(l['units'] * l['price_per_unit_eth']):.4f} ETH</strong></div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                # Action Row aligned vertically
                c_qty, c_btn = st.columns([3, 1], vertical_alignment="bottom")
                buy_qty = c_qty.number_input(f"Quantity (kWh) to buy from Lot #{l['id']}", min_value=1, max_value=l['units'], value=min(10, l['units']), key=f"qty_{l['id']}")
                
                if c_btn.button(f"Buy {buy_qty} kWh", key=f"btn_buy_{l['id']}", type="primary", use_container_width=True):

                    total_cost = buy_qty * l['price_per_unit_eth']
                    l['units'] -= buy_qty
                    if l['units'] == 0:
                        l['active'] = False
                    st.session_state["transactions"].append({
                        "id": len(st.session_state["transactions"]) + 100,
                        "listing_id": l['id'],
                        "buyer": account,
                        "seller": l['seller'],
                        "units": buy_qty,
                        "total_cost_eth": total_cost,
                        "timestamp": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
                    st.success(f"Transaction Confirmed! Bought {buy_qty} kWh for {total_cost:.4f} ETH.")
                    st.rerun()

    with tab2:
        st.subheader("Post Surplus Energy Listing")
        with st.form("create_listing_form"):
            e_type = st.selectbox("Energy Source", ["Solar PV", "Wind Power", "Biomass / Hydro", "Battery Storage"])
            units = st.number_input("Energy Quantity (kWh)", min_value=1, max_value=1000, value=50)
            price_per_unit = st.number_input("Price per kWh (ETH)", min_value=0.0001, max_value=0.1, value=0.0020, step=0.0001, format="%.4f")
            
            submitted = st.form_submit_button("Post Listing to Smart Contract", use_container_width=True, type="primary")
            if submitted:
                new_id = len(st.session_state["listings"])
                st.session_state["listings"].append({
                    "id": new_id,
                    "seller": account,
                    "units": units,
                    "price_per_unit_eth": price_per_unit,
                    "total_cost_eth": units * price_per_unit,
                    "energy_type": e_type,
                    "active": True
                })
                st.success(f"Listing #{new_id} created successfully!")
                st.rerun()

# --- VIEW 2: TELEMETRY & SMART METER ---
elif nav == "📊 Telemetry & Smart Meter":
    st.title("📊 Smart Meter Telemetry")
    st.caption("Real-time microgrid IoT telemetry & smart contract automation")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("☀️ Generation vs Consumption")
        solar_output = st.slider("Solar PV Output (kWh)", 0.0, 20.0, 10.5, 0.5)
        home_load = st.slider("Household Load (kWh)", 0.0, 20.0, 4.2, 0.5)

        net_grid = solar_output - home_load
        
        if net_grid > 0:
            st.success(f"**Surplus Generation:** +{net_grid:.2f} kWh (Available for P2P Sale)")
        elif net_grid < 0:
            st.warning(f"**Grid Deficit:** {net_grid:.2f} kWh (Import Required)")
        else:
            st.info("**Balanced Microgrid Node**")

    with col2:
        st.subheader("⚡ Automated Trading Rules")
        auto_trade = st.toggle("Enable Smart-Contract Auto-Listing", value=True)
        min_threshold = st.number_input("Trigger Threshold (kWh Surplus)", value=2.0)

        if auto_trade and net_grid >= min_threshold:
            st.info(f"Smart Meter Rule Matched: Surplus ({net_grid:.1f} kWh) exceeds threshold ({min_threshold} kWh)")
            if st.button("Execute Auto-Listing On-Chain", type="primary", use_container_width=True):
                new_id = len(st.session_state["listings"])
                st.session_state["listings"].append({
                    "id": new_id,
                    "seller": account,
                    "units": int(net_grid),
                    "price_per_unit_eth": 0.0019,
                    "total_cost_eth": net_grid * 0.0019,
                    "energy_type": "Solar PV (IoT Telemetry)",
                    "active": True
                })
                st.success(f"Smart Meter automatically listed {int(net_grid)} kWh on-chain!")

    st.markdown("---")
    st.subheader("📈 24-Hour Microgrid Load Profile")
    hours = [f"{h:02d}:00" for h in range(24)]
    solar_curve = [0,0,0,0,0,0, 1.2, 3.5, 6.8, 9.5, 11.2, 12.0, 11.5, 9.8, 7.1, 4.2, 1.5, 0,0,0,0,0,0,0]
    load_curve = [1.5, 1.2, 1.1, 1.0, 1.2, 2.5, 4.5, 3.8, 3.2, 3.0, 3.1, 3.5, 3.2, 3.0, 3.4, 4.2, 6.5, 7.2, 6.8, 5.2, 3.8, 2.5, 1.8, 1.5]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=hours, y=solar_curve, mode='lines+markers', name='Solar Production (kWh)', line=dict(color='#f59e0b', width=3)))
    fig.add_trace(go.Scatter(x=hours, y=load_curve, mode='lines+markers', name='Household Load (kWh)', line=dict(color='#0284c7', width=3)))
    fig.update_layout(template="plotly_white", height=380, margin=dict(l=20, r=20, t=30, b=20), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)

# --- VIEW 3: ANALYTICS & LEDGER ---
elif nav == "📈 Analytics & Ledger":
    st.title("📈 Analytics & Transaction Ledger")

    df_tx = pd.DataFrame(st.session_state["transactions"])
    
    col1, col2 = st.columns(2)
    col1.metric("Settled Transactions", len(df_tx))
    col2.metric("Total ETH Traded", f"{df_tx['total_cost_eth'].sum():.4f} ETH")

    st.markdown("---")
    st.subheader("📜 Blockchain Transaction History")
    st.dataframe(df_tx, use_container_width=True)

    st.subheader("📊 Trade Volume Distribution")
    fig_bar = px.bar(df_tx, x="id", y="units", color="units", labels={"id": "Tx ID", "units": "kWh Traded"}, template="plotly_white")
    fig_bar.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig_bar, use_container_width=True)

# --- VIEW 4: CHAINLINK ORACLES ---
elif nav == "🔗 Chainlink Oracles":
    st.title("🔗 Chainlink Oracles & Data Feeds")
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("ETH/USD Price Oracle")
        st.metric("Oracle ETH Price", "$2,850.42", delta="+2.4%")
        st.caption("Contract: `0x694AA1769357215DE4FAC081bf1f309aDC325306`")

    with col2:
        st.subheader("Direct Smart Meter Verification")
        if st.button("Request Oracle Data Fulfillment (LINK)", type="primary"):
            st.info("Chainlink Oracle Job Triggered...")
            st.success("Fulfilled on-chain by Oracle Node `0xec39A0C...`!")

    st.markdown("---")
    st.subheader("Oracle Audit Logs")
    logs = [
        {"Job ID": "f3d904c3519a43c69b0aba5b6d7a78f6", "Node": "0xec39A0C2...", "Type": "Production Telemetry", "Status": "Fulfilled"},
        {"Job ID": "11e8ab573ede4b978b4dd0619c44d467", "Node": "0xec39A0C2...", "Type": "Consumption Telemetry", "Status": "Fulfilled"}
    ]
    st.table(logs)
