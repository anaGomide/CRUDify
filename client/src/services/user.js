import axios from 'axios'

const apiUrl = import.meta.env.VITE_API_URL

const UserAPI = axios.create({
  baseURL: apiUrl // Substitua pela URL da sua API, se houver
})

export default UserAPI
