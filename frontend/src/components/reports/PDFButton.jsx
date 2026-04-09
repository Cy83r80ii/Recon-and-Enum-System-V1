export default function PDFButton(){

  function downloadReport(){
  
  window.open("http://127.0.0.1:8001/report")
  
  }
  
  return(
  
  <button onClick={downloadReport}>
  Download PDF Report
  </button>
  
  )
  
  }