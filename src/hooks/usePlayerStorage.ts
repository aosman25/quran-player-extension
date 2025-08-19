import { useCallback } from 'react';

interface PlayerStorageData {
  paused?: boolean;
  currentTime?: number;
  volume?: number;
  loop?: boolean;
  playing?: number;
}

export const usePlayerStorage = (storageKey: string) => {
  const getStoredData = useCallback((): PlayerStorageData => {
    const stored = localStorage.getItem(storageKey);
    return stored ? JSON.parse(stored) : {};
  }, [storageKey]);

  const updateStoredData = useCallback((newData: Partial<PlayerStorageData>) => {
    const currentData = getStoredData();
    localStorage.setItem(
      storageKey,
      JSON.stringify({
        ...currentData,
        ...newData,
      })
    );
  }, [storageKey, getStoredData]);

  return {
    getStoredData,
    updateStoredData,
  };
};
