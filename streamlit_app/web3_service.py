import os
import json
from web3 import Web3

class Web3Service:
    def __init__(self, rpc_url="http://127.0.0.1:8545"):
        self.rpc_url = rpc_url
        self.w3 = Web3(Web3.HTTPProvider(self.rpc_url))
        self.connected = self.w3.is_connected()
        
    def get_accounts(self):
        if not self.connected:
            # Fallback simulated accounts for offline/demo mode
            return [
                "0x70997970C51812dc3A010C7d01b50e0d17dc79C8",
                "0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC",
                "0x90F79bf6EB2c4f870365E785982E1f101E93b906",
                "0x15d34AAf54267DB7D7c367839AAf71A00a2C6A65"
            ]
        return self.w3.eth.accounts

    def get_balance(self, address):
        if not self.connected:
            return 10.5
        balance_wei = self.w3.eth.get_balance(address)
        return float(self.w3.from_wei(balance_wei, 'ether'))

    def get_mock_listings(self):
        return [
            {
                "id": 0,
                "seller": "0x70997970C51812dc3A010C7d01b50e0d17dc79C8",
                "units": 45,
                "price_per_unit_eth": 0.002,
                "total_cost_eth": 0.09,
                "energy_type": "Solar PV",
                "active": True
            },
            {
                "id": 1,
                "seller": "0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC",
                "units": 120,
                "price_per_unit_eth": 0.0018,
                "total_cost_eth": 0.216,
                "energy_type": "Wind Turbine",
                "active": True
            },
            {
                "id": 2,
                "seller": "0x90F79bf6EB2c4f870365E785982E1f101E93b906",
                "units": 20,
                "price_per_unit_eth": 0.0025,
                "total_cost_eth": 0.05,
                "energy_type": "Biomass / Hydro",
                "active": True
            }
        ]

    def get_mock_transactions(self):
        return [
            {
                "id": 101,
                "listing_id": 4,
                "buyer": "0x15d34AAf54267DB7D7c367839AAf71A00a2C6A65",
                "seller": "0x70997970C51812dc3A010C7d01b50e0d17dc79C8",
                "units": 30,
                "total_cost_eth": 0.06,
                "timestamp": "2026-08-24 12:45:10"
            },
            {
                "id": 102,
                "listing_id": 5,
                "buyer": "0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC",
                "seller": "0x90F79bf6EB2c4f870365E785982E1f101E93b906",
                "units": 15,
                "total_cost_eth": 0.0375,
                "timestamp": "2026-08-24 13:10:05"
            }
        ]
