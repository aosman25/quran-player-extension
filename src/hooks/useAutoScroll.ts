import { useCallback, useEffect, useRef } from 'react';
import { scroller, animateScroll as scroll } from 'react-scroll';
import { Play } from '../types';
import { 
  SCROLL_DURATIONS, 
  INSTANT_SCROLL_OPTIONS,
  createScrollOptions,
  getScrollOffset
} from '../constants/scrollConfig';

interface UseAutoScrollProps {
  playlist: Play[];
  playing: number;
  pageWidth: number;
}

interface UseAutoScrollReturn {
  scrollToCurrentItem: (playingId: number, delay?: number) => void;
  scrollToTop: () => void;
  setupAutoScrollOnUserActivity: (containerRef: React.RefObject<HTMLElement>) => () => void;
}

/**
 * Custom hook for managing auto-scroll functionality
 * Centralizes scroll logic and removes redundant code
 */
export const useAutoScroll = ({ 
  playlist, 
  playing, 
  pageWidth 
}: UseAutoScrollProps): UseAutoScrollReturn => {
  const playlistRef = useRef<Play[]>(playlist);
  const playingRef = useRef<number>(playing);
  const scrollTimeoutRef = useRef<number | null>(null);
  const debounceTimeoutRef = useRef<number | null>(null);

  // Keep refs updated
  useEffect(() => {
    playlistRef.current = playlist;
    playingRef.current = playing;
  }, [playlist, playing]);

  /**
   * Scroll to the currently playing item with debouncing to prevent spam
   */
  const scrollToCurrentItem = useCallback((playingId: number, delay: number = 0) => {
    const executeScroll = () => {
      if (playlistRef.current.length === 0 || playingRef.current < 0) {
        return;
      }

      const currentItem = playlistRef.current[playingId];
      if (!currentItem) return;

      const targetId = String(currentItem.id);
      
      // Use instant scroll (no smooth animation) when delay is INSTANT
      const isInstant = delay === SCROLL_DURATIONS.INSTANT;
      const scrollOptions = isInstant 
        ? {
            smooth: false,
            duration: 0,
            offset: getScrollOffset(pageWidth),
          }
        : createScrollOptions(pageWidth, delay, 'easeInOutQuart');

      scroller.scrollTo(targetId, scrollOptions);
    };

    // Clear any existing debounce timeout
    if (debounceTimeoutRef.current) {
      clearTimeout(debounceTimeoutRef.current);
    }

    // For smooth scrolls, debounce to prevent spam with reduced delay for better responsiveness
    if (delay === SCROLL_DURATIONS.SMOOTH || delay === SCROLL_DURATIONS.EXTRA_SMOOTH || delay === SCROLL_DURATIONS.AUTO_SCROLL_DELAY) {
      debounceTimeoutRef.current = setTimeout(executeScroll, Math.max(delay, 100));
    } else {
      // For instant scrolls, execute immediately
      if (delay > 0) {
        setTimeout(executeScroll, delay);
      } else {
        executeScroll();
      }
    }
  }, [pageWidth]);

  /**
   * Scroll to top of the page
   */
  const scrollToTop = useCallback(() => {
    scroll.scrollToTop(INSTANT_SCROLL_OPTIONS);
  }, []);

  /**
   * Setup auto-scroll behavior on user activity (scroll/mouse move)
   * Returns cleanup function
   */
  const setupAutoScrollOnUserActivity = useCallback((
    containerRef: React.RefObject<HTMLElement>
  ) => {
    const handleUserActivity = () => {
      // Clear existing timeout
      if (scrollTimeoutRef.current) {
        clearTimeout(scrollTimeoutRef.current);
      }

      // Disable pointer events during scroll
      if (containerRef.current) {
        containerRef.current.style.pointerEvents = "none";
      }

      // Set new timeout to re-enable interactions and auto-scroll
      scrollTimeoutRef.current = setTimeout(() => {
        if (containerRef.current) {
          containerRef.current.style.pointerEvents = "initial";
        }
        scrollToCurrentItem(playingRef.current, SCROLL_DURATIONS.SMOOTH);
      }, SCROLL_DURATIONS.SCROLL_TIMEOUT);
    };

    const handleMouseMove = () => {
      // Clear timeout and restore pointer events on mouse move
      if (scrollTimeoutRef.current) {
        clearTimeout(scrollTimeoutRef.current);
      }
      
      if (containerRef.current) {
        containerRef.current.style.pointerEvents = "initial";
      }
    };

    // Add event listeners
    window.addEventListener("scroll", handleUserActivity);
    window.addEventListener("mousemove", handleMouseMove);

    // Return cleanup function
    return () => {
      window.removeEventListener("scroll", handleUserActivity);
      window.removeEventListener("mousemove", handleMouseMove);
      if (scrollTimeoutRef.current) {
        clearTimeout(scrollTimeoutRef.current);
      }
      if (debounceTimeoutRef.current) {
        clearTimeout(debounceTimeoutRef.current);
      }
    };
  }, [scrollToCurrentItem]);

  return {
    scrollToCurrentItem,
    scrollToTop,
    setupAutoScrollOnUserActivity,
  };
};
