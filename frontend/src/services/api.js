import axios from "axios"

// 🔥 Use environment variable instead of localhost
const API = axios.create({
  baseURL: import.meta.env.VITE_API_URL
})

// API calls
export const startScan = (target, mode) =>
  API.post("/scan", { target, mode })

export const getResults = () =>
  API.get("/results")

export default API