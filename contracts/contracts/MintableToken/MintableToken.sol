// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "../Allocation/AllocationStorage.sol";


contract MintableToken is ERC20, Ownable {
    AllocationStorage public allocationStorage;

    constructor(
        address _allocationStorage
    ) ERC20("MintableToken", "MT") Ownable(msg.sender) {
        allocationStorage = AllocationStorage(_allocationStorage);
    }

    // TODO: fix infinite minting
    function mint() public onlyOwner {
        uint256 allocationAmount = allocationStorage.getAllocation(msg.sender);
        require(allocationAmount > 0, "Allocation amount is 0");
        _mint(msg.sender, allocationAmount * 1 ether);
    }

    function getAllocationStorage() public view returns (address) {
        return address(allocationStorage);
    }
}
