import axios from "axios"

const API = axios.create({
  baseURL: "http://127.0.0.1:8001"
})

export const startScan = (target,mode) =>
  API.post("/scan",{target,mode})

export const getResults = () =>
  API.get("/results")

export default API
