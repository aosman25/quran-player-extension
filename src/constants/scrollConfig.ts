/**
 * Centralized scroll configuration constants
 * Removes hard-coded values and provides consistent scroll behavior
 */

// Breakpoint for responsive scroll offsets
export const MOBILE_BREAKPOINT = 800;

// Scroll offset values
export const SCROLL_OFFSETS = {
  MOBILE: -165,
  DESKTOP: -120,
} as const;

// Scroll durations
export const SCROLL_DURATIONS = {
  INSTANT: 0,
  SMOOTH: 500,
  EXTRA_SMOOTH: 800,
  AUTO_SCROLL_DELAY: 1000,
  SCROLL_TIMEOUT: 3500,
} as const;

// Default scroll options for react-scroll with easing
export const DEFAULT_SCROLL_OPTIONS = {
  smooth: 'easeInOutQuart',
} as const;

// Scroll options for immediate scrolling (no animation)
export const INSTANT_SCROLL_OPTIONS = {
  smooth: false,
  duration: SCROLL_DURATIONS.INSTANT,
} as const;

// Scroll options for smooth animated scrolling
export const SMOOTH_SCROLL_OPTIONS = {
  ...DEFAULT_SCROLL_OPTIONS,
  duration: SCROLL_DURATIONS.SMOOTH,
} as const;

// Scroll options for extra smooth animated scrolling
export const EXTRA_SMOOTH_SCROLL_OPTIONS = {
  ...DEFAULT_SCROLL_OPTIONS,
  duration: SCROLL_DURATIONS.EXTRA_SMOOTH,
} as const;

/**
 * Get appropriate scroll offset based on page width
 */
export const getScrollOffset = (pageWidth: number): number => {
  return pageWidth <= MOBILE_BREAKPOINT 
    ? SCROLL_OFFSETS.MOBILE 
    : SCROLL_OFFSETS.DESKTOP;
};

/**
 * Create scroll options with responsive offset and easing
 */
export const createScrollOptions = (
  pageWidth: number,
  duration: number = SCROLL_DURATIONS.SMOOTH,
  easing: string | boolean = 'easeInOutQuart'
) => ({
  smooth: easing,
  duration,
  offset: getScrollOffset(pageWidth),
});
