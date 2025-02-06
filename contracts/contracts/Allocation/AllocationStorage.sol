// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AllocationStorage {
    address public owner;

    uint256 public artistId;
    uint256 public remainingAllocation;
    mapping(address => uint256) public allocation;

    constructor(address _artistAddress, uint256 _artistId, uint256 _maxAllocation) {
        owner = _artistAddress;
        artistId = _artistId;
        remainingAllocation = _maxAllocation;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    function getOwner() external view returns (address) {
        return owner;
    }

    function getArtistId() external view returns (uint256) {
        return artistId;
    }

    function getAllocation(address _address) external view returns (uint256) {
        return allocation[_address];
    }

    function getRemainingAllocation() external view returns (uint256) {
        return remainingAllocation;
    }

    function updateAllocation(address _address, uint256 _allocation) external onlyOwner {
        require(_allocation <= remainingAllocation, "Allocation exceeds remaining allocation");
        remainingAllocation -= _allocation;
        allocation[_address] = _allocation;
    }


}
