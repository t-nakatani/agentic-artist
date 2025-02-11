import { ANIMATION_CONFIG } from '@/lib/constants'
import { BackgroundRow } from './BackgroundRow'

interface AnimatedBackgroundProps {
  images: Array<{
    src: string
    href: string
  }>
}

export function AnimatedBackground({ images }: AnimatedBackgroundProps) {
  return (
    <div className="fixed inset-0 z-0 overflow-hidden flex flex-col h-screen">
      {[...Array(ANIMATION_CONFIG.ROWS)].map((_, index) => (
        <BackgroundRow
          key={index}
          rowIndex={index}
          images={images}
        />
      ))}
    </div>
  )
}
