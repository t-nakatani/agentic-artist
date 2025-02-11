export interface Chain {
  chainId: string;
  chainName: string;
  nativeCurrency: {
    name: string;
    symbol: string;
    decimals: number;
  };
  rpcUrls: string[];
  blockExplorerUrls: string[];
}

export const CHAINS: { [key: string]: Chain } = {
  BASE_SEPOLIA: {
    chainId: '0x14a34',  // 84532
    chainName: 'Base Sepolia (Testnet)',
    nativeCurrency: {
      name: 'ETH',
      symbol: 'ETH',
      decimals: 18
    },
    rpcUrls: ['https://sepolia.base.org'],
    blockExplorerUrls: ['https://sepolia.basescan.org']
  },
}

export const DEFAULT_CHAIN = CHAINS.BASE_SEPOLIA 