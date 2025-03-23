// src/services/userService.js
import axios from 'axios'
import api from '../services/api'


const API_URL = 'http://localhost:5000'


const userService = {

  listUsers() {
    return axios.get(`${API_URL}/users/list`)
  },

  viewUser(id) {
    return api.get(`${API_URL}/users/view/${id}`)
  },
  createUser(userData) {
    return api.post(`${API_URL}/users/create`, userData)
  },  
  updateUser(id, userData) {
    return api.put(`${API_URL}/users/update/${id}`, userData)
  },  
  deleteUser(id) {
    return api.delete(`${API_URL}/users/delete/${id}`)
  }
}

export default userService
