import Image from 'next/image'

interface HoverOverlayProps {
  logoSrc: string
  text: string
}

export function HoverOverlay({ logoSrc, text }: HoverOverlayProps) {
  return (
    <div className="absolute inset-0 flex items-center justify-center">
      <div className="flex flex-col items-center opacity-0 group-hover:opacity-100 transition-opacity duration-300 bg-black/30 p-6 rounded-xl">
        <div className="relative w-48 h-12 mb-4">
          <Image
            src={logoSrc}
            alt="Hover overlay logo"
            fill
            style={{ objectFit: 'contain' }}
          />
        </div>
        
        <div className="text-white flex items-center gap-2">
          <span className="font-bold text-medium">{text}</span>
          <svg 
            xmlns="http://www.w3.org/2000/svg" 
            width="24" 
            height="24" 
            viewBox="0 0 24 24" 
            fill="none" 
            stroke="currentColor" 
            strokeWidth="2" 
            strokeLinecap="round" 
            strokeLinejoin="round"
          >
            <path d="M7 17L17 7" />
            <path d="M7 7h10v10" />
          </svg>
        </div>
      </div>
    </div>
  )
} 