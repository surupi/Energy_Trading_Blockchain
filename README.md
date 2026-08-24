# ⚡ Peer-to-Peer Energy Trading Blockchain & Streamlit DEX

[![Solidity](https://img.shields.io/badge/Solidity-^0.8.0-363636?style=for-the-badge&logo=solidity)](https://soliditylang.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![Chainlink](https://img.shields.io/badge/Chainlink-Oracles-375BD2?style=for-the-badge&logo=chainlink)](https://chain.link/)
[![Web3.py](https://img.shields.io/badge/Web3.py-6.15+-F7931A?style=for-the-badge&logo=ethereum)](https://web3py.readthedocs.io/)

A decentralized Peer-to-Peer (P2P) energy trading platform that empowers prosumers (producers + consumers) to trade surplus renewable energy (Solar, Wind, Biomass) directly over an Ethereum microgrid using smart contracts, real-time IoT smart meter telemetry, and interactive Streamlit analytics.

---

## 📋 Executive Summary & Project Report

### 🎯 Key Objectives
1. **Assessment of Blockchain's Feasibility:** Evaluate the suitability of Ethereum smart contracts in facilitating transparent, tamper-proof, and secure peer-to-peer energy trading in decentralized microgrids.
2. **Decentralization Impact:** Analyze how peer-to-peer networks eliminate utility intermediaries, reducing transaction fees and improving green energy accessibility.
3. **Smart Contract Architecture:** Implement secure Solidity contracts (`MarketContract.sol`, `EnergySwapToken.sol`, `UserContract.sol`, `EnergyDataContract.sol`) for automated execution, reentrancy-safe payments, and partial order fills.
4. **Interactive Dashboard:** Build a high-performance Streamlit application for orderbook management, IoT telemetry simulation, and market analytics.

---

### 🔬 Methodology & Implementation
* **Smart Contract Layer:** Built using Solidity `^0.8.0` with OpenZeppelin security modules (`ReentrancyGuard`, `ERC20`). Deployed and tested using Truffle, Ganache, and Hardhat.
* **IoT & Telemetry Integration:** Simulated 24-hour prosumer telemetry profiles (solar generation vs. household load) with automated smart contract listing triggers.
* **Oracle Feeds:** Integrated Chainlink decentralized price feeds (`AggregatorV3Interface`) and off-chain telemetry verification contracts.
* **Web3 DEX Control Center:** Streamlit Light Mode frontend powered by `web3.py` for real-time orderbook management, single-click purchases, and transaction ledger visualizer.

---

### 💡 Key Findings & Industry Impact
1. **Decentralization Enhances Transparency:** Blockchain provides an immutable, auditable transaction ledger, building trust between energy sellers and buyers.
2. **Automated Efficiency:** Smart contracts remove third-party brokerages, lowering administrative overhead and facilitating instant settlement.
3. **Scalability & Adoption:** Widespread adoption requires intuitive web interfaces and integration with physical smart meters.

---

### 🔮 Future Roadmap & Recommendations
* **IoT Smart Meter Integration:** Hardware integration with physical IoT energy meters via Chainlink oracle nodes.
* **Regulatory & Microgrid Compliance:** Alignment with local grid distribution regulations and carbon credit offset tracking.
* **Dynamic Tariff Algorithms:** Automated algorithmic pricing based on real-time microgrid supply/demand ratios.

---

## 🚀 App Features

* **⚡ Decentralized Microgrid Trading:** Direct prosumer-to-consumer P2P trading without intermediary utility fees.
* **🛡️ Secure Smart Contracts:** `MarketContract.sol` with `ReentrancyGuard`, partial-fill order execution, and safe ETH/ERC-20 token settlements.
* **📊 Interactive Streamlit DEX Dashboard:** Crisp Light Mode UI featuring active orderbook management, listing creation, and live transaction ledgers.
* **☀️ Smart Meter Telemetry Simulator:** Real-time IoT generation vs. consumption sliders with automated smart-contract listing triggers.
* **📈 Rich P2P Analytics:** Interactive Plotly visual charts tracking volume distributions, pricing trends, and past settlement history.
* **🔗 Chainlink Oracles:** Integrated decentralized ETH/USD price feeds and verified off-chain smart meter audit logs.

---

## 🏗️ Architecture Overview

```mermaid
graph TD
    A[Prosumer Solar/Wind IoT Meter] -->|Telemetry| B(Smart Meter Simulator)
    B -->|Auto-Trigger| C[MarketContract.sol]
    D[Buyer Wallet] -->|Execute Partial Purchase| C
    C -->|Reentrancy Safe Ether Transfer| E[Seller Wallet]
    F[Chainlink Oracle Node] -->|Verified Telemetry Logs| C
    C -->|Web3.py Event Stream| G[Streamlit DEX App]
```

---

## 💻 Tech Stack

- **Smart Contracts:** Solidity `^0.8.0`, OpenZeppelin Security Standards (`ReentrancyGuard`, `ERC20`).
- **Blockchain Framework:** Truffle / Hardhat / Ganache local node integration.
- **Frontend Dashboard:** Python 3.10+, Streamlit, Plotly, Pandas.
- **Web3 Connector:** `web3.py` client library for EVM network RPC calls.

---

## ⚙️ Getting Started

### Prerequisites

Ensure you have the following installed on your system:
- **Python 3.10+**
- **Node.js** (v18+) & **npm** / **Truffle** or **Ganache-cli**

### Quick Start (One-Click Launcher)

Run the included automated setup script to set up virtual environments, install dependencies, and launch the Streamlit app:

```bash
chmod +x setup.sh
./setup.sh
```

### Manual Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/surupi/Energy_Trading_Blockchain.git
   cd Energy_Trading_Blockchain
   ```

2. **Set Up Python Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Launch Streamlit Dashboard:**
   ```bash
   cd streamlit_app
   streamlit run app.py
   ```
   Open `http://localhost:8501` in your browser.

---

## 📁 Repository Structure

```
Energy_Trading_Blockchain/
├── backend/
│   └── contracts/
│       ├── EnergyDataContract.sol   # Chainlink oracle telemetry contract
│       ├── EnergySwapToken.sol     # ERC-20 token standard
│       ├── MarketContract.sol       # P2P marketplace & partial-fill logic
│       └── UserContract.sol         # Role-based access control (Buyer/Seller)
├── streamlit_app/
│   ├── app.py                       # Main Streamlit DEX application & Light Theme
│   ├── web3_service.py              # Web3.py RPC connector layer
│   └── .streamlit/
│       └── config.toml              # Streamlit Light theme configuration
├── setup.sh                         # Automated launcher script
├── requirements.txt                 # Python dependencies
├── .gitignore                       # Ignored build, venv, and binary artifacts
└── README.md                        # Documentation & Project Report
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to open an Issue or submit a Pull Request.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
