// This setup uses Hardhat Ignition to manage smart contract deployments.
// Learn more about it at https://hardhat.org/ignition

import { buildModule } from "@nomicfoundation/hardhat-ignition/modules";

const AllocationStorageFactoryModule = buildModule("AllocationStorageFactoryModule", (module) => {
  const allocationStorageFactory = module.contract("AllocationStorageFactory");

  return { allocationStorageFactory };
});

export default AllocationStorageFactoryModule;
