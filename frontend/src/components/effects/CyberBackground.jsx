import { useEffect, useRef } from "react"

export default function CyberBackground(){

  const canvasRef = useRef(null)

  useEffect(()=>{

    const canvas = canvasRef.current
    const ctx = canvas.getContext("2d")

    canvas.width = window.innerWidth
    canvas.height = window.innerHeight

    const letters = "01"
    const fontSize = 16
    const columns = canvas.width / fontSize

    const drops = []

    for(let x=0;x<columns;x++){
      drops[x] = 1
    }

    function draw(){

      ctx.fillStyle = "rgba(0,0,0,0.05)"
      ctx.fillRect(0,0,canvas.width,canvas.height)

      ctx.fillStyle = "#ff0000"
      ctx.font = fontSize + "px monospace"

      for(let i=0;i<drops.length;i++){

        const text = letters[Math.floor(Math.random()*letters.length)]

        ctx.fillText(text,i*fontSize,drops[i]*fontSize)

        if(drops[i]*fontSize > canvas.height && Math.random()>0.975){
          drops[i] = 0
        }

        drops[i]++
      }
    }

    const interval = setInterval(draw,33)

    return ()=>clearInterval(interval)

  },[])

  return(

    <canvas
      ref={canvasRef}
      className="fixed top-0 left-0 w-full h-full opacity-20 -z-10"
    />

  )

}
