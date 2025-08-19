import { useCallback, useEffect, useRef, useState } from 'react';
import { usePlayerStorage } from './usePlayerStorage';

interface AudioStateProps {
  storageKey: string;
  extensionMode?: boolean;
  onPlayingChange?: (playing: boolean) => void;
}

export const useAudioState = ({ storageKey, extensionMode, onPlayingChange }: AudioStateProps) => {
  const { updateStoredData } = usePlayerStorage(storageKey);

  const [audioState, setAudioState] = useState<{
    playing: boolean;
    duration: number;
  } | null>(() => ({
    playing: false,
    duration: 0
  }));

  const playingStateRef = useRef<boolean>(false);
  const audioInitializedRef = useRef<boolean>(false);

  const saveData = useCallback((audio: HTMLAudioElement, isPlaying: boolean) => {
    updateStoredData({
      paused: !isPlaying,
      currentTime: audio.currentTime,
    });
  }, [updateStoredData]);

  const playAudio = useCallback(async (audio: HTMLAudioElement) => {
    try {
      await audio.play();

      playingStateRef.current = true;
      saveData(audio, true);
      
      if (extensionMode) {
        if (audioInitializedRef.current) {
          chrome.runtime.sendMessage({ type: "PLAY_AUDIO" });
        }
        audioInitializedRef.current = true;
      }
      onPlayingChange?.(true);
    } catch (error) {
      console.error('Error playing audio:', error);
      playingStateRef.current = false;
      saveData(audio, false);
      onPlayingChange?.(false);
    }
  }, [extensionMode, saveData, onPlayingChange]);

  const pauseAudio = useCallback((audio: HTMLAudioElement) => {
    try {
      audio.pause();

      playingStateRef.current = false;
      saveData(audio, false);
      
      if (extensionMode) {
        chrome.runtime.sendMessage({ type: "PAUSE_AUDIO" });
      }
      onPlayingChange?.(false);
    } catch (error) {
      console.error('Error pausing audio:', error);
    }
  }, [extensionMode, saveData, onPlayingChange]);

  // Cleanup on unmount
  useEffect(() => {
    return () => {
      if (audioState?.playing) {
        onPlayingChange?.(false);
      }
    };
  }, [audioState, onPlayingChange]);

  return {
    audioState,
    setAudioState,
    playingStateRef,
    playAudio,
    pauseAudio,
  };
};