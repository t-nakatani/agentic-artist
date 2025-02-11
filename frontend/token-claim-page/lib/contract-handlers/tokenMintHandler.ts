import { ethers } from 'ethers';
import { SmartContract } from './smartContractHandler';
import { address, abi } from './config/tokenMint';

export class TokenMintHandler extends SmartContract {
    constructor(provider: ethers.Provider | ethers.Signer) {
        super(provider, address, abi);
    }

    async mint(): Promise<void> {
        await this.contract.mint();
    }
}
