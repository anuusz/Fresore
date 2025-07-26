import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000', // Ganti ke URL backend Django
  withCredentials: false,
})

export default api
