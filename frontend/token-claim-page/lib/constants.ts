export const ANIMATION_CONFIG = {
  BANNER_HEIGHT: 320,
  BACKGROUND_ROW_HEIGHT: 'calc(100vh / 4)', // 画面の高さを4等分
  ROWS: 4,
  ROW_SPEEDS: [
    24, // 1段目（一番上）: やや遅め
    48, // 2段目: 標準速度
    48, // 3段目: やや速め
    24  // 4段目（一番下）: 最も遅め
  ],
} as const

export const ANIMATION_STYLES = `
  @keyframes scrollLeft {
    0% {
      transform: translateX(0);
    }
    100% {
      transform: translateX(-50%);
    }
  }

  @keyframes scrollRight {
    0% {
      transform: translateX(-50%);
    }
    100% {
      transform: translateX(0);
    }
  }

  ${ANIMATION_CONFIG.ROW_SPEEDS.map((speed, index) => `
    .animate-scroll-left-${index} {
      display: flex;
      animation: scrollLeft ${speed}s linear infinite;
    }

    .animate-scroll-right-${index} {
      display: flex;
      animation: scrollRight ${speed}s linear infinite;
    }
  `).join('\n')}

  .background-row:hover .animate-scroll-left-0,
  .background-row:hover .animate-scroll-left-1,
  .background-row:hover .animate-scroll-left-2,
  .background-row:hover .animate-scroll-left-3,
  .background-row:hover .animate-scroll-right-0,
  .background-row:hover .animate-scroll-right-1,
  .background-row:hover .animate-scroll-right-2,
  .background-row:hover .animate-scroll-right-3 {
    animation-play-state: paused;
  }

  .background-image {
    transition: all 0.3s ease;
    opacity: 0.15;
  }

  .background-image:hover {
    transform: scale(1.05);
    opacity: 0.3;
  }
` 