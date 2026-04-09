function ResultsSection() {
  return (
    <div className="bg-white/5 backdrop-blur-lg border border-white/10 p-8 rounded-2xl shadow-2xl">
      <h2 className="text-2xl font-semibold text-primary mb-6">
        Scan Results
      </h2>

      <div className="bg-slate-900 p-6 rounded-lg text-gray-400 text-center">
        No vulnerabilities detected yet.
      </div>
    </div>
  )
}

export default ResultsSection
