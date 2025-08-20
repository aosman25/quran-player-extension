import { useCallback, useEffect, useRef } from 'react';

interface UseProgressBarProps {
  lang: string;
  audioState: { playing: boolean; duration: number } | null;
  onProgressChange: (time: number) => void;
}

export const useProgressBar = ({ lang, audioState, onProgressChange }: UseProgressBarProps) => {
  const containerRef = useRef<HTMLDivElement>(null);
  const pointerRef = useRef<HTMLDivElement>(null);
  const progressRef = useRef<HTMLDivElement>(null);
  const isDraggingRef = useRef<boolean>(false);

  const positionPointer = useCallback((pointer: HTMLDivElement, x: number, isRtl: boolean) => {
    if (isRtl) {
      pointer.style.right = `${x}px`;
      pointer.style.left = "auto";
    } else {
      pointer.style.left = `${x}px`;
      pointer.style.right = "auto";
    }
  }, []);

  // Removed updateProgressPosition - no longer needed as we handle progress manually

  const resetProgress = useCallback(() => {
    if (!progressRef.current || !pointerRef.current) return;
    
    const progress = progressRef.current;
    const pointer = pointerRef.current;
    const isRtl = lang === "ar";

    progress.style.transition = "none";
    pointer.style.transition = "none";
    progress.style.width = "0";
    positionPointer(pointer, -5, isRtl);
  }, [lang, positionPointer]);

  const handleProgressClick = useCallback((e: React.MouseEvent<HTMLDivElement>) => {
    if (!containerRef.current || !audioState?.duration) return;

    const container = containerRef.current;
    const containerRect = container.getBoundingClientRect();
    const maxX = containerRect.width;
    const isRtl = lang === "ar";

    let clickX;
    if (isRtl) {
      clickX = containerRect.right - e.clientX;
    } else {
      clickX = e.clientX - containerRect.left;
    }

    const progress = Math.max(0, Math.min(1, clickX / maxX));
    onProgressChange(progress * audioState.duration);
  }, [lang, audioState, onProgressChange]);

  useEffect(() => {
    if (!containerRef.current) return;
    const container = containerRef.current;
    container.style.direction = lang === "ar" ? "rtl" : "ltr";
  }, [lang]);

  return {
    containerRef,
    pointerRef,
    progressRef,
    isDraggingRef,
    positionPointer,
    resetProgress,
    handleProgressClick,
  };
};
