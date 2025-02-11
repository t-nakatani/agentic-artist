import { useState } from 'react';
import { ethers } from 'ethers';
import { DEFAULT_CHAIN } from '../lib/chains';

declare global {
  interface Window {
    ethereum?: {
      request: (args: { method: string; params?: any[] }) => Promise<any>;
      isMetaMask?: boolean;
    };
  }
}

export const useWallet = () => {
  const [account, setAccount] = useState<string | null>(null);
  const [balance, setBalance] = useState<string | null>(null);
  const [isConnected, setIsConnected] = useState(false);

  const disconnectWallet = () => {
    setAccount(null);
    setBalance(null);
    setIsConnected(false);
  };

  const connectWallet = async () => {
    try {
      if (typeof window.ethereum === 'undefined') {
        alert('MetaMaskをインストールしてください');
        return;
      }

      try {
        await window.ethereum.request({
          method: 'wallet_switchEthereumChain',
          params: [{ chainId: DEFAULT_CHAIN.chainId }],
        });
      } catch (switchError: any) {
        if (switchError.code === 4902) {
          await window.ethereum.request({
            method: 'wallet_addEthereumChain',
            params: [DEFAULT_CHAIN],
          });
        }
      }

      const accounts = (await window.ethereum.request({ 
        method: 'eth_requestAccounts' 
      })) as string[];
      
      if (accounts[0]) {
        setAccount(accounts[0]);
        const provider = new ethers.BrowserProvider(window.ethereum as any);
        const balance = await provider.getBalance(accounts[0]);
        setBalance(ethers.formatEther(balance));
        setIsConnected(true);
      }
    } catch (error) {
      console.error('接続エラー:', error);
    }
  };

  return {
    account,
    balance,
    isConnected,
    connectWallet,
    disconnectWallet,
  };
}; 