// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./UserContract.sol";
import "./EnergyDataContract.sol";

abstract contract ReentrancyGuard {
    uint256 private constant _NOT_ENTERED = 1;
    uint256 private constant _ENTERED = 2;
    uint256 private _status;

    constructor() {
        _status = _NOT_ENTERED;
    }

    modifier nonReentrant() {
        require(_status != _ENTERED, "ReentrancyGuard: reentrant call");
        _status = _ENTERED;
        _;
        _status = _NOT_ENTERED;
    }
}

contract MarketContract is ReentrancyGuard {
    struct Listing {
        uint256 id;
        address seller;
        uint256 units;
        uint256 pricePerUnit;
        bool active;
    }

    struct Transaction {
        uint256 id;
        uint256 listingId;
        address buyer;
        address seller;
        uint256 units;
        uint256 totalCost;
        uint256 timestamp;
    }

    UserContract public userContract;
    EnergyDataContract public energyDataContract;

    Transaction[] public transactions;
    Listing[] public listings;
    uint256 public nextListingId;
    uint256 public nextTxId;

    event ListingCreated(uint256 indexed listingId, address indexed seller, uint256 units, uint256 pricePerUnit);
    event PurchaseEvent(uint256 indexed listingId, address indexed buyer, address indexed seller, uint256 units, uint256 totalCost);

    constructor(address _userContract, address _energyDataContract) {
        userContract = UserContract(_userContract);
        energyDataContract = EnergyDataContract(_energyDataContract);
    }

    function addListing(uint256 units, uint256 pricePerUnit) public {
        require(units > 0, "Units must be greater than 0");
        require(pricePerUnit > 0, "Price must be greater than 0");
        UserContract.Role role = userContract.getUserRole(msg.sender);
        require(role == UserContract.Role.Seller, "Only sellers can add listings");   
        
        listings.push(Listing(nextListingId, msg.sender, units, pricePerUnit, true));
        emit ListingCreated(nextListingId, msg.sender, units, pricePerUnit);
        nextListingId++;
    }

    function purchase(uint256 listingId, uint256 unitsToBuy) public payable nonReentrant {
        require(listingId < listings.length, "Invalid listing ID");
        Listing storage listing = listings[listingId];
        UserContract.Role role = userContract.getUserRole(msg.sender);

        require(listing.active, "Listing is not active");
        require(role == UserContract.Role.Buyer, "Only buyers can purchase");
        require(unitsToBuy > 0 && unitsToBuy <= listing.units, "Invalid units requested");
        
        uint256 totalCost = listing.pricePerUnit * unitsToBuy;
        require(msg.value == totalCost, "Incorrect Ether amount sent");

        listing.units -= unitsToBuy;
        if (listing.units == 0) {
            listing.active = false;
        }

        transactions.push(Transaction(nextTxId++, listingId, msg.sender, listing.seller, unitsToBuy, totalCost, block.timestamp));

        // Transfer funds using low-level call for safety
        (bool success, ) = payable(listing.seller).call{value: totalCost}("");
        require(success, "Transfer to seller failed");

        emit PurchaseEvent(listingId, msg.sender, listing.seller, unitsToBuy, totalCost);
    }

    function getListingCount() public view returns (uint256) {
        return listings.length;
    }

    function getTransactionCount() public view returns (uint256) {
        return transactions.length;
    }
}

