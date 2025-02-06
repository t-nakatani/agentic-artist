// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./AllocationStorage.sol";

contract AllocationStorageFactory {
    address public owner;

    uint256 public nextArtistId = 1;
    AllocationStorage[] public deployedAllocations;

    mapping(uint256 => address) public artistId2Contract;
    mapping(string => uint256) public artistName2Id;
    
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    event AllocationStorageCreated(
        address indexed contractAddress,
        uint256 indexed artistId,
        uint256 maxAllocation,
        address indexed owner,
        string artistName
    );

    constructor() {
        owner = msg.sender;
    }

    // @dev called by the artist agent
    function createAllocationStorage(
        string memory _artistName,
        uint256 _maxAllocation
    ) external returns (address) {
        require(artistName2Id[_artistName] == 0, "Artist name already exists");

        uint256 currentArtistId = nextArtistId;
        nextArtistId++;

        AllocationStorage newAllocation = new AllocationStorage(msg.sender, currentArtistId, _maxAllocation);

        deployedAllocations.push(newAllocation);
        artistName2Id[_artistName] = currentArtistId;
        artistId2Contract[currentArtistId] = address(newAllocation);


        emit AllocationStorageCreated(
            address(newAllocation),
            currentArtistId,
            _maxAllocation,
            msg.sender,
            _artistName
        );
        return address(newAllocation);
    }

    function getDeployedAllocations() external view returns (AllocationStorage[] memory) {
        return deployedAllocations;
    }

    function getContractByArtistId(uint256 _artistId) external view returns (address) {
        return artistId2Contract[_artistId];
    }

    function getAddressByArtistName(string memory _artistName) external view returns (address) {
        uint256 artistId = artistName2Id[_artistName];
        return artistId2Contract[artistId];
    }
}
