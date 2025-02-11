import { ANIMATION_CONFIG } from '@/lib/constants'
import { BackgroundImage } from './BackgroundImage'

interface BackgroundRowProps {
  rowIndex: number
  images: Array<{
    src: string
    href: string
  }>
}

export function BackgroundRow({ rowIndex, images }: BackgroundRowProps) {
  const scrollDirection = rowIndex < 2 ? 'left' : 'right'
  
  return (
    <div className="background-row relative overflow-hidden flex-1 py-4">
      <div className="overflow-hidden h-full">
        <div
          className={`flex h-full animate-scroll-${scrollDirection}-${rowIndex}`}
          style={{
            width: `${images.length * (100 / ANIMATION_CONFIG.ROWS * 1.2 + 16)}vw`,
          }}
        >
          {images.map((image, imgIndex) => (
            <BackgroundImage
              key={`${image.src}-${imgIndex}`}
              src={image.src}
              rowIndex={rowIndex}
              rowCount={ANIMATION_CONFIG.ROWS}
              href={image.href}
            />
          ))}
        </div>
      </div>
    </div>
  )
}
