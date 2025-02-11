import { ethers } from 'ethers';
import { SmartContract } from './smartContractHandler';
import { address, abi } from './config/allocationStorage';

export class AllocationStorageHandler extends SmartContract {
    constructor(provider: ethers.Provider | ethers.Signer) {
        super(provider, address, abi);
    }

    async getAllocation(address: string): Promise<number> {
        const allocation = await this.contract.getAllocation(address);
        return Number(allocation);
    }
}
