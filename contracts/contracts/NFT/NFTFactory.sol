// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./SimpleNFT.sol";

contract NFTFactory {
    address[] public deployedNFTs;

    event NFTDeployed(address indexed nftAddress, address creator);

    function createNFTContract(string memory name, string memory symbol) public {
        SimpleNFT newNFT = new SimpleNFT(name, symbol);
        newNFT.transferOwnership(msg.sender);
        deployedNFTs.push(address(newNFT));
        emit NFTDeployed(address(newNFT), msg.sender);
    }

    function getDeployedNFTs() public view returns (address[] memory) {
        return deployedNFTs;
    }
}
