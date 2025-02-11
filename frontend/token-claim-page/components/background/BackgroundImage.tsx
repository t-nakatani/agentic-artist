import Image from 'next/image'
import Link from 'next/link'
import { HoverOverlay } from './HoverOverlay'

interface BackgroundImageProps {
  src: string
  rowIndex: number
  rowCount: number
  href: string
  overlayLogo?: string
  overlayText?: string
}

export function BackgroundImage({ 
  src, 
  rowIndex, 
  rowCount, 
  href,
  overlayLogo = '/images/opensea_logo.png',
  overlayText = 'Browse in Opensea'
}: BackgroundImageProps) {
  return (
    <Link 
      href={href} 
      target="_blank"
      rel="noopener noreferrer"
      className="background-image group flex-shrink-0 mx-2 relative h-full hover:cursor-pointer"
      style={{
        width: `${100 / rowCount * 1.2}vw`,
      }}
    >
      <Image
        src={src}
        alt="Background image"
        fill
        style={{ objectFit: 'contain' }}
        priority={rowIndex === 0}
        className="transition-opacity duration-300"
      />
      
      <HoverOverlay logoSrc={overlayLogo} text={overlayText} />
    </Link>
  )
}
