import { useCallback, useEffect, useRef } from 'react';

interface UseAudioEventsProps {
  audioRef: React.RefObject<HTMLAudioElement>;
  playingStateRef: React.RefObject<boolean>;
  onLoadingChange: (isLoading: boolean) => void;
  onPlaybackError?: () => void;
}

export const useAudioEvents = ({
  audioRef,
  playingStateRef,
  onLoadingChange,
  onPlaybackError,
}: UseAudioEventsProps) => {
  const loadingTimeoutRef = useRef<ReturnType<typeof setTimeout>>();

  const clearLoadingTimeout = useCallback(() => {
    if (loadingTimeoutRef.current) {
      clearTimeout(loadingTimeoutRef.current);
      loadingTimeoutRef.current = undefined;
    }
  }, []);

  useEffect(() => {
    const audio = audioRef.current;
    if (!audio) return;

    const handleWaiting = () => {
      clearLoadingTimeout();
      loadingTimeoutRef.current = setTimeout(() => {
        if (!audio.paused && audio.readyState < 3) {
          onLoadingChange(true);
        }
      }, 500);
    };

    const handlePlaying = () => {
      clearLoadingTimeout();
      onLoadingChange(false);
    };

    const handleLoadStart = () => {
      clearLoadingTimeout();
      if (!audio.paused || playingStateRef.current) {
        onLoadingChange(true);
      }
    };

    const handleCanPlay = () => {
      clearLoadingTimeout();
      onLoadingChange(false);
    };

    const handlePause = () => {
      clearLoadingTimeout();
      if (audio.readyState >= 3) {
        onLoadingChange(false);
      }
    };

    const handleError = () => {
      if (!navigator.onLine && (playingStateRef.current || !audio.paused)) {
        onLoadingChange(true);
      } else {
        onLoadingChange(false);
      }
      onPlaybackError?.();
    };

    const handleOnline = () => {
      if (audio.error || audio.readyState < 3) {
        audio.load();
        if (playingStateRef.current || !audio.paused) {
          onLoadingChange(true);
        }
      }
    };

    const handleOffline = () => {
      if (playingStateRef.current || !audio.paused) {
        onLoadingChange(true);
      }
    };

    // Initial network check
    if (!navigator.onLine && (playingStateRef.current || !audio.paused)) {
      onLoadingChange(true);
    }

    // Add event listeners
    audio.addEventListener('waiting', handleWaiting);
    audio.addEventListener('playing', handlePlaying);
    audio.addEventListener('loadstart', handleLoadStart);
    audio.addEventListener('canplay', handleCanPlay);
    audio.addEventListener('pause', handlePause);
    audio.addEventListener('error', handleError);
    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);

    return () => {
      clearLoadingTimeout();
      audio.removeEventListener('waiting', handleWaiting);
      audio.removeEventListener('playing', handlePlaying);
      audio.removeEventListener('loadstart', handleLoadStart);
      audio.removeEventListener('canplay', handleCanPlay);
      audio.removeEventListener('pause', handlePause);
      audio.removeEventListener('error', handleError);
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
    };
  }, [audioRef, playingStateRef, onLoadingChange, onPlaybackError, clearLoadingTimeout]);
};
