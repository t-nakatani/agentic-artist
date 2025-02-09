// This setup uses Hardhat Ignition to manage smart contract deployments.
// Learn more about it at https://hardhat.org/ignition

import { buildModule } from "@nomicfoundation/hardhat-ignition/modules";

const MintableTokenModule = buildModule("MintableTokenModule", (module) => {
  const allocationStorage = "0xF7Bc8ADae2B0Ba136f4b0e288099728239AC41b2";
  const mintableToken = module.contract("MintableToken", [allocationStorage]);

  return { mintableToken };
});

export default MintableTokenModule;
